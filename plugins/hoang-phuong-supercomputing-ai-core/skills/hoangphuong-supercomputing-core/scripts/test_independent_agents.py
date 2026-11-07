"""Offline validation of 128 independent, opt-in research-agent configurations."""
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

modpath=Path(__file__).with_name('independent_agents.py')
spec=importlib.util.spec_from_file_location('independent_agents',modpath)
agent=importlib.util.module_from_spec(spec)
spec.loader.exec_module(agent)

class AgentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root=modpath.resolve().parents[3]

    def test_every_profile_valid(self):
        r=agent.validate(self.root)
        self.assertEqual(r['status'],'pass',r['errors'])

    def test_all_agents_individually_addressable(self):
        self.assertEqual([agent.load_profile(i,self.root)['id'] for i in range(1,129)],list(range(1,129)))

    def test_all_128_have_unique_name_and_mission(self):
        p=[agent.load_profile(i,self.root) for i in range(1,129)]
        self.assertEqual(len({x['name'] for x in p}),128)
        self.assertEqual(len({x['mission'] for x in p}),128)

    def test_sixteen_disciplines(self):
        self.assertEqual(len({agent.load_profile(i,self.root)['discipline'] for i in range(1,129)}),16)

    def test_every_agent_has_curriculum_and_rubric(self):
        for i in range(1,129):
            p=agent.load_profile(i,self.root)
            self.assertEqual(len(p['doctoral_style_curriculum']),4)
            self.assertEqual(sum(p['evaluation']['rubric'].values()),100)
            self.assertEqual(p['training_status'],'curriculum_defined_only')
            self.assertTrue(p['evaluation']['requires_independent_human_domain_expert'])

    def test_unique_prompt_specialization(self):
        p=[agent.system_prompt(agent.load_profile(i,self.root)) for i in range(1,129)]
        self.assertEqual(len(set(p)),128)

    def test_dry_run_never_calls_provider(self):
        def prohibited(*_args,**_kwargs):
            raise AssertionError('provider called without execute')
        with patch.object(agent,'call_provider',prohibited):
            for i in (1,64,128):
                x=agent.run_agent(i,'Nghiên cứu tính đúng',self.root)
                self.assertEqual((x['status'],x['actual_model_calls']),('dry_run',0))

    def test_dry_run_never_writes_memory(self):
        with tempfile.TemporaryDirectory() as tmp:
            agent.run_agent(42,'test',self.root,execute=False,persist=False)
            self.assertEqual(list(Path(tmp).iterdir()),[])

    def test_invalid_ids_rejected(self):
        for v in (-1,0,129,'1',True):
            with self.assertRaises(ValueError):agent.load_profile(v,self.root)

    def test_long_task_rejected(self):
        with self.assertRaises(ValueError):agent.run_agent(1,'x'*6001,self.root)

    def test_endpoint_http_rejected(self):
        with self.assertRaises(ValueError):agent.validate_endpoint('http://example.org/v1/chat/completions','example.org')

    def test_endpoint_private_hosts_rejected(self):
        for host in ('127.0.0.1','localhost','192.168.1.100','169.254.169.254','[::1]'):
            with self.subTest(host=host),self.assertRaises(ValueError):
                agent.validate_endpoint(f'https://{host}/v1/chat/completions',host)

    def test_endpoint_allowlist_required(self):
        with self.assertRaises(ValueError):agent.validate_endpoint('https://example.org/v1/chat/completions','')
        with self.assertRaises(ValueError):agent.validate_endpoint('https://example.org/v1/chat/completions','bad.org')
        self.assertEqual(agent.validate_endpoint('https://example.org/v1/chat/completions','example.org'),
                         'https://example.org/v1/chat/completions')

    def test_endpoint_reject_userinfo_and_query(self):
        for url in ('https://u:p@example.org/v1/chat/completions','https://example.org/v1/chat/completions?api_key=secret'):
            with self.assertRaises(ValueError):agent.validate_endpoint(url,'example.org')

    def test_provider_not_called_without_credentials(self):
        with patch.dict(os.environ,{'AGENT_ALLOWED_HOSTS':'example.org'},clear=True):
            with self.assertRaises(ValueError):
                agent.run_agent(1,'test',self.root,execute=True,endpoint='https://example.org/v1/chat/completions',model='mock')

    def test_mock_provider_is_explicitly_simulated(self):
        p=lambda profile,messages: ('simulated response',{'total_tokens':12})
        a=agent.run_agent(1,'test',self.root,execute=True,provider=p)
        self.assertEqual((a['status'],a['actual_model_calls']),('simulated_test_only',0))
        self.assertFalse(a['model_weights_trained'])

    def test_agent_memory_isolated_per_id(self):
        p=lambda profile,messages:(f'reply from {profile["key"]}',{})
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            agent.run_agent(1,'question one',self.root,execute=True,provider=p,persist=True,memory_dir=root)
            agent.run_agent(2,'question two',self.root,execute=True,provider=p,persist=True,memory_dir=root)
            a=agent.read_memory(root,1);b=agent.read_memory(root,2)
            self.assertIn('question one',str(a));self.assertNotIn('question two',str(a))
            self.assertIn('question two',str(b));self.assertNotIn('question one',str(b))
            self.assertNotEqual(agent.memory_path(root,1),agent.memory_path(root,2))

    def test_memory_identity_tamper_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            memory=Path(tmp);(memory/'agent-001.json').write_text(json.dumps({'agent_id':2,'history':[]}))
            with self.assertRaises(ValueError):agent.read_memory(memory,1)

    def test_memory_is_opt_in(self):
        with self.assertRaises(ValueError):agent.run_agent(1,'q',self.root,persist=True)

    def test_team_budget_rejected(self):
        with self.assertRaises(ValueError):agent.run_team(list(range(1,10)),'q',self.root)
        with self.assertRaises(ValueError):agent.run_team([1,2,3],'q',self.root,max_calls=2)
        with self.assertRaises(ValueError):agent.run_team([1,1],'q',self.root)

    def test_team_dry_run(self):
        r=agent.run_team([1,64,128],'q',self.root)
        self.assertEqual((r['status'],r['actual_model_calls']),('dry_run',0))
        self.assertEqual([x['agent_id'] for x in r['agents']],[1,64,128])

    def test_team_mock_real_instances_and_boundaries(self):
        calls=[]
        def fake(p,msg):
            calls.append(p['id'])
            return ('test-only result',{})
        r=agent.run_team([1,64,128],'q',self.root,execute=True,provider=fake,parallel=2)
        self.assertEqual(sorted(calls),[1,64,128])
        self.assertEqual(r['actual_model_calls'],0)
        self.assertEqual(r['status'],'simulated_test_only')

    def test_dataset_schema_requires_source_and_review(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'cases.jsonl'
            p.write_text(json.dumps({'agent_id':1,'question':'q','reference_answer':'a','split':'test'}))
            self.assertEqual(agent.evaluate_dataset_schema(self.root,p)['status'],'fail')
            p.write_text(json.dumps({'agent_id':1,'question':'q','reference_answer':'a','split':'test',
                                      'source_license':'CC-BY-4.0','reviewer_id':'reviewer_1'}))
            self.assertEqual(agent.evaluate_dataset_schema(self.root,p)['status'],'pass')

    def test_dataset_leakage_detection(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'c.jsonl'
            one={'agent_id':1,'question':'same','reference_answer':'a','source_license':'owned','reviewer_id':'human','split':'train'}
            two={**one,'split':'test'}
            p.write_text(json.dumps(one)+'\n'+json.dumps(two)+'\n')
            r=agent.evaluate_dataset_schema(self.root,p)
            self.assertEqual(r['status'],'fail')

if __name__=='__main__':unittest.main()
