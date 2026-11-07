import unittest,tempfile,argparse
from pathlib import Path
import free_voiceover as f
class Tests(unittest.TestCase):
 def args(self,root,**kw):
  p=Path(root)/'text.txt';p.write_text('Xin chào',encoding='utf-8');a=dict(doctor=False,text=str(p),output=str(Path(root)/'out.wav'),reference=None,voice=None,consent=False,allow_model_download=True,engine='vieneu');a.update(kw);return argparse.Namespace(**a)
 def test_no_consent_blocks_clone(self):
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaisesRegex(ValueError,'quyền'):f.validate(self.args(d,reference='sample.wav'))
 def test_download_gate(self):
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaisesRegex(ValueError,'cho phép'):f.validate(self.args(d,allow_model_download=False))
 def test_no_overwrite(self):
  with tempfile.TemporaryDirectory() as d:
   a=self.args(d);Path(a.output).write_bytes(b'old')
   with self.assertRaisesRegex(ValueError,'ghi đè'):f.validate(a)
 def test_accept_script(self):
  with tempfile.TemporaryDirectory() as d:f.validate(self.args(d))
 def test_engine_voice_mismatch(self):
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaisesRegex(ValueError,'preset'):f.validate(self.args(d,engine='voxcpm',voice='Adam'))
if __name__=='__main__':unittest.main()
