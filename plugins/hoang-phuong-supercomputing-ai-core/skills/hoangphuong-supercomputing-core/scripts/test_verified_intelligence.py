"""Offline regression tests for the v13.1 verification harness."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

MODULE_PATH=Path(__file__).with_name('verified_intelligence.py')
spec=importlib.util.spec_from_file_location('verified_intelligence',MODULE_PATH)
core=importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)

def _is_historical_v13_release():
    try:
        versions=[json.loads((core.root_dir()/name).read_text(encoding='utf-8'))['version']
                  for name in ('plugin.json','.codex-plugin/plugin.json')]
        return versions[0]==versions[1] and versions[0].startswith('13.1.')
    except (OSError,KeyError,ValueError,TypeError):
        return False


@unittest.skipUnless(_is_historical_v13_release(), "historical v13.1 harness; active plugin is a later release")
class VerificationTests(unittest.TestCase):
    def test_roles_parser_preserves_order_and_uniqueness(self):
        sample='01. Role A\n02. Role B\n01. Dup\n'
        self.assertEqual(core.parse_roles(sample),[1,2,1])
    def test_percentile_bounds(self):
        self.assertEqual(core.percentile([1,3,5],0),1)
        self.assertEqual(core.percentile([1,3,5],50),3)
        self.assertEqual(core.percentile([1,3,5],100),5)
        with self.assertRaises(ValueError): core.percentile([],99)
    def test_lookup_equivalence_absent_and_present(self):
        sample=list(range(0,40,2))
        for q in range(-1,42):
            self.assertEqual(core.linear_lookup(sample,q),core.binary_lookup(sample,q))
    def test_benchmark_correct_and_bounded(self):
        result=core.benchmark(size=128,iterations=30,seed=22)
        self.assertEqual(result['correctness'],'passed')
        self.assertEqual(len(result['results']),2)
        with self.assertRaises(ValueError): core.benchmark(size=9999999)
    def test_evaluation_detects_wrong_answer(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'cases.jsonl'
            path.write_text('\n'.join(json.dumps(row) for row in [
                {'id':'a','expected':'Yes','actual':'yes','evidence':['doc1']},
                {'id':'b','expected':'yes','actual':'no','evidence':[]}
            ]),encoding='utf8')
            result=core.evaluate(path)
            self.assertEqual(result['exact_match_rate'],.5)
            self.assertEqual(result['evidence_coverage'],.5)
    def test_evaluation_rejects_invalid_dataset(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'bad.jsonl'
            path.write_text('{"id":"1","expected":true,"actual":"x"}',encoding='utf8')
            with self.assertRaises(ValueError):core.evaluate(path)
    def test_utf16_integrity_hash_known(self):
        self.assertEqual(core.fnv_utf16(""),"cbf29ce484222325")
        self.assertEqual(core.fnv_utf16("A"),"0908a207b5a15704")
    def test_verify_fails_on_missing_plugin(self):
        with tempfile.TemporaryDirectory() as tmp:
            result=core.verify(Path(tmp))
            self.assertEqual(result['status'],'failed')
            self.assertGreater(result['total']-result['passed'],0)
    def test_full_plugin_structure_when_available(self):
        root=core.root_dir()
        if not (root/core.ROLES).exists(): self.skipTest('only patch files present; release overlay required')
        result=core.verify(root)
        self.assertEqual(result['status'],'passed',result['checks'])

if __name__=='__main__': unittest.main()
