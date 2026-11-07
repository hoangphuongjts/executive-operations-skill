"""Private local library + Google Books metadata client. Python stdlib only."""
from __future__ import annotations
import hashlib, json, os, re, secrets, sqlite3, threading, time, urllib.error, urllib.parse, urllib.request, zipfile
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from html.parser import HTMLParser
from xml.etree import ElementTree as ET

BASE = Path(os.environ.get('HP_EBOOK_HOME', str(Path.home() / 'HoangPhuongEbookLibrary'))).expanduser().resolve()
BASE.mkdir(parents=True, exist_ok=True)
IMPORT_DIR = Path(os.environ.get('EBOOK_IMPORT_DIR', str(BASE / 'imports'))).expanduser().resolve()
IMPORT_DIR.mkdir(parents=True, exist_ok=True)
STORE = BASE / 'books'
STORE.mkdir(exist_ok=True)
DB = BASE / 'books.sqlite3'
BOOKS_API = 'https://www.googleapis.com/books/v1/'
MAX_BOOK_BYTES = 50 * 1024 * 1024

class LibraryError(Exception): pass

class TextExtractor(HTMLParser):
    IGNORE = {'script', 'style', 'svg', 'iframe', 'object', 'noscript'}
    BLOCK = {'p', 'h1', 'h2', 'h3', 'h4', 'li', 'div', 'blockquote', 'br', 'section'}
    def __init__(self):
        super().__init__(convert_charrefs=True); self.parts=[]; self.hidden=0
    def handle_starttag(self, tag, attrs):
        if tag in self.IGNORE: self.hidden += 1
        elif not self.hidden and tag in self.BLOCK: self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in self.IGNORE and self.hidden: self.hidden -= 1
        elif not self.hidden and tag in self.BLOCK: self.parts.append('\n')
    def handle_data(self, data):
        if not self.hidden: self.parts.append(data)
    def result(self): return '\n'.join(x.strip() for x in ''.join(self.parts).splitlines() if x.strip())

def safe_epub_chapters(path: Path):
    if not zipfile.is_zipfile(path): raise LibraryError('EPUB ZIP không hợp lệ')
    with zipfile.ZipFile(path) as z:
        members = z.infolist()
        if len(members)>2500: raise LibraryError('Quá nhiều tệp trong EPUB')
        if sum(x.file_size for x in members)>200*1024*1024: raise LibraryError('EPUB giải nén vượt giới hạn')
        if 'META-INF/container.xml' not in z.namelist(): raise LibraryError('Thiếu cấu trúc EPUB')
        container=ET.fromstring(z.read('META-INF/container.xml'))
        rootfile=container.find('.//{*}rootfile')
        if rootfile is None: raise LibraryError('Thiếu OPF')
        opf_path=rootfile.attrib.get('full-path','')
        if not opf_path or opf_path not in z.namelist(): raise LibraryError('OPF không hợp lệ')
        package=ET.fromstring(z.read(opf_path))
        manifest={e.attrib.get('id'):e.attrib for e in package.findall('.//{*}manifest/{*}item')}
        spine=[e.attrib.get('idref') for e in package.findall('.//{*}spine/{*}itemref')]
        opf_dir=__import__('posixpath').dirname(opf_path)
        chapters=[]
        for idref in spine[:300]:
            item=manifest.get(idref,{})
            if item.get('media-type') not in {'application/xhtml+xml','text/html'}: continue
            rel=urllib.parse.unquote(item.get('href',''))
            fname=__import__('posixpath').normpath(__import__('posixpath').join(opf_dir,rel.split('#')[0]))
            if fname.startswith('../') or fname not in z.namelist(): continue
            if z.getinfo(fname).file_size > 3*1024*1024: continue
            page=z.read(fname).decode('utf-8',errors='replace')
            parser=TextExtractor();parser.feed(page)
            txt=parser.result()
            if txt: chapters.append({'index':len(chapters),'title':f'Phần {len(chapters)+1}', 'text':txt[:200000]})
        if not chapters: raise LibraryError('EPUB không có chương đọc được')
        return chapters

@contextmanager
def open_db():
    db=sqlite3.connect(DB,timeout=10)
    db.row_factory=sqlite3.Row
    db.execute('PRAGMA journal_mode=WAL')
    db.execute('CREATE TABLE IF NOT EXISTS books (id TEXT PRIMARY KEY, title TEXT NOT NULL, kind TEXT NOT NULL, filename TEXT NOT NULL, sha256 TEXT UNIQUE NOT NULL, added_at INTEGER NOT NULL, progress INTEGER NOT NULL DEFAULT 0, notes TEXT NOT NULL DEFAULT \'\')')
    db.commit()
    try:
        with db:
            yield db
    finally:
        db.close()

def list_books():
    with open_db() as db:
        return [dict(x) for x in db.execute('SELECT id,title,kind,filename,sha256,added_at,progress,notes FROM books ORDER BY added_at DESC')]

def find_book(book_id):
    if not re.fullmatch(r'[a-f0-9]{24}',book_id): raise LibraryError('ID sách không hợp lệ')
    with open_db() as db:
        x=db.execute('SELECT * FROM books WHERE id=?',(book_id,)).fetchone()
        if not x: raise LibraryError('Không tìm thấy sách')
        return dict(x)

def stored_path(book):return STORE/(book['sha256'] + ('.epub' if book['kind']=='epub' else '.pdf'))

def import_bytes(data:bytes, filename:str):
    if not data or len(data)>MAX_BOOK_BYTES:raise LibraryError('Kích thước ebook không hợp lệ (tối đa 50 MiB)')
    kind=Path(filename).suffix.lower().lstrip('.')
    if kind not in ('epub','pdf'): raise LibraryError('Chỉ chấp nhận EPUB và PDF')
    if kind=='pdf' and not data.startswith(b'%PDF-'):raise LibraryError('PDF sai định dạng')
    if kind=='epub' and not zipfile.is_zipfile(__import__('io').BytesIO(data)):raise LibraryError('EPUB sai định dạng')
    sha=hashlib.sha256(data).hexdigest()
    with open_db() as db:
        existing=db.execute('SELECT * FROM books WHERE sha256=?',(sha,)).fetchone()
        if existing:return {'book':dict(existing),'duplicate':True}
        book_id=secrets.token_hex(12)
        target=STORE/(sha+'.'+kind)
        target.write_bytes(data)
        try:
            if kind=='epub':safe_epub_chapters(target)
        except Exception:
            target.unlink(missing_ok=True);raise
        title=Path(filename).stem[:200] or 'Chưa đặt tên'
        db.execute('INSERT INTO books (id,title,kind,filename,sha256,added_at) VALUES (?,?,?,?,?,?)',(book_id,title,kind,Path(filename).name[:240],sha,int(time.time())))
        db.commit()
    return {'book':find_book(book_id),'duplicate':False}

def import_from_path(path:str):
    p=Path(path).expanduser().resolve()
    if not p.is_relative_to(IMPORT_DIR) or not p.is_file():raise LibraryError('Chỉ được nhập tệp trong thư mục nhập đã cấu hình')
    if p.stat().st_size>MAX_BOOK_BYTES:raise LibraryError('Tệp vượt giới hạn')
    return import_bytes(p.read_bytes(),p.name)

def save_progress(book_id,progress:int):
    find_book(book_id)
    if not 0<=progress<=100:raise LibraryError('Tiến độ cần từ 0 đến 100')
    with open_db() as db:db.execute('UPDATE books SET progress=? WHERE id=?',(progress,book_id));db.commit()
    return {'id':book_id,'progress':progress}

def _google_get(path:str, params:dict, token:str|None=None):
    if not path.startswith(('volumes','mylibrary/')):raise LibraryError('Đường dẫn API không được phép')
    q=urllib.parse.urlencode(params,doseq=True)
    url=BOOKS_API+path+'?'+q
    req=urllib.request.Request(url,headers={'Accept':'application/json',**({'Authorization':'Bearer '+token} if token else {})})
    try:
        with urllib.request.urlopen(req,timeout=12) as r: return json.loads(r.read(3*1024*1024))
    except urllib.error.HTTPError as e:
        # Never log or return access tokens.
        raise LibraryError('Google Books API HTTP '+str(e.code)) from None
    except (urllib.error.URLError,TimeoutError):raise LibraryError('Không thể kết nối Google Books API') from None

def search_google(q:str, limit:int=12):
    if not 1<=len(q.strip())<=200:raise LibraryError('Từ khóa dài 1-200 ký tự')
    params={'q':q.strip(),'maxResults':min(max(int(limit),1),40)}
    key=os.environ.get('GOOGLE_BOOKS_API_KEY')
    if key:params['key']=key
    return _google_get('volumes',params)

class GoogleSession:
    def __init__(self):self._token=None;self._expires=0;self._flow=None;self._lock=threading.Lock()
    def authorized(self):return bool(self._token and time.time()<self._expires-30)
    def disconnect(self):self._token=None;self._expires=0;self._flow=None
    def token(self):
        if not self.authorized():raise LibraryError('Chưa kết nối Google hoặc phiên đăng nhập hết hạn')
        return self._token
    def shelves(self):return _google_get('mylibrary/bookshelves',{},self.token())
    def uploaded(self,start:int=0,max_results:int=40):
        return _google_get('volumes/useruploaded',{'startIndex':max(0,int(start)),'maxResults':min(max(1,int(max_results)),40)},self.token())
    def uploaded_fallback(self,start:int=0,max_results:int=100):
        return _google_get('volumes/mybooks',{'acquireMethod':'UPLOADED','startIndex':max(0,int(start)),'maxResults':min(max(1,int(max_results)),100)},self.token())
    def begin_oauth(self):
        cid=os.environ.get('GOOGLE_OAUTH_CLIENT_ID','').strip()
        if not cid:raise LibraryError('Thiếu GOOGLE_OAUTH_CLIENT_ID của ứng dụng Desktop OAuth')
        if self._flow:raise LibraryError('Có phiên kết nối đang chờ, hãy thử lại sau')
        state=secrets.token_urlsafe(24);verifier=secrets.token_urlsafe(48)
        challenge=__import__('base64').urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).decode().rstrip('=')
        parent=self
        class Callback(BaseHTTPRequestHandler):
            def log_message(self,*a):pass
            def do_GET(self):
                vals=urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
                if not secrets.compare_digest(vals.get('state',[''])[0],state):
                    self.send_response(400);self.end_headers();self.wfile.write(b'Invalid OAuth state');return
                code=vals.get('code',[''])[0]
                if not code:
                    parent._flow=None;self.send_response(400);self.end_headers();self.wfile.write(b'Google authorization denied');return
                try:
                    body=urllib.parse.urlencode({'client_id':cid,'grant_type':'authorization_code','code':code,'redirect_uri':parent._flow['redirect'],'code_verifier':verifier}).encode()
                    req=urllib.request.Request('https://oauth2.googleapis.com/token',data=body,headers={'Content-Type':'application/x-www-form-urlencoded'})
                    with urllib.request.urlopen(req,timeout=12) as r:payload=json.load(r)
                    parent._token=payload['access_token'];parent._expires=time.time()+int(payload.get('expires_in',3500));parent._flow=None
                    response='Đã kết nối Google Books. Có thể quay về thư viện.'
                    self.send_response(200)
                except Exception:
                    parent._flow=None;response='Không thể hoàn tất OAuth; kiểm tra cấu hình Google Cloud.';self.send_response(400)
                self.send_header('Content-Type','text/plain; charset=utf-8');self.send_header('Cache-Control','no-store');self.end_headers();self.wfile.write(response.encode('utf-8'))
        callback=HTTPServer(('127.0.0.1',0),Callback)
        redirect=f'http://127.0.0.1:{callback.server_port}/'
        self._flow={'state':state,'redirect':redirect}
        threading.Thread(target=callback.handle_request,daemon=True).start()
        params={'client_id':cid,'redirect_uri':redirect,'response_type':'code','scope':'https://www.googleapis.com/auth/books','state':state,'code_challenge':challenge,'code_challenge_method':'S256','access_type':'online'}
        return {'url':'https://accounts.google.com/o/oauth2/v2/auth?'+urllib.parse.urlencode(params),'note':'Mở liên kết trên máy đang chạy Plugin; token chỉ giữ trong RAM, không lưu refresh token.'}

google_session=GoogleSession()
