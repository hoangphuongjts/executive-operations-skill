import unittest,tempfile,wave,array,copy
from pathlib import Path
from voice_select import evaluate
class TestSelection(unittest.TestCase):
 def fixture(self,d):
  p=Path(d)
  for name,value in [('clean',1000),('clip',32767)]:
   with wave.open(str(p/(name+'.wav')),'wb') as w:w.setnchannels(1);w.setsampwidth(2);w.setframerate(16000);w.writeframes(array.array('h',[value,-value]*8000).tobytes())
  c={'id':'A','file':'clean.wav','rights_verified':True,'script_sha256':'abc','listening_review':{'reviewer':'test fixture, not actual perception','full_listen':True,'critical_errors':False,'scores':dict.fromkeys(['accuracy','naturalness','identity','prosody','cleanliness'],4)}}
  return {'script_sha256':'abc','candidates':[c]}
 def test_missing_listen_abstains(self):
  with tempfile.TemporaryDirectory() as d:
   x=self.fixture(d);x['candidates'][0].pop('listening_review');self.assertIsNone(evaluate(x,Path(d))['recommended_candidate'])
 def test_clip_excluded(self):
  with tempfile.TemporaryDirectory() as d:
   x=self.fixture(d);c=copy.deepcopy(x['candidates'][0]);c.update(id='B',file='clip.wav');x['candidates'].append(c);r=evaluate(x,Path(d));self.assertEqual(r['recommended_candidate'],'A');self.assertIn('possible_clipping',r['results'][1]['issues'])
 def test_wrong_script_excluded(self):
  with tempfile.TemporaryDirectory() as d:
   x=self.fixture(d);x['candidates'][0]['script_sha256']='other';self.assertIsNone(evaluate(x,Path(d))['recommended_candidate'])
 def test_clone_consent_required(self):
  with tempfile.TemporaryDirectory() as d:
   x=self.fixture(d);x['candidates'][0]['is_clone']=True;self.assertIsNone(evaluate(x,Path(d))['recommended_candidate'])
 def test_tie_abstains(self):
  with tempfile.TemporaryDirectory() as d:
   x=self.fixture(d);c=copy.deepcopy(x['candidates'][0]);c['id']='B';x['candidates'].append(c);self.assertIsNone(evaluate(x,Path(d))['recommended_candidate'])
if __name__=='__main__':unittest.main()
