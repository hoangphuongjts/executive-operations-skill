import json
import shutil
import tempfile
import unittest
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
from hpcore_evolution.cli import main
from hpcore_evolution.engine import fetch_github_metadata, search_github_repositories

class CliTest(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory()
        self.root=Path(self.t.name)
        self.skills=self.root/'skills'
        f=self.skills/'demo-skill';f.mkdir(parents=True)
        (f/'SKILL.md').write_text('---\nname: demo-skill\ndescription: "Use when demo"\n---\n# Demo',encoding='utf-8')
        self.reports=self.root/'reports'
    def tearDown(self):self.t.cleanup()
    def invoke(self,*argv):
        out=StringIO()
        with redirect_stdout(out):main(['--root',str(self.skills),'--reports',str(self.reports),*argv])
        return json.loads(out.getvalue())
    def test_cycle_produces_reports_without_mutating_skill(self):
        before=(self.skills/'demo-skill'/'SKILL.md').read_bytes()
        a=self.invoke('cycle')
        self.assertEqual(a['skills_scanned'],1)
        self.assertTrue((self.reports/'assessment.json').exists())
        self.assertEqual(before,(self.skills/'demo-skill'/'SKILL.md').read_bytes())
    def test_cli_stage_apply_restore(self):
        p=self.invoke('cycle')['proposals'][0]
        self.invoke('stage',p['id'])
        applied=self.invoke('apply',p['id'],'--approve',p['id'])
        self.assertEqual(applied['status'],'local_doc_patch_applied')
        restored=self.invoke('restore',applied['backup_id'],'--approve',applied['backup_id'])
        self.assertEqual(restored['status'],'restored')
    def test_network_requires_explicit_permission(self):
        with self.assertRaises(PermissionError):fetch_github_metadata('github/spec-kit')
    def test_discover_network_blocked_by_default(self):
        with self.assertRaises(PermissionError):search_github_repositories('agent workflows')
    def test_discover_invalid_query_or_limit(self):
        with self.assertRaises(ValueError):search_github_repositories('a',allow_network=True)
        with self.assertRaises(ValueError):search_github_repositories('agent',allow_network=True,limit=25)
    def test_reject_reports_inside_source(self):
        with self.assertRaises(SystemExit):
            main(['--root',str(self.skills),'--reports',str(self.skills/'out'),'scan'])

if __name__=='__main__':unittest.main()
