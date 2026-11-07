"""No paid API calls or network are used by this test suite."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

path=Path(__file__).with_name('swarm128.py')
spec=importlib.util.spec_from_file_location('swarm128',path)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class RegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root=path.resolve().parents[3]
        cls.registry=m.load_registry(cls.root)

    def test_128_consecutive_ids(self):
        self.assertEqual([r['id'] for r in self.registry['roles']],list(range(1,129)))

    def test_names_unique(self):
        self.assertEqual(len(set(r['name'].casefold() for r in self.registry['roles'])),128)

    def test_sixteen_groups_of_eight(self):
        self.assertEqual([sum(r['group']==g for r in self.registry['roles']) for g in range(1,17)],[8]*16)

    def test_preserves_original_64(self):
        self.assertEqual(m.validate(self.root)['status'],'pass')

    def test_chosen_roles_bounded_and_core_present(self):
        out=m.route('Dựng video khoa học trên YouTube có phụ đề',self.registry,6)
        self.assertEqual(len(out),6)
        self.assertTrue({32,57,64}.issubset({r['id'] for r in out}))

    def test_new_roles_are_reachable(self):
        tasks=['Xây website UX khách hàng','Xây hệ thống RAG vector dữ liệu','Agent runtime với quota token','Kiểm tra SBOM secret bảo mật','Lồng giọng đọc phụ đề video','Dự báo dòng tiền tài chính','Thiết kế CAD in 3D STL','benchmark độ trễ p99']
        for task in tasks:
            out=m.route(task,self.registry,8)
            self.assertTrue(any(r['id']>=65 for r in out),task)

    def test_deterministic_selector(self):
        t='thiết kế 3D CAD cho STL'
        self.assertEqual([r['id'] for r in m.route(t,self.registry)],[r['id'] for r in m.route(t,self.registry)])

    def test_reject_overly_long_user_task(self):
        with self.assertRaises(ValueError):m.route('x'*6001,self.registry)

    def test_reject_too_many_roles(self):
        with self.assertRaises(ValueError):m.route('test',self.registry,128)

    def test_run_default_never_calls_model(self):
        with patch.object(m,'ask_model',side_effect=AssertionError('Network called unexpectedly')):
            p=m.run('test',self.registry,6,False,None,None,8,256)
        self.assertEqual(p['actual_model_calls'],0)

    def test_fail_closed_without_external_config(self):
        with self.assertRaises(ValueError):m.run('test',self.registry,6,True,None,None,8,256)

    def test_reject_http_endpoint(self):
        with self.assertRaises(ValueError):m.verify_endpoint('http://example.com/v1/chat/completions')

    def test_reject_embedded_credentials(self):
        with self.assertRaises(ValueError):m.verify_endpoint('https://name:pass@example.com')

    def test_small_call_budget_is_rejected(self):
        with patch.dict('os.environ',{'AGENT_API_KEY':'fake'},clear=True):
            with self.assertRaises(ValueError):m.run('agent security',self.registry,8,True,'https://example.com/v1/chat/completions','test',4,128)

    def test_optin_mock_provider_without_network(self):
        def fake(endpoint,model,key,role,task,max_tokens):
            return {'role_id':role['id'],'role_name':role['name'],'content':'mock evidence','duration_ms':1,'provider_reported_usage':{}}
        with patch.dict('os.environ',{'AGENT_API_KEY':'fake'},clear=True):
            with patch.object(m,'ask_model',side_effect=fake) as mocked:
                result=m.run('test',self.registry,5,True,'https://example.com/v1/chat/completions','mock-model',5,128)
        self.assertEqual(result['actual_model_calls'],5)
        self.assertEqual(mocked.call_count,5)
        self.assertEqual(result['calls'][-1]['role_id'],64)

    def test_explicit_role_128_is_selectable(self):
        out=m.route('Chọn tác tử số 128',self.registry,4,[128])
        self.assertEqual({r['id'] for r in out},{128,57,32,64})

    def test_duplicate_explicit_role_rejected(self):
        with self.assertRaises(ValueError):m.route('test',self.registry,6,[65,65])

    def test_benchmark_is_routing_only(self):
        b=m.benchmark_routing(self.registry,10)
        self.assertEqual(b['actual_model_calls'],0)
        self.assertEqual(b['iterations'],10)

if __name__=='__main__':unittest.main()
