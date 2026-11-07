import io, json, os, subprocess, sys, tempfile, unittest, zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TEMP=tempfile.TemporaryDirectory();os.environ['HP_EBOOK_HOME']=TEMP.name
os.environ['EBOOK_IMPORT_DIR']=str(Path(TEMP.name)/'imports')
sys.path.insert(0,str(ROOT/'server'))
import library as lib
import mcp_server

def fixture_epub():
 b=io.BytesIO()
 with zipfile.ZipFile(b,'w') as z:
  z.writestr('mimetype','application/epub+zip')
  z.writestr('META-INF/container.xml','<container xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf"/></rootfiles></container>')
  z.writestr('OEBPS/content.opf','<package xmlns="http://www.idpf.org/2007/opf"><manifest><item id="one" href="ch1.xhtml" media-type="application/xhtml+xml"/></manifest><spine><itemref idref="one"/></spine></package>')
  z.writestr('OEBPS/ch1.xhtml','<html><body><h1>Chương 1</h1><p>Nội dung an toàn.</p><script>STEAL_TOKEN()</script></body></html>')
 return b.getvalue()
class Tests(unittest.TestCase):
 def test_import_epub_extracts_without_script(self):
  r=lib.import_bytes(fixture_epub(),'quyen sach.epub');self.assertFalse(r['duplicate'])
  chapters=lib.safe_epub_chapters(lib.stored_path(r['book']))
  self.assertIn('Nội dung an toàn',chapters[0]['text']);self.assertNotIn('STEAL_TOKEN',chapters[0]['text'])
  self.assertTrue(lib.import_bytes(fixture_epub(),'other.epub')['duplicate'])
 def test_invalid_pdf_blocked(self):
  with self.assertRaises(lib.LibraryError):lib.import_bytes(b'NOT PDF','x.pdf')
 def test_safe_import_directory_enforced(self):
  path=Path(TEMP.name)/'outside.pdf';path.write_bytes(b'%PDF-1.7\n')
  with self.assertRaises(lib.LibraryError):lib.import_from_path(str(path))
 def test_progress_validations(self):
  r=lib.import_bytes(b'%PDF-1.7\n','example.pdf');self.assertEqual(lib.save_progress(r['book']['id'],40)['progress'],40)
  with self.assertRaises(lib.LibraryError):lib.save_progress(r['book']['id'],101)
 def test_oauth_without_client_fails(self):
  old=os.environ.pop('GOOGLE_OAUTH_CLIENT_ID',None)
  with self.assertRaises(lib.LibraryError):lib.google_session.begin_oauth()
  if old:os.environ['GOOGLE_OAUTH_CLIENT_ID']=old
 def test_mcp_tools_schema_and_status(self):
  x=mcp_server.handle({'jsonrpc':'2.0','id':1,'method':'tools/list'});self.assertEqual(len(x['result']['tools']),10)
  s=mcp_server.handle({'jsonrpc':'2.0','id':2,'method':'tools/call','params':{'name':'ebook_status'}})
  self.assertEqual(s['result']['content'][0]['type'],'text')
 def test_google_upload_metadata_requires_oauth(self):
  lib.google_session.disconnect()
  with self.assertRaises(lib.LibraryError):lib.google_session.uploaded()
if __name__=='__main__':unittest.main()

# Imported by unittest discovery from class below; no remote requests.
class ApiTests(unittest.TestCase):
 def test_google_uploads_endpoint_and_filter(self):
  from unittest.mock import patch
  lib.google_session._token='unit-test-token';lib.google_session._expires=__import__('time').time()+3600
  try:
   with patch.object(lib,'_google_get',return_value={'items':[{'id':'sample'}]}) as call:
    lib.google_session.uploaded(10);self.assertEqual(call.call_args.args[0],'volumes/useruploaded')
    lib.google_session.uploaded_fallback(10);self.assertEqual(call.call_args.args[0],'volumes/mybooks')
    self.assertEqual(call.call_args.args[1]['acquireMethod'],'UPLOADED')
  finally:lib.google_session.disconnect()
 def test_google_search_validates(self):
  with self.assertRaises(lib.LibraryError):lib.search_google('')
