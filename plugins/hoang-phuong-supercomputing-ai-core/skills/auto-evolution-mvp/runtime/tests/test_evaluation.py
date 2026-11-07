import json
import tempfile
import unittest
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
from hpcore_evolution.evaluation import validate_evidence, compare_runs, assess_candidate, write_release_candidate
from hpcore_evolution.cli import main


def sample(run_id, passed, *, safety=True, source='independent_human_reviewed'):
    return {'run_id': run_id, 'dataset_id': 'frozen-dataset-2026-11',
            'dataset_sha256':'a'*64, 'evaluator': source, 'environment':'python-local-test',
            'model_version':'mocked-test-pipeline', 'tasks':[{'id':str(i),'passed':i < passed} for i in range(5)],
            'security_blockers': ([] if safety else ['critical-unresolved']),
            'measured_at': '2026-11-05T00:00:00Z'}


class EvaluationTest(unittest.TestCase):
    def test_requires_provenance_and_nonempty_tasks(self):
        with self.assertRaises(ValueError):validate_evidence({'tasks':[]})
    def test_rejects_duplicate_ids(self):
        e=sample('a',3);e['tasks'][1]['id']='0'
        with self.assertRaises(ValueError):validate_evidence(e)
    def test_rejects_self_judgement_as_independent(self):
        e=sample('a',3,source='model_self_review')
        with self.assertRaises(ValueError):validate_evidence(e)
    def test_rejects_dataset_mismatch(self):
        b=sample('baseline',3);c=sample('candidate',4);c['dataset_sha256']='b'*64
        with self.assertRaises(ValueError):compare_runs(b,c)
    def test_rejects_id_mismatch(self):
        b=sample('baseline',3);c=sample('candidate',4);c['tasks'][4]['id']='other'
        with self.assertRaises(ValueError):compare_runs(b,c)
    def test_reports_improvement_without_claiming_deployment(self):
        r=compare_runs(sample('baseline',3),sample('candidate',4))
        self.assertEqual(r['decision'],'candidate_eligible_for_review')
        self.assertEqual(r['improved_tasks'],1)
        self.assertEqual(r['status'],'offline_evidence_compared_not_deployed')
    def test_blocks_regression(self):
        r=compare_runs(sample('baseline',4),sample('candidate',3))
        self.assertEqual(r['decision'],'blocked_regression')
    def test_blocks_security_issue(self):
        r=compare_runs(sample('baseline',3),sample('candidate',4,safety=False))
        self.assertEqual(r['decision'],'blocked_security')
    def test_release_gate_explicit_approval_even_after_pass(self):
        r=compare_runs(sample('baseline',3),sample('candidate',4))
        self.assertEqual(assess_candidate(r,approval=False)['can_deploy'],False)
        self.assertEqual(assess_candidate(r,approval=True)['can_deploy'],False)
    def test_release_record_cannot_claim_deployment(self):
        r=compare_runs(sample('baseline',3),sample('candidate',4))
        with tempfile.TemporaryDirectory() as t:
            doc=write_release_candidate(Path(t),r)
            self.assertTrue(doc.exists())
            self.assertEqual(json.loads(doc.read_text())['stage'],'review_only')
    def test_cli_evaluate_read_only(self):
        with tempfile.TemporaryDirectory() as t:
            base=Path(t); root=base/'skills';root.mkdir(); reports=base/'reports'
            bp=base/'b.json';cp=base/'c.json'
            bp.write_text(json.dumps(sample('baseline',3)),encoding='utf-8');cp.write_text(json.dumps(sample('candidate',4)),encoding='utf-8')
            output=StringIO()
            with redirect_stdout(output):
                main(['--root',str(root),'--reports',str(reports),'evaluate','--baseline',str(bp),'--candidate',str(cp)])
            self.assertEqual(json.loads(output.getvalue())['decision'],'candidate_eligible_for_review')
            self.assertTrue((reports/'evaluation.json').exists())
