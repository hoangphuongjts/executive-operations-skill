import io, pathlib, tempfile, unittest, zipfile
from source.quarantine_download import archive_url,download

def zipdata(members):
    buf=io.BytesIO()
    with zipfile.ZipFile(buf,'w') as z:
        for name,data in members.items():z.writestr(name,data)
    return buf.getvalue()
class Reply:
    def __init__(self,data):self.stream=io.BytesIO(data)
    def __enter__(self):return self
    def __exit__(self,*a):return False
    def read(self,n):return self.stream.read(n)
    def geturl(self):return 'https://codeload.github.com/owner/repo/zip/abc'
class TestDownload(unittest.TestCase):
    def setUp(self):self.sha='a'*40;self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.path=pathlib.Path(self.temp.name)/'quarantine.zip'
    def test_url(self):self.assertEqual(archive_url('owner/repo',self.sha),'https://api.github.com/repos/owner/repo/zipball/'+self.sha)
    def test_bad_repo(self):
        for repo in ['../repo','a/b/extra','https://evil/a','a/../x']:
            with self.assertRaises(ValueError):archive_url(repo,self.sha)
    def test_bad_sha(self):
        with self.assertRaises(ValueError):archive_url('owner/repo','main')
    def test_quarantines_zip(self):
        blob=zipdata({'repo/README.md':'hello'})
        result=download('owner/repo',self.sha,self.path,opener=lambda *args,**kwargs:Reply(blob))
        self.assertTrue(self.path.exists());self.assertEqual(result['status'],'QUARANTINED_UNTRUSTED_NOT_INSTALLED')
    def test_no_overwrite(self):
        self.path.write_text('existing')
        with self.assertRaises(FileExistsError):download('owner/repo',self.sha,self.path)
    def test_zip_traversal(self):
        with self.assertRaises(ValueError):download('owner/repo',self.sha,self.path,opener=lambda *a,**kw:Reply(zipdata({'../escape.txt':'bad'})))
        self.assertFalse(self.path.exists())
    def test_nonzip(self):
        with self.assertRaises(ValueError):download('owner/repo',self.sha,self.path,opener=lambda *a,**kw:Reply(b'<html>bad</html>'))
        self.assertFalse(self.path.exists())
    def test_size_limit(self):
        blob=zipdata({'repo/x':'123456789'})
        with self.assertRaises(ValueError):download('owner/repo',self.sha,self.path,opener=lambda *a,**kw:Reply(blob),limit=30)
        self.assertFalse(self.path.exists())
    def test_bad_redirect(self):
        class Bad(Reply):
            def geturl(self):return 'https://evil.example/archive.zip'
        with self.assertRaises(ValueError):download('owner/repo',self.sha,self.path,opener=lambda *a,**kw:Bad(zipdata({'a':'b'})))
