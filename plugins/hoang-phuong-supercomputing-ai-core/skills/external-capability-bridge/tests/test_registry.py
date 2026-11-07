import json,pathlib,unittest
P=pathlib.Path(__file__).resolve().parents[1]/'references/EXTERNAL_16_CLUSTER_REGISTRY.json'
class RegistryTest(unittest.TestCase):
 def test_invariants(self):
  a=json.loads(P.read_text(encoding='utf-8'));s=a['skills']
  self.assertEqual(181,len(s));self.assertEqual(14,len(a['owned_external_plugins']))
  self.assertEqual(181,len({x['id'] for x in s}))
  self.assertEqual(set(f'{i:02d}' for i in range(1,17)),set(x['primary_cluster'] for x in s)|set(c['id'] for c in a['clusters']))
  self.assertTrue(all(x['source_uri'].startswith('skills://plugins/') and x['integration']=='federated_reference' for x in s))
  self.assertEqual(181,sum(c['external_skill_count'] for c in a['clusters']))
if __name__=='__main__':unittest.main()
