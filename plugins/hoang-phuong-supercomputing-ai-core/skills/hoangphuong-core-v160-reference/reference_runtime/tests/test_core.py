import sqlite3
import tempfile
import unittest
from pathlib import Path
from hpcore.core import AuditStore, Limits, Orchestrator, Policy, PolicyDenied, Request, Router, ToolRegistry

class CoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.audit = AuditStore(Path(self.tmp.name) / 'audit.db', secret=b'local-test-key')
    def tearDown(self): self.tmp.cleanup()
    def test_kill_switch_on_by_default(self):
        d=Orchestrator(Policy(), self.audit).run(Request('build app'))
        self.assertFalse(d.allowed); self.assertEqual(d.evidence, 'BLOCKED')
    def test_plan_with_explicit_opt_in(self):
        d=Orchestrator(Policy(), self.audit, kill_switch=False).run(Request('kiểm thử api'))
        self.assertTrue(d.allowed); self.assertIn('integrator', d.roles); self.assertIn('evaluator', d.roles)
    def test_denies_all_sensitive_actions_even_with_approval(self):
        orch=Orchestrator(Policy(allowed_resources={'local:plan'}), self.audit, kill_switch=False)
        for act in ['write','publish','delete','payment','admin','external_network']:
            self.assertFalse(orch.run(Request('test', action=act, approved=True)).allowed)
    def test_denies_unknown_action(self):
        self.assertFalse(Orchestrator(Policy(), self.audit, False).run(Request('do something', action='root')).allowed)
    def test_denies_unlisted_resource(self):
        self.assertFalse(Orchestrator(Policy(), self.audit, False).run(Request('test', resource='https://example.com')).allowed)
    def test_denies_high_cost(self):
        self.assertFalse(Orchestrator(Policy(), self.audit, False).run(Request('test', estimated_cost_usd=2.0)).allowed)
    def test_denies_empty_or_oversize(self):
        o=Orchestrator(Policy(), self.audit, False)
        self.assertFalse(o.run(Request('')).allowed)
        self.assertFalse(o.run(Request('x'*12001)).allowed)
    def test_roles_are_bounded(self):
        self.assertLessEqual(len(Router.choose('api security benchmark plugin test')), 4)
    def test_audit_chain(self):
        o=Orchestrator(Policy(), self.audit, False)
        o.run(Request('task1'));o.run(Request('task2'))
        self.assertTrue(self.audit.verify())
    def test_audit_tamper_detected(self):
        Orchestrator(Policy(), self.audit, False).run(Request('task1'))
        with sqlite3.connect(self.audit.db) as c:
            c.execute("UPDATE events SET reason='modified' WHERE id=1")
        self.assertFalse(self.audit.verify())
    def test_registry_requires_host_presence(self):
        reg=ToolRegistry();reg.register('provider.read', 'read', 'demo')
        self.assertEqual(reg.resolve('provider.read', set())['status'], 'external_tool_unavailable')
        self.assertEqual(reg.resolve('provider.read', {'provider.read'})['status'], 'HOST_VISIBLE_NOT_EXECUTED')
    def test_invalid_limits(self):
        with self.assertRaises(ValueError): Policy(limits=Limits(max_steps=0))
    def test_audit_does_not_store_task_text(self):
        secret='private user task sample xyz'
        Orchestrator(Policy(), self.audit, False).run(Request(secret))
        with sqlite3.connect(self.audit.db) as c:
            values=str(c.execute('SELECT * FROM events').fetchall())
        self.assertNotIn(secret, values)

if __name__ == '__main__': unittest.main()
