"""Bounded cross-cluster plan & execution tests (offline, no external calls)."""
from pathlib import Path
import tempfile
import unittest
from contextlib import closing
from unittest.mock import patch
import os

import platform128 as core
import cluster_debate as d

class ClusterTests(unittest.TestCase):
    def test_cluster_counts(self):
        c=d.clusters()
        self.assertEqual(len(c),16)
        self.assertEqual(sum(x['agent_count'] for x in c),128)
        self.assertEqual(sorted(i for g in c for i in g['agent_ids']),list(range(1,129)))
    def test_routing_vietnamese_topic(self):
        plan=d.plan('Sản xuất video khoa học thiên văn cho YouTube, cần kiểm chứng nội dung')
        group_ids={x['cluster_id'] for x in plan['specialists']}
        self.assertIn(13,group_ids)
        self.assertTrue(1 in group_ids or 16 in group_ids)
    def test_film_and_3d_recommend_different_clusters(self):
        result=d.plan('Thiết kế phim hoạt hình 3D bằng AI',max_specialists=4)
        groups={x['cluster_id'] for x in result['specialists']}
        self.assertIn(13,groups)
        self.assertIn(15,groups)
    def test_routing_software_topic(self):
        plan=d.plan('Phát triển phần mềm Python API lưu dữ liệu với bảo mật',max_specialists=4)
        self.assertLessEqual(len(plan['specialists']),4)
        self.assertTrue({2,3,10,12}.intersection({x['cluster_id'] for x in plan['specialists']}))
    def test_generic_task_uses_two_clusters(self):
        plan=d.plan('Tôi cần tư vấn')
        self.assertGreaterEqual(len({x['cluster_id'] for x in plan['specialists']}),2)
    def test_unique_agents_no_core_as_specialists(self):
        plan=d.plan('Kiến trúc hệ thống và bảo mật dữ liệu')
        ids=[x['id'] for x in plan['specialists']]
        self.assertEqual(len(set(ids)),len(ids))
        self.assertTrue(all(i not in d.CORE_AGENTS for i in ids))
    def test_manual_ids(self):
        plan=d.plan('Thiết kế app',3,forced_ids=[9,128])
        self.assertEqual([x['id'] for x in plan['specialists']],[9,128])
        self.assertEqual(plan['estimated_model_calls'],6)
    def test_refuse_duplicate_ids(self):
        for invalid in [[9,9],[9,32],[0,128],[True,128],[129,9]]:
            with self.subTest(invalid=invalid),self.assertRaises(ValueError):d.plan('Task',3,invalid)
    def test_wrong_max_specialists(self):
        for n in [1,5,0,True,'3']:
            with self.subTest(n=n),self.assertRaises(ValueError):d.plan('Task',n)
    def test_long_task_denied(self):
        with self.assertRaises(ValueError):d.plan('T'*(core.MAX_TASK+1))
    def test_no_model_call_on_dryrun(self):
        with tempfile.TemporaryDirectory() as td,closing(core.connect(Path(td)/'t.sqlite')) as db:
            def bad_provider(messages):raise AssertionError('no provider calls allowed')
            result=d.run_debate(db,'Lập dự án video',provider=bad_provider)
            self.assertEqual(result['api_calls'],0)
            self.assertFalse(result['debate_performed'])
    def test_external_disallowed_even_with_mock(self):
        with tempfile.TemporaryDirectory() as td,closing(core.connect(Path(td)/'t.sqlite')) as db:
            with patch.dict(os.environ,{'AGENT_ALLOW_EXTERNAL':'0'}):
                with self.assertRaises(RuntimeError):d.run_debate(db,'Kiểm tra dữ liệu',True,provider=lambda m:('mock',{}))
    def test_actual_phases_under_mock_provider(self):
        calls=[]
        def mock(messages):
            calls.append(messages)
            return ('Câu trả lời mô phỏng '+str(len(calls)),{'total_tokens':3})
        with tempfile.TemporaryDirectory() as td,closing(core.connect(Path(td)/'t.sqlite')) as db:
            with patch.dict(os.environ,{'AGENT_ALLOW_EXTERNAL':'1'}):
                result=d.run_debate(db,'Nghiên cứu video và dữ liệu',execute=True,forced_ids=[1,105],provider=mock)
            self.assertEqual(result['api_calls'],6)
            self.assertEqual(len(calls),6)
            self.assertEqual([x['stage'] for x in result['trace']],['independent','independent','critical_review','rebuttal','rebuttal','integrated_verdict'])
            self.assertEqual(result['status'],'model_synthesis_unverified')
            self.assertEqual(result['evidence_status'],'requires_independent_fact_check')
            self.assertNotIn('trained_weights',str(result))
            self.assertEqual(db.execute('select count(*) from memory').fetchone()[0],0)
    def test_max_ten_provider_calls(self):
        calls=[]
        def mock(m):calls.append(m);return ('ok',{})
        with tempfile.TemporaryDirectory() as td,closing(core.connect(Path(td)/'t.sqlite')) as db:
            with patch.dict(os.environ,{'AGENT_ALLOW_EXTERNAL':'1'}):
                result=d.run_debate(db,'Phát triển ứng dụng AI',True,4,[9,10,17,128],mock)
        self.assertEqual(result['api_calls'],10)
        self.assertEqual(len(calls),10)
    def test_peer_messages_are_limited(self):
        def verbose(m):return ('Lời phản biện '+('X'*15000),{})
        with tempfile.TemporaryDirectory() as td,closing(core.connect(Path(td)/'t.sqlite')) as db:
            with patch.dict(os.environ,{'AGENT_ALLOW_EXTERNAL':'1'}):
                res=d.run_debate(db,'Viết kịch bản video',True,3,[105,106],verbose)
        self.assertLessEqual(max(len(x['answer']) for x in res['rebuttals']),1400)
        self.assertLessEqual(len(res['critic']['analysis']),1800)

if __name__=='__main__':unittest.main()
