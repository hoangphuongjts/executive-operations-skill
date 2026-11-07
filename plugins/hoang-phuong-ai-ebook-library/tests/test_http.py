import io,json,sys,tempfile,unittest,urllib.request,urllib.error
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'server'))
from web_app import start_http
from library import import_bytes,list_books

class HTTPTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.server=start_http(port=0);cls.root='http://127.0.0.1:'+str(cls.server.server_port)
 @classmethod
 def tearDownClass(cls):cls.server.shutdown();cls.server.server_close()
 def fetch(self,path):
  with urllib.request.urlopen(self.root+path,timeout=4) as r:return r.status,r.headers,r.read()
 def test_home_and_local_api(self):
  status,headers,data=self.fetch('/')
  self.assertEqual(status,200);self.assertIn(b'HO\xc3\x80NG PH\xc6\xaf\xc6\xa0NG',data)
  self.assertIn('no-store',headers['Cache-Control'])
  status,_,data=self.fetch('/api/books');self.assertEqual(status,200);self.assertIn('items',json.loads(data))
 def test_reject_wrong_host(self):
  req=urllib.request.Request(self.root+'/',headers={'Host':'evil.test'})
  with self.assertRaises(urllib.error.HTTPError) as e:urllib.request.urlopen(req,timeout=4)
  self.assertEqual(e.exception.code,403)
 def test_reject_cross_origin_post(self):
  req=urllib.request.Request(self.root+'/api/google/disconnect',data=b'',headers={'Origin':'https://evil.test'},method='POST')
  with self.assertRaises(urllib.error.HTTPError) as e:urllib.request.urlopen(req,timeout=4)
  self.assertEqual(e.exception.code,403)
 def test_uploaded_requires_auth(self):
  with self.assertRaises(urllib.error.HTTPError) as e:urllib.request.urlopen(self.root+'/api/google/uploads',timeout=4)
  self.assertEqual(e.exception.code,400)
