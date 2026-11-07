import unittest
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from cluster_skill_router_v165 import classify,validate,audit_counts

class TestClusterRouter(unittest.TestCase):
    def test_registry(self): self.assertEqual(validate()["result"],"passed")
    def test_current_inventory_counts(self):
        result=validate()
        self.assertEqual(result["existing_skills"],41)
        self.assertEqual(result["integrated_candidate_skills"],8)
        self.assertEqual(result["github_installed"],0)
        self.assertEqual(result["unique_github_repositories"],382)
        self.assertEqual(result["cross_cluster_duplicate_records"],2)
    def test_original_role_preserved(self):
        self.assertEqual(classify("",known_id="agent-128")["cluster_id"],16)
        self.assertEqual(classify("",known_id="agent-001")["cluster_id"],1)
    def test_existing_skill_preserved(self):
        self.assertEqual(classify("",known_id="sanxuatnoidung")["cluster_id"],13)
    def test_new_skill_route(self):
        self.assertEqual(classify("",known_id="cluster-skill-11-smart-agriculture")["cluster_id"],15)
    def test_ai_coding(self):
        self.assertEqual(classify("software engineer refactor codebase")["cluster_id"],3)
    def test_quantum(self):
        self.assertEqual(classify("quantum circuit simulation")["cluster_id"],6)
    def test_ambiguous(self):
        self.assertEqual(classify("help me")["decision"],"requires_human_review")
    def test_no_automatic_approval(self):
        self.assertEqual(sum(d["github_accepted"] for d in audit_counts().values()),0)

if __name__=="__main__":unittest.main()
