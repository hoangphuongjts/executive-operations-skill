import unittest
import importlib.util
from pathlib import Path
import json
p=Path(__file__).with_name('github500_router.py')
spec=importlib.util.spec_from_file_location('github500_router',p)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
class GitHub500Tests(unittest.TestCase):
    def test_exact_500_unique(self):self.assertEqual(len(mod.load()),500)
    def test_urls_grounded_format(self):self.assertTrue(all(r['github_url']=='https://github.com/'+r['repo'] for r in mod.load()))
    def test_no_auto_install_claim(self):self.assertEqual(sum(r['integration_status']=='adapted_native_skill_guidance' for r in mod.load()),3);self.assertTrue(all(r['integration_status'].startswith(('not_integrated','catalog_link_only','adapted_native_skill_guidance')) for r in mod.load()))
    def test_pilot_count(self):self.assertEqual(mod.report()['pilot'],25)
    def test_license_still_review_only(self):self.assertTrue(all('certified' not in r.get('license_status','') or r['license_status']=='file_located_not_legally_certified' for r in mod.load()))
    def test_search_repo(self):self.assertTrue(any(x['repo']=='n8n-io/n8n' for x in mod.search('n8n')))
    def test_search_area(self):self.assertTrue(all(x['discovery_area']=='12_AGRI' for x in mod.search(area='12_AGRI')))
    def test_empty_search(self):self.assertEqual(mod.search('unlikely_this_repo_token_3992111'),[])
    def test_limit_validation(self):
        with self.assertRaises(ValueError):mod.search(limit=0)
        with self.assertRaises(ValueError):mod.search(limit=101)
    def test_readonly_mode(self):self.assertEqual(mod.report()['external_runtime_executed'],0)
    def test_pilot_licenses_initial(self):
        pilots=json.loads(mod.PILOT.read_text(encoding='utf-8'))['records']
        self.assertEqual(sum(x['license_status']=='file_located_not_legally_certified' for x in pilots),23);self.assertEqual(mod.report()['pilot_license_paths_located'],23)
    def test_108_code_cannot_be_overridden(self):
        self.assertTrue(all(not x['repo'].startswith('/') for x in mod.load()))
if __name__=='__main__':unittest.main()
