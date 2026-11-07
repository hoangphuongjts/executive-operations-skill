"""Isolated tests for v14.8..v15.1 delta, stdlib unittest, offline."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent

def import_from(name):
    spec=importlib.util.spec_from_file_location(name,HERE/(name+'.py'))
    mod=importlib.util.module_from_spec(spec)
    import sys
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod

core=import_from('core_v151')
runtime=import_from('runtime_v150')
hub=import_from('capability_hub_v151')

class TestV151(unittest.TestCase):
    def test_route_accented_and_unaccented(self):
        self.assertEqual(core.route('Tôi muốn thiết kế kiến trúc phần mềm')['skill'],'github500-architecture-blueprint')
        self.assertEqual(core.route('thiet ke kien truc phan mem')['skill'],'github500-architecture-blueprint')
    def test_route_abstains_unknown(self):
        self.assertEqual(core.route('Bài thơ về lá cây')['status'],'abstained')
    def test_route_no_slash_override(self):
        self.assertEqual(core.route('/generatehandwrittenimage tạo ảnh')['status'],'study_command')
    def test_study_exact_registry_loaded(self):
        h=core.study_baseline_health()
        self.assertEqual(h['status'],'passed')
        self.assertEqual(h['codes'],108)
        self.assertIn('trang ghi chép viết tay',core.route('/generatehandwrittenimage tạo ảnh')['original_function'])
    def test_study_unknown_slash_not_invented(self):
        self.assertEqual(core.route('/nonexistent-study-command')['status'],'reserved_study_command')
    def test_route_gh500_alias_no_host_registration(self):
        a=core.route('/gh500-find');self.assertEqual(a['skill'],'github500-command-library');self.assertEqual(a['execution'],'instruction_only')
    def test_multi_intent_review(self):
        self.assertIn(core.route('kiểm thử AI rồi phân quyền agent')['status'],('ambiguous','selected'))
    def test_gate_no_host_no_execution(self):
        self.assertEqual(core.action_gate('send','gmail')['decision'],'plan_only')
    def test_gate_requires_approval(self):
        self.assertEqual(core.action_gate('publish','channel',host_tool_available=True)['decision'],'approval_required')
    def test_gate_explicit_approval_not_actual_execution(self):
        self.assertEqual(core.action_gate('publish','channel',True,True,True)['decision'],'permitted_by_policy_only')
    def test_gate_default_budget(self):
        self.assertEqual(core.action_gate('purchase','store',True,True,True,1,0)['decision'],'deny')
    def test_codes_fail_closed(self):
        self.assertEqual(core.verify_study_codes(None,None)['status'],'blocked')
    def test_codes_protect_full_pair(self):
        with tempfile.TemporaryDirectory() as d:
            a=Path(d)/'original.json';b=Path(d)/'candidate.json'
            v=[{'code':f'/study{i:03}', 'function':f'Function {i}'} for i in range(108)]
            a.write_text(json.dumps(v));b.write_text(json.dumps(v))
            self.assertEqual(core.verify_study_codes(a,b)['verified'],108)
            v[2]['function']='changed';b.write_text(json.dumps(v))
            self.assertEqual(core.verify_study_codes(a,b)['status'],'failed')
    def test_runtime_defaults_disabled(self):
        self.assertEqual(runtime.pilot_plan([9,17,25,32])['status'],'disabled_by_kill_switch')
    def test_runtime_rejects_invalid_ids(self):
        self.assertEqual(runtime.pilot_plan([9,9,25,32])['status'],'rejected')
    def test_runtime_never_executed_even_with_config(self):
        c=runtime.PilotConfig(enabled=True,external_execution_allowed=True,kill_switch=False,max_cost_usd=1.0)
        r=runtime.pilot_plan([9,17,25,32],c,approved=True,model_endpoint='https://example.invalid/v1')
        self.assertEqual(r['status'],'ready_for_separate_runtime_integration_not_executed')
        self.assertEqual(r['model_calls_executed'],0)
    def test_federation_requires_real_tool_presence(self):
        self.assertEqual(hub.resolve({'tool_name':'mock.email.send'},set())['status'],'external_tool_unavailable')
    def test_federation_requires_write_consent(self):
        self.assertEqual(hub.resolve({'tool_name':'mock.email.send'},{'mock.email.send'},'send')['status'],'approval_required')
    def test_federation_never_actually_calls_tool(self):
        self.assertEqual(hub.resolve({'tool_name':'mock.email.send'},{'mock.email.send'},'send',True,True)['execution'],'not_executed')
    def test_catalog_500_not_executed_claim(self):
        self.assertEqual(core.plan('tự động hóa n8n')['execution'],'not_executed')
    def test_delta_manifest_detects_tamper(self):
        import hashlib
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            ref=root/'skills/hoangphuong-supercomputing-core/references';ref.mkdir(parents=True)
            target=root/'data.txt';target.write_text('ok')
            (ref/'V151_DELTA_SHA256.json').write_text(json.dumps({'files':{'data.txt':hashlib.sha256(b'ok').hexdigest()}}))
            self.assertEqual(core.verify_delta_manifest(root)['status'],'passed')
            target.write_text('tampered')
            self.assertEqual(core.verify_delta_manifest(root)['status'],'failed')
    def test_plan_reports_matched_current_release(self):
        manifests=[json.loads((core.ROOT/name).read_text(encoding='utf-8')) for name in ('plugin.json','.codex-plugin/plugin.json')]
        self.assertEqual(manifests[0]['version'],manifests[1]['version'])
        self.assertEqual(core.current_release_version(),manifests[0]['version'])
        self.assertEqual(core.plan('kiến trúc phần mềm')['version'],manifests[0]['version'])

    def test_doctor_on_complete_fixture(self):
        import shutil
        with tempfile.TemporaryDirectory() as d:
            r=Path(d)
            original=HERE.parents[2]
            for source in ('plugin.json','.codex-plugin/plugin.json'):
                f=r/source;f.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(original/source,f)
            for name in core.SKILLS:
                f=r/'skills'/name/'SKILL.md';f.parent.mkdir(parents=True,exist_ok=True);f.write_text('---\nname: test\n---\n')
            for name in core.SKILL_RULES:
                f=r/'skills'/name/'SKILL.md';f.parent.mkdir(parents=True,exist_ok=True);f.write_text('---\nname: test\n---\n')
            refs=r/core.CORE/'references';refs.mkdir(parents=True)
            for name in ('CAPABILITY_MATRIX.json','STUDY_108_BASELINE.json','STUDY_108_PROVENANCE.json'):
                shutil.copy2(original/core.CORE/'references'/name,refs/name)
            (refs/'AGENTS_128.json').write_text(json.dumps({'roles':[{'id':i,'group':(i-1)//8+1} for i in range(1,129)]}))
            (refs/'GITHUB_500_MASTER_CATALOG.json').write_text(json.dumps({'records':[{'repo':f'owner/repo{i}'} for i in range(500)]}))
            report=core.doctor(r)
            self.assertEqual(report['status'],'passed',report)
            self.assertEqual(report['evidence']['study_codes'],108)
            (r/'skills/hoangphuong/SKILL.md').unlink()
            self.assertEqual(core.doctor(r)['status'],'failed')
    def test_compound_200_route_smoke(self):
        # Regression coverage, not an independently labeled benchmark.
        templates=('Lập giải pháp cho {x}','Phân tích cách làm {x}','Tư vấn {x}','Cho mình tài liệu {x}')
        keywords=('kiến trúc phần mềm','benchmark','prompt injection','citation','workflow','gia thuyet','cad','ab test','doi thu','supply chain')
        results=[core.route(t.format(x=k)) for t in templates for k in keywords for _ in range(5)]
        self.assertEqual(len(results),200)
        self.assertTrue(all(r['status'] in ('selected','ambiguous','needs_review') for r in results))

if __name__=='__main__':unittest.main()
