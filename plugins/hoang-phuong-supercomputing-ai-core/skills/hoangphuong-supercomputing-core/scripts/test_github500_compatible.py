"""Offline tests for GitHub500 compatible skill routing, provenance and preservation."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[3]
SCRIPT=ROOT/'skills/hoangphuong-supercomputing-core/scripts/github500_compatible.py'
spec=importlib.util.spec_from_file_location('github500_compatible', SCRIPT)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class TestV147(unittest.TestCase):
    def test_registry(self):self.assertTrue(mod.validate()['passed'],mod.validate()['issues'])
    def test_count(self):self.assertEqual(mod.validate()['skill_count'],12)
    def test_stable_catalog(self):self.assertEqual(mod.validate()['catalog_count'],500)
    def test_manifest(self):
        for p in ('plugin.json','.codex-plugin/plugin.json'):
            versions=[json.loads((ROOT/name).read_text())['version'] for name in ('plugin.json','.codex-plugin/plugin.json')]
            self.assertEqual(versions[0],versions[1])
            self.assertGreaterEqual(tuple(map(int,versions[0].split('.'))),(14,7,0))
    def test_old_skills_remain(self):
        names=['hoangphuong','phattrienungdung','sanxuatnoidung','marketingtongluc','trolydieuhanh','tudonghethong','phantichdautu']
        for n in names:self.assertTrue((ROOT/f'skills/{n}/SKILL.md').exists(),n)
    def test_old_integrated_skills_remain(self):
        for n in ['github500-ab-testing','github500-experimental-design','github500-agent-supply-chain','github500-research']:
            self.assertTrue((ROOT/f'skills/{n}/SKILL.md').exists(),n)
    def test_mode(self):
        d=json.loads((ROOT/'skills/hoangphuong-supercomputing-core/references/EMBEDDED_128_MODE.json').read_text())
        self.assertEqual(d['mode'],'embedded_skills_only')
        self.assertFalse(d['external_model_api_default']);self.assertFalse(d['runtime_execution_default'])
    def test_research_route(self):self.assertEqual(mod.route('Xây dựng giả thuyết khoa học')['skill'],'github500-hypothesis-research')
    def test_security_route(self):self.assertEqual(mod.route('Kiểm soát quyền agent')['skill'],'github500-agent-governance')
    def test_automation_route(self):self.assertEqual(mod.route('tự động hóa n8n')['skill'],'github500-workflow-design')
    def test_slash(self):
        r=mod.route('/gh500-find')
        self.assertEqual(r['skill'],'github500-command-library')
        self.assertFalse(r['host_slash_command_registered'])
    def test_unknown(self):self.assertIsNone(mod.route('một truy vấn không có từ khóa')['skill'])
    def test_tampered_name_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            reg={'entries':[{'name':'../../oops','skill_path':'skills/../../oops/SKILL.md','source_sha1':'0'*40,'license':'MIT'}],
                 'execution_mode':'embedded_skills_only','safety':{'auto_run_external_repos':False,'auto_register_slash_commands':False,'external_api_calls':False,'original_108_code_names_changed':False,'original_core_agent_ids_changed':False}}
            (p/'skills/hoangphuong-supercomputing-core/references').mkdir(parents=True)
            (p/'skills/hoangphuong-supercomputing-core/references/GITHUB_500_V147_COMPATIBLE_SKILLS.json').write_text(json.dumps(reg))
            (p/'skills/hoangphuong-supercomputing-core/references/AGENTS_128.json').write_text(json.dumps({'roles':[None]*128}))
            (p/'skills/hoangphuong-supercomputing-core/references/GITHUB_500_MASTER_CATALOG.json').write_text(json.dumps({'records':[None]*500}))
            self.assertIn('bad_name:../../oops',mod.validate(p)['issues'])
    def test_unsafe_flag_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            (p/'skills/hoangphuong-supercomputing-core/references').mkdir(parents=True)
            reg=json.loads(mod.REGISTRY.read_text())
            reg['safety']['auto_run_external_repos']=True
            (p/'skills/hoangphuong-supercomputing-core/references/GITHUB_500_V147_COMPATIBLE_SKILLS.json').write_text(json.dumps(reg))
            (p/'skills/hoangphuong-supercomputing-core/references/AGENTS_128.json').write_text(json.dumps({'roles':[None]*128}))
            (p/'skills/hoangphuong-supercomputing-core/references/GITHUB_500_MASTER_CATALOG.json').write_text(json.dumps({'records':[None]*500}))
            self.assertIn('unsafe_flag:auto_run_external_repos',mod.validate(p)['issues'])

if __name__=='__main__':unittest.main()
