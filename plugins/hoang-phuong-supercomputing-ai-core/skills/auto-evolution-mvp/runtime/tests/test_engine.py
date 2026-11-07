import json
import tempfile
import unittest
from pathlib import Path
from hashlib import sha256
from unittest.mock import patch

from hpcore_evolution.engine import (scan_skills, diagnose, create_proposals, stage_proposal,
    apply_proposal, restore_backup, audit_tree, safe_read, GitHubCandidate, candidate_report)


class EvolutionTest(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory()
        self.root = Path(self.t.name)
        self.skill = self.root/'skills'/'sample'
        self.skill.mkdir(parents=True)
        self.original = '---\nname: sample\ndescription: "Use when analyzing sample requests."\n---\n# Sample\nInstructions.\n'
        (self.skill/'SKILL.md').write_text(self.original, encoding='utf-8')
        self.out = self.root/'reports'

    def tearDown(self):
        self.t.cleanup()

    def test_scan_parses_and_detects_features(self):
        skills=scan_skills(self.root/'skills')
        self.assertEqual(len(skills),1)
        self.assertEqual(skills[0]['name'],'sample')
        self.assertFalse(skills[0]['has_tests'])

    def test_scan_hashes_original_file_bytes(self):
        raw=(self.skill/'SKILL.md').read_bytes()
        scanned=scan_skills(self.root/'skills')
        self.assertEqual(scanned[0]['sha256'],sha256(raw).hexdigest())

    def test_diagnosis_has_evidence_not_fake_quality_score(self):
        items=diagnose(scan_skills(self.root/'skills'))
        self.assertTrue(any(x['code']=='missing_verification_section' for x in items))
        self.assertTrue(all('path' in x and 'evidence' in x for x in items))

    def test_stage_does_not_modify_original(self):
        issues=diagnose(scan_skills(self.root/'skills'))
        proposals=create_proposals(issues)
        self.assertTrue(proposals)
        stage_proposal(self.root/'skills',self.out,proposals[0])
        self.assertEqual((self.skill/'SKILL.md').read_text(encoding='utf-8'),self.original)
        self.assertTrue((self.out/'staged'/proposals[0]['id']/'SKILL.md').exists())

    def test_apply_requires_explicit_approval(self):
        proposals=create_proposals(diagnose(scan_skills(self.root/'skills')))
        proposal=next(x for x in proposals if x['repair_type']=='append_verification')
        stage_proposal(self.root/'skills',self.out,proposal)
        with self.assertRaises(PermissionError):
            apply_proposal(self.root/'skills',self.out,proposal['id'],approval='no')
        self.assertEqual((self.skill/'SKILL.md').read_text(encoding='utf-8'),self.original)

    def test_apply_and_restore_backup(self):
        proposal=next(x for x in create_proposals(diagnose(scan_skills(self.root/'skills'))) if x['repair_type']=='append_verification')
        stage_proposal(self.root/'skills',self.out,proposal)
        applied=apply_proposal(self.root/'skills',self.out,proposal['id'],approval=proposal['id'])
        self.assertIn('Kiểm chứng', (self.skill/'SKILL.md').read_text(encoding='utf-8'))
        restore_backup(self.root/'skills',self.out,applied['backup_id'],approval=applied['backup_id'])
        self.assertEqual((self.skill/'SKILL.md').read_text(encoding='utf-8'),self.original)

    def test_apply_rejects_changed_original(self):
        p=create_proposals(diagnose(scan_skills(self.root/'skills')))[0]
        stage_proposal(self.root/'skills',self.out,p)
        (self.skill/'SKILL.md').write_text('modified',encoding='utf-8')
        with self.assertRaises(ValueError):
            apply_proposal(self.root/'skills',self.out,p['id'],approval=p['id'])

    def test_path_traversal_is_rejected(self):
        with self.assertRaises(ValueError):safe_read(self.root/'skills','../outside')

    def test_symlink_components_are_rejected_without_os_symlink_support(self):
        link=self.root/'skills'/'sneaky'
        with patch.object(Path,'is_symlink',autospec=True,side_effect=lambda path:path==link):
            with self.assertRaises(ValueError):safe_read(self.root/'skills','sneaky')

    def test_audit_tree_hash_detects_tampering(self):
        a=audit_tree(self.root/'skills')
        (self.skill/'SKILL.md').write_text('changed',encoding='utf-8')
        b=audit_tree(self.root/'skills')
        self.assertNotEqual(a['tree_sha256'],b['tree_sha256'])

    def test_research_candidate_no_auto_install(self):
        c=GitHubCandidate('owner','repo','abc123','MIT','2026-01-01','https://github.com/owner/repo')
        report=candidate_report(c)
        self.assertEqual(report['status'],'metadata_only')
        self.assertFalse(report['can_install'])

    def test_no_duplicate_on_rerun(self):
        issues=diagnose(scan_skills(self.root/'skills'))
        a=create_proposals(issues);b=create_proposals(issues)
        self.assertEqual([i['id'] for i in a],[i['id'] for i in b])

if __name__=='__main__':unittest.main()
