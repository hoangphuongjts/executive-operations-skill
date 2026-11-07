"""MCP stdio server, minimal JSON-RPC 2.0 implementation for portable local clients."""
import json,sys,threading
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from library import LibraryError,list_books,import_from_path,save_progress,search_google,google_session,IMPORT_DIR

TOOLS=[
 {'name':'ebook_status','description':'Kiểm tra thư viện local, trạng thái Google OAuth và thư mục nhập sách.', 'inputSchema':{'type':'object','properties':{}}},
 {'name':'ebook_local_list','description':'Liệt kê ebook EPUB/PDF cá nhân đã nhập.', 'inputSchema':{'type':'object','properties':{}}},
 {'name':'ebook_google_search','description':'Tìm Google Books công khai theo tiêu đề/tác giả.', 'inputSchema':{'type':'object','properties':{'query':{'type':'string','minLength':1,'maxLength':200}},'required':['query']}},
 {'name':'ebook_google_auth_start','description':'Tạo URL OAuth Google; người dùng tự mở và cấp quyền.', 'inputSchema':{'type':'object','properties':{}}},
 {'name':'ebook_google_uploads','description':'Liệt kê metadata sách đã upload lên Play Sách qua API có xác thực.', 'inputSchema':{'type':'object','properties':{'start_index':{'type':'integer','minimum':0}}}},
 {'name':'ebook_google_shelves','description':'Liệt kê bookshelf riêng tư đã được Google cấp quyền.', 'inputSchema':{'type':'object','properties':{}}},
 {'name':'ebook_google_disconnect','description':'Ngắt phiên OAuth Google hiện tại.', 'inputSchema':{'type':'object','properties':{}}},
 {'name':'ebook_import_local','description':'Nhập ebook từ thư mục an toàn, không ghi lên Google.', 'inputSchema':{'type':'object','properties':{'path':{'type':'string'}},'required':['path']}},
 {'name':'ebook_save_progress','description':'Cập nhật % đã đọc của ebook cá nhân.', 'inputSchema':{'type':'object','properties':{'book_id':{'type':'string'},'progress':{'type':'integer','minimum':0,'maximum':100}},'required':['book_id','progress']}},
 {'name':'ebook_reader_start','description':'Khởi chạy giao diện đọc trên 127.0.0.1.', 'inputSchema':{'type':'object','properties':{}}},
]
_server=None

def dispatch(name,args):
 global _server
 if name=='ebook_status':return {'google_connected':google_session.authorized(),'import_directory':str(IMPORT_DIR),'local_books':len(list_books()),'uploads_api':'unverified_for_account'}
 if name=='ebook_local_list':return {'items':list_books()}
 if name=='ebook_google_search':return search_google(args['query'])
 if name=='ebook_google_auth_start':return google_session.begin_oauth()
 if name=='ebook_google_uploads':
  try:return {'source':'volumes/useruploaded','data':google_session.uploaded(args.get('start_index',0))}
  except LibraryError as e:
   if 'HTTP 404' not in str(e):raise
   return {'source':'volumes/mybooks?acquireMethod=UPLOADED','data':google_session.uploaded_fallback(args.get('start_index',0))}
 if name=='ebook_google_shelves':return google_session.shelves()
 if name=='ebook_google_disconnect':google_session.disconnect();return {'connected':False}
 if name=='ebook_import_local':return import_from_path(args['path'])
 if name=='ebook_save_progress':return save_progress(args['book_id'],int(args['progress']))
 if name=='ebook_reader_start':
  if _server is None:
   from web_app import start_http
   _server=start_http(port=0)
  return {'url':f'http://127.0.0.1:{_server.server_port}/','note':'Web UI chỉ hoạt động trên máy chạy MCP server'}
 raise LibraryError('Tool không hỗ trợ')

def handle(req):
 method=req.get('method'); id=req.get('id')
 if method=='notifications/initialized' or (id is None):return None
 if method=='initialize':return {'jsonrpc':'2.0','id':id,'result':{'protocolVersion':'2025-03-26','capabilities':{'tools':{}},'serverInfo':{'name':'hp-ebook-library','version':'1.0.0'}}}
 if method=='ping':return {'jsonrpc':'2.0','id':id,'result':{}}
 if method=='tools/list':return {'jsonrpc':'2.0','id':id,'result':{'tools':TOOLS}}
 if method=='tools/call':
  p=req.get('params',{});name=p.get('name');args=p.get('arguments') or {}
  try:
   value=dispatch(name,args)
   return {'jsonrpc':'2.0','id':id,'result':{'content':[{'type':'text','text':json.dumps(value,ensure_ascii=False)}]}}
  except (LibraryError,KeyError,ValueError,TypeError) as e:
   return {'jsonrpc':'2.0','id':id,'result':{'isError':True,'content':[{'type':'text','text':str(e)}]}}
 return {'jsonrpc':'2.0','id':id,'error':{'code':-32601,'message':'Method not found'}}

if __name__=='__main__':
 from web_app import start_http
 for raw in sys.stdin:
  try:
   message=json.loads(raw)
   result=handle(message)
   if result is not None:
    sys.stdout.write(json.dumps(result,ensure_ascii=False)+'\n');sys.stdout.flush()
  except Exception as e:print('Protocol error:',type(e).__name__,file=sys.stderr)
