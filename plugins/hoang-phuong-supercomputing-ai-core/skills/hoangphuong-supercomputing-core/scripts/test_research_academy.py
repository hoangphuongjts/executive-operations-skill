"""Offline research academy regression & negative tests: no network or model calls."""
from pathlib import Path
import importlib.util,json,tempfile,unittest
p=Path(__file__).with_name('research_academy.py')
s=importlib.util.spec_from_file_location('research_academy',p)
ra=importlib.util.module_from_spec(s);s.loader.exec_module(ra)

class Tests(unittest.TestCase):
    @staticmethod
    def source():
        return {'source_id':'test','title':'synthetic','canonical_url':'https://example.com/a',
                'rights_holder':'test author','license_id':'CC-BY-4.0',
                'license_evidence_url':'https://example.com/license',
                'allowed_uses':['quote','rag'],'review_status':'human_reviewed',
                'reviewer_id':'test-reviewer','reviewed_at':'2026-11-04','attribution':'test author'}
    @staticmethod
    def review(name):
        return {'agent_id':25,'case_id':'R025-P1','reviewer_id':name,
            'artifact_sha256':'a'*64,'reviewer_type':'human_domain_expert',
            'reviewed_at':'2026-11-04','scores':ra.RUBRIC.copy(),
            'evidence_source_ids':['test'],'critical_issue':False}
    @staticmethod
    def claim(status):return {'claim':'X','alternative':'Y','falsification_test':'test X','counterexample':'Z','status':status}
    def test_rubric_total(self):self.assertEqual(sum(ra.RUBRIC.values()),100)
    def test_approved_metadata_not_legal_proof(self):
        x=ra.check_license(self.source(),'rag');self.assertTrue(x['metadata_gate_passed']);self.assertFalse(x['legal_rights_verified'])
    def test_unknown_license_fails(self):
        s=self.source();s['license_id']='unknown';self.assertFalse(ra.check_license(s,'rag')['metadata_gate_passed'])
    def test_pending_license_fails(self):
        s=self.source();s['review_status']='pending_review';self.assertFalse(ra.check_license(s,'rag')['metadata_gate_passed'])
    def test_training_use_not_implied(self):self.assertFalse(ra.check_license(self.source(),'training')['metadata_gate_passed'])
    def test_attribution_required(self):
        s=self.source();s.pop('attribution');self.assertFalse(ra.check_license(s,'rag')['metadata_gate_passed'])
    def test_bad_license_date(self):
        s=self.source();s['reviewed_at']='tomorrow';self.assertFalse(ra.check_license(s,'rag')['metadata_gate_passed'])
    def test_https_required(self):
        s=self.source();s['canonical_url']='http://example.com';self.assertFalse(ra.check_license(s,'rag')['metadata_gate_passed'])
    def test_unknown_purpose_error(self):
        with self.assertRaises(ValueError):ra.check_license(self.source(),'scrape')
    def test_empty_registry_not_populated(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/ra.CORE/'academy/source_registry.json';p.parent.mkdir(parents=True);p.write_text('{"sources":[]}')
            self.assertEqual(ra.licenses(Path(d))['status'],'no_approved_sources')
    def test_duplicate_license_id_error(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/ra.CORE/'academy/source_registry.json';p.parent.mkdir(parents=True)
            p.write_text(json.dumps({'sources':[self.source(),self.source()]}))
            with self.assertRaises(ValueError):ra.licenses(Path(d))
    def test_report_version_matches_manifest(self):
        manifest=json.loads((ra.ROOT/'plugin.json').read_text(encoding='utf-8'))
        self.assertEqual(ra.report(ra.ROOT)['version'],manifest['version'])
    def test_pilot_outside_bounds(self):
        for id in [1,24,33,128]:
            with self.assertRaises(ValueError):ra.pilot(Path('.'),id)
    def test_two_high_reviews_not_credential(self):
        r=ra.assess_records([self.review('alice'),self.review('bob')],{'test'})
        x=r['cases'][0];self.assertIn('candidate_pending',x['status']);self.assertFalse(x['expert_degree_certified'])
    def test_single_review_not_enough(self):
        r=ra.assess_records([self.review('alice')],{'test'});self.assertEqual(r['cases'][0]['status'],'not_yet_eligible')
    def test_duplicate_reviewer_not_enough(self):
        r=ra.assess_records([self.review('alice'),self.review('alice')],{'test'})
        self.assertEqual(r['cases'][0]['status'],'not_yet_eligible')
    def test_critical_issue_blocks(self):
        x=self.review('alice');x['critical_issue']=True
        r=ra.assess_records([x,self.review('bob')],{'test'});self.assertEqual(r['cases'][0]['status'],'blocked_critical_issue')
    def test_unapproved_reference_fails(self):
        r=ra.assess_records([self.review('alice')],set());self.assertEqual(len(r['invalid_records']),1)
    def test_overmax_score_fails(self):
        x=self.review('alice');x['scores']['accuracy']=26
        self.assertEqual(len(ra.assess_records([x],{'test'})['invalid_records']),1)
    def test_nonhuman_reviewer_fails(self):
        x=self.review('alice');x['reviewer_type']='automated'
        self.assertEqual(len(ra.assess_records([x],{'test'})['invalid_records']),1)
    def test_bad_digest_fails(self):
        x=self.review('alice');x['artifact_sha256']='wrong'
        self.assertEqual(len(ra.assess_records([x],{'test'})['invalid_records']),1)
    def test_debate_hypothesis_passes(self):
        self.assertEqual(ra.debate_check([self.claim('hypothesis')])['status'],'pass')
    def test_debate_fake_experiment_rejected(self):
        self.assertEqual(ra.debate_check([self.claim('tested')])['status'],'fail')
    def test_debate_fake_refutation_rejected(self):
        self.assertEqual(ra.debate_check([self.claim('refuted')])['status'],'fail')
    def test_full_plugin_if_available(self):
        if not (ra.ROOT/ra.CORE/'references/AGENTS_128.json').exists():self.skipTest('patch only')
        x=ra.validate(ra.ROOT);self.assertEqual(x['status'],'pass',x['errors'])
        self.assertEqual(ra.licenses(ra.ROOT)['approved_metadata_count'],0)
        self.assertEqual(ra.pilot(ra.ROOT,28)['agent']['name'],'Formal Methods Specialist')
        self.assertEqual(ra.report(ra.ROOT)['academy_status']['pilot_evaluation_results'],0)
        self.assertEqual(ra.report(ra.ROOT)['status'],'pass')
if __name__=='__main__':unittest.main()
