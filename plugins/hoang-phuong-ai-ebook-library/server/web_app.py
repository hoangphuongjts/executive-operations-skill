"""Loopback-only UI; no public binding or cookies. Same Python interpreter as MCP when invoked by tool."""
from __future__ import annotations
import json,sys,threading,urllib.parse
from email.parser import BytesParser
from email.policy import default
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from library import LibraryError,list_books,find_book,stored_path,import_bytes,save_progress,safe_epub_chapters,search_google,google_session,MAX_BOOK_BYTES
UI=Path(__file__).resolve().parent.parent/'web'/'index.html'

class Handler(BaseHTTPRequestHandler):
 def log_message(self, fmt,*args): pass
 def send_data(self,code:int,payload,content_type='application/json; charset=utf-8'):
  body=json.dumps(payload,ensure_ascii=False).encode() if isinstance(payload,(dict,list)) else payload
  self.send_response(code);self.send_header('Content-Type',content_type);self.send_header('Content-Length',str(len(body)))
  self.send_header('X-Content-Type-Options','nosniff');self.send_header('Cache-Control','no-store');self.send_header('X-Frame-Options','SAMEORIGIN')
  self.send_header('Content-Security-Policy',"default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' https://books.google.com https://books.googleusercontent.com https://*.googleusercontent.com data:; object-src 'self'; frame-src 'self'; base-uri 'none'; form-action 'self'")
  self.end_headers();self.wfile.write(body)
 def _allowed_host(self):
  return self.headers.get('Host','')==f'127.0.0.1:{self.server.server_port}' and self.headers.get('Sec-Fetch-Site','same-origin') in ('same-origin','none')
 def route(self):
  p=urllib.parse.urlparse(self.path);return p.path,urllib.parse.parse_qs(p.query)
 def do_GET(self):
  if not self._allowed_host():return self.send_data(403,{'error':'Host hoặc origin không hợp lệ'})
  path,q=self.route()
  try:
   if path=='/':return self.send_data(200,UI.read_bytes(),'text/html; charset=utf-8')
   if path=='/api/books':return self.send_data(200,{'items':list_books()})
   if path=='/api/google/status':return self.send_data(200,{'connected':google_session.authorized()})
   if path=='/api/google/auth':return self.send_data(200,google_session.begin_oauth())
   if path=='/api/google/search':return self.send_data(200,search_google(q.get('q',[''])[0]))
   if path=='/api/google/uploads':
    try:data=google_session.uploaded()
    except LibraryError as e:
     if 'HTTP 404' not in str(e):raise
     data=google_session.uploaded_fallback()
    return self.send_data(200,data)
   if path=='/api/google/shelves':return self.send_data(200,google_session.shelves())
   if path.startswith('/api/books/'):
    parts=path.split('/')
    if len(parts)!=5:raise LibraryError('Đường dẫn không hợp lệ')
    book=find_book(parts[3]);p=stored_path(book)
    if parts[4]=='chapters':
     if book['kind']!='epub':raise LibraryError('Chỉ EPUB có các chương')
     return self.send_data(200,{'chapters':safe_epub_chapters(p),'progress':book['progress']})
    if parts[4]=='file':
     if book['kind']!='pdf':raise LibraryError('Chỉ PDF có tệp nhúng')
     if p.stat().st_size>MAX_BOOK_BYTES:raise LibraryError('Tệp quá lớn')
     return self.send_data(200,p.read_bytes(),'application/pdf')
   raise LibraryError('Không tìm thấy địa chỉ')
  except LibraryError as e:return self.send_data(400,{'error':str(e)})
 def do_POST(self):
  if not self._allowed_host():return self.send_data(403,{'error':'Host hoặc origin không hợp lệ'})
  origin=self.headers.get('Origin')
  if origin and origin != f'http://127.0.0.1:{self.server.server_port}':return self.send_data(403,{'error':'Origin không hợp lệ'})
  path,_=self.route()
  try:
   if path=='/api/google/disconnect':google_session.disconnect();return self.send_data(200,{'connected':False})
   limit=MAX_BOOK_BYTES+1024*1024
   size=int(self.headers.get('Content-Length','0'))
   if size<=0 or size>limit:raise LibraryError('Kích thước yêu cầu không hợp lệ')
   data=self.rfile.read(size)
   if path=='/api/import':
    ct=self.headers.get('Content-Type','')
    if not ct.startswith('multipart/form-data;'):raise LibraryError('Cần multipart/form-data')
    msg=BytesParser(policy=default).parsebytes(('Content-Type: '+ct+'\r\nMIME-Version: 1.0\r\n\r\n').encode()+data)
    part=next((p for p in msg.iter_parts() if p.get_param('name',header='content-disposition')=='file'),None)
    if part is None:raise LibraryError('Thiếu tệp')
    name=part.get_filename() or 'ebook'
    return self.send_data(200,import_bytes(part.get_payload(decode=True),name))
   if path.startswith('/api/books/') and path.endswith('/progress'):
    id=path.split('/')[3]
    value=json.loads(data)
    return self.send_data(200,save_progress(id,int(value['progress'])))
   raise LibraryError('Không tìm thấy địa chỉ')
  except (LibraryError,ValueError,TypeError,KeyError) as e:return self.send_data(400,{'error':str(e)})

def start_http(port=8765):
 server=ThreadingHTTPServer(('127.0.0.1',port),Handler)
 threading.Thread(target=server.serve_forever,daemon=True).start()
 return server

if __name__=='__main__':
 server=start_http();print('HOÀNG PHƯƠNG EBOOK READER: http://127.0.0.1:%d/'%server.server_port)
 try:threading.Event().wait()
 except KeyboardInterrupt:server.shutdown()
