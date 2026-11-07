"""Tests for v14.6 Skill adoption and offline integrity tool, no network."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[3]
CORE=ROOT/'skills/hoangphuong-supercomputing-core'
FILE=CORE/'scripts/github500_integrity.py'
spec=importlib.util.spec_from_file_location('github500_integrity',FILE)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class Pilots(unittest.TestCase):
    def test_skills_exist(self):
        for n in ('github500-ab-testing','github500-experimental-design','github500-agent-supply-chain'):
            p=ROOT/f'skills/{n}/SKILL.md'
            s=p.read_text()
            self.assertTrue(s.startswith('---\nname: '+n+'\n'))
            self.assertIn('description:',s.split('---',2)[1])
            self.assertTrue((p.parent/'references/PROVENANCE.md').is_file())
    def test_pilot_registry(self):
        x=json.loads((CORE/'references/GITHUB_500_PILOT_INTEGRATIONS.json').read_text())
        self.assertEqual(x['pilot_total'],25)
        self.assertEqual(x['license_file_located'],23)
        self.assertEqual(x['full_repo_security_audits_complete'],0)
        self.assertEqual(len(x['integrations']),3)
        self.assertEqual(len(set(y['native_path'] for y in x['integrations'])),3)
    def test_main_catalog_retained(self):
        x=json.loads((CORE/'references/GITHUB_500_MASTER_CATALOG.json').read_text())
        self.assertEqual(len(x['records']),500)
        self.assertEqual(len({r['repo'].lower() for r in x['records']}),500)
    def test_embedded_mode_retained(self):
        x=json.loads((CORE/'references/EMBEDDED_128_MODE.json').read_text())
        self.assertEqual(x['mode'],'embedded_skills_only')
        self.assertFalse(x['external_model_api_default'])
    def test_original_registry_retained(self):
        x=json.loads((CORE/'references/AGENTS_128.json').read_text())
        self.assertEqual(len(x['roles']),128)
    def test_prompts_not_overwritten(self):
        for n in ('github500-ab-testing','github500-experimental-design','github500-agent-supply-chain'):
            self.assertNotIn('/generate', (ROOT/f'skills/{n}/SKILL.md').read_text())
    def test_manifest_bump(self):
        versions=[json.loads((ROOT/name).read_text())['version'] for name in ('plugin.json','.codex-plugin/plugin.json')]
        self.assertEqual(versions[0],versions[1])
        self.assertGreaterEqual(tuple(map(int,versions[0].split('.'))),(14,7,0))

class Integrity(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory()
        self.root=Path(self.t.name)
        (self.root/'x').mkdir()
        (self.root/'x/a.txt').write_text('abc')
        self.base=mod.snapshot(self.root)
    def tearDown(self):self.t.cleanup()
    def test_sha256_snapshot(self):
        self.assertEqual(self.base['file_count'],1)
        self.assertEqual(len(self.base['files']['x/a.txt']),64)
    def test_verify_untouched(self):
        self.assertTrue(mod.verify(self.root,self.base)['passed'])
    def test_detect_modified(self):
        (self.root/'x/a.txt').write_text('modified')
        self.assertEqual(mod.verify(self.root,self.base)['errors']['modified'],['x/a.txt'])
    def test_detect_added(self):
        (self.root/'new.txt').write_text('new')
        self.assertEqual(mod.verify(self.root,self.base)['errors']['added'],['new.txt'])
    def test_detect_missing(self):
        (self.root/'x/a.txt').unlink()
        self.assertEqual(mod.verify(self.root,self.base)['errors']['missing'],['x/a.txt'])
    def test_tampered_digest_rejected(self):
        self.base['manifest_digest']='0'*64
        with self.assertRaises(ValueError):mod.verify(self.root,self.base)
    def test_manifest_path_traversal_rejected(self):
        self.base['files']={'../secret':'0'*64}
        self.base['file_count']=1
        with self.assertRaises(ValueError):mod.verify(self.root,self.base)
    def test_symlink_rejected(self):
        try:(self.root/'evil').symlink_to(self.root/'x/a.txt')
        except (OSError,NotImplementedError):self.skipTest('symlink unavailable')
        with self.assertRaises(ValueError):mod.snapshot(self.root)
    def test_excludes_cache(self):
        (self.root/'.git').mkdir()
        (self.root/'.git/config').write_text('secret')
        self.assertEqual(mod.snapshot(self.root)['file_count'],1)

if __name__=='__main__':unittest.main()
