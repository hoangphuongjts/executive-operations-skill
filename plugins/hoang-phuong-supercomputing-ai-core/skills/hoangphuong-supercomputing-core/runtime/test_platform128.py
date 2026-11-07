"""Offline tests: no paid model calls, no cloud, no pretrained-model claims."""
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import platform128 as p


class RegistryTests(unittest.TestCase):
    def test_128_agent_profiles(self):
        self.assertEqual(len(p.catalog()),128)
    def test_16_groups_eight_each(self):
        self.assertEqual(sorted(set(a['group_id'] for a in p.catalog())),list(range(1,17)))
    def test_128_distinct_names(self):
        self.assertEqual(len({a['name'] for a in p.catalog()}),128)
    def test_eval_blueprints(self):
        self.assertEqual(len(p.eval_catalog()),128)
    def test_evaluation_not_certified(self):
        self.assertEqual(p.evaluate_structure()['model_ability_status'],'not_evaluated')
    def test_agent_128(self):
        self.assertEqual(p.get_agent(128)['id'],128)
    def test_bad_id(self):
        for k in [True,0,129,'42',-1]:
            with self.subTest(k=k),self.assertRaises(ValueError):p.get_agent(k)
    def test_missing_provider(self):
        with patch.dict(os.environ, {'AGENT_MODEL_ENDPOINT':'','AGENT_MODEL_NAME':''}):
            with self.assertRaises(RuntimeError):p.endpoint_config()
    def test_insecure_provider_rejected(self):
        with patch.dict(os.environ, {'AGENT_MODEL_ENDPOINT':'http://some-external-server.example/v1/chat/completions','AGENT_MODEL_NAME':'x'}):
            with self.assertRaises(ValueError):p.endpoint_config()
    def test_local_provider_accepted(self):
        with patch.dict(os.environ, {'AGENT_MODEL_ENDPOINT':'http://localhost:11434/v1/chat/completions','AGENT_MODEL_NAME':'local'}):
            self.assertEqual(p.endpoint_config()[1],'local')

class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.db=p.connect(Path(self.tmp.name)/'test.sqlite')
    def tearDown(self):
        self.db.close();self.tmp.cleanup()
    def doc(self,group=1,license='project_original'):
        return {'group_id':group,'title':'Giả thuyết phản biện','body':'Giả thuyết phải có đối chứng và phản ví dụ để kiểm định.',
                'license':license,'author':'Nhóm tác giả','approved_by':'Chủ dự án',
                'permission_proof':'Nguồn do tác giả tự biên soạn','source_url':''}
    def test_ingest_original(self):
        self.assertEqual(p.ingest(self.db,self.doc())['group_id'],1)
    def test_group_isolation(self):
        p.ingest(self.db,self.doc())
        self.assertEqual(len(p.search_docs(self.db,1,'giả thuyết')),1)
        self.assertEqual(len(p.search_docs(self.db,2,'giả thuyết')),0)
    def test_reject_unlicensed(self):
        with self.assertRaises(ValueError):p.ingest(self.db,self.doc(license='unknown'))
    def test_external_needs_review(self):
        d=self.doc(license='CC-BY-4.0');d['source_url']='https://example.com/faq'
        with self.assertRaises(ValueError):p.ingest(self.db,d)
        d['reviewed_license']=True
        self.assertEqual(p.ingest(self.db,d)['review_status'],'self_attested')
    def test_external_http_rejected(self):
        d=self.doc(license='CC0-1.0');d.update(source_url='http://example.com',reviewed_license=True)
        with self.assertRaises(ValueError):p.ingest(self.db,d)
    def test_bad_group(self):
        d=self.doc(group=17)
        with self.assertRaises(ValueError):p.ingest(self.db,d)
    def test_duplicate_document(self):
        d=self.doc();p.ingest(self.db,d);p.ingest(self.db,d)
        self.assertEqual(self.db.execute('select count(*) from documents').fetchone()[0],1)
    def test_default_dry_run_no_model(self):
        self.assertEqual(p.run_agent(self.db,1,'Mô tả kiểm định')['status'],'dry_run')
    def test_external_disabled(self):
        with patch.dict(os.environ, {'AGENT_ALLOW_EXTERNAL':'0'}):
            with self.assertRaises(RuntimeError):p.run_agent(self.db,1,'Giải thích',True,provider=lambda m: ('x',{}))
    def test_provider_mock_and_memory_opt_in(self):
        observed=[]
        def fake(messages):
            observed.append(messages)
            return ('câu trả lời mẫu', {'total_tokens':14})
        with patch.dict(os.environ, {'AGENT_ALLOW_EXTERNAL':'1'}):
            result=p.run_agent(self.db,1,'Kiểm định giả thuyết',True,remember=True,session='s',provider=fake)
            self.assertEqual(result['status'],'model_response_unverified')
            self.assertEqual(len(p.memory_read(self.db,1,'s')),1)
            self.assertEqual(len(p.memory_read(self.db,2,'s')),0)
            p.run_agent(self.db,1,'Phản ví dụ',True,remember=False,provider=fake)
            self.assertEqual(len(p.memory_read(self.db,1,'default')),0)
    def test_isolated_document_in_prompt(self):
        p.ingest(self.db,self.doc(group=1));calls=[]
        def fake(msg):calls.append(msg);return ('ok',{})
        with patch.dict(os.environ, {'AGENT_ALLOW_EXTERNAL':'1'}):
            p.run_agent(self.db,1,'giả thuyết',True,provider=fake)
            self.assertIn('Giả thuyết phản biện',calls[0][0]['content'])
            p.run_agent(self.db,9,'giả thuyết',True,provider=fake)
            self.assertNotIn('Giả thuyết phản biện',calls[1][0]['content'])
    def test_team_cap(self):
        with self.assertRaises(ValueError):p.team(self.db,list(range(1,10)),'x')
        with self.assertRaises(ValueError):p.team(self.db,[1,1],'x')
    def test_team_dryrun(self):
        self.assertEqual(p.team(self.db,[1,2],'nghiên cứu')['agent_count'],2)
    def test_doc_too_large(self):
        d=self.doc();d['body']='A'*(p.MAX_DOC+1)
        with self.assertRaises(ValueError):p.ingest(self.db,d)
    def test_memory_deletion_is_scoped(self):
        self.db.execute("INSERT INTO memory(agent_id,session_id,prompt,answer,created_at) VALUES (1,'s','a','b','t')")
        self.db.execute("INSERT INTO memory(agent_id,session_id,prompt,answer,created_at) VALUES (2,'s','a','c','t')")
        with self.db:self.db.execute('DELETE FROM memory WHERE agent_id=? AND session_id=?',(1,'s'))
        self.assertEqual(self.db.execute('select count(*) from memory').fetchone()[0],1)
        self.assertEqual(self.db.execute('select agent_id from memory').fetchone()[0],2)

if __name__=='__main__':unittest.main()

class ExpertReviewTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.db=p.connect(Path(self.tmp.name)/'reviews.sqlite')
    def tearDown(self):
        self.db.close();self.tmp.cleanup()
    def valid(self):
        return {'agent_id':1,'case_id':'D001-001','reviewer':'Independent reviewer - self-attested',
                'score':87,'feedback':'Bổ sung nhóm đối chứng và nói rõ giới hạn mẫu','approved':True}
    def test_review_applied_only_to_same_agent(self):
        p.submit_review(self.db,self.valid())
        self.assertEqual(len(p.approved_feedback(self.db,1)),1)
        self.assertEqual(len(p.approved_feedback(self.db,2)),0)
    def test_reject_wrong_case(self):
        bad=self.valid();bad['case_id']='D002-002'
        with self.assertRaises(ValueError):p.submit_review(self.db,bad)
    def test_review_not_verified_degree(self):
        result=p.submit_review(self.db,self.valid())
        self.assertEqual(result['status'],'self_attested_review')
    def test_bad_score(self):
        bad=self.valid();bad['score']=101
        with self.assertRaises(ValueError):p.submit_review(self.db,bad)
    def test_review_not_approved_not_used(self):
        d=self.valid();d['approved']=False
        p.submit_review(self.db,d)
        self.assertEqual(len(p.approved_feedback(self.db,1)),0)
    def test_eval_group_has_eight_cases(self):
        result=p.eval_group(self.db,16)
        self.assertEqual(result['cases'],8)
        self.assertEqual(result['status'],'evaluation_plan_only')
    def test_eval_group_rejects_bad_group(self):
        with self.assertRaises(ValueError):p.eval_group(self.db,17)
