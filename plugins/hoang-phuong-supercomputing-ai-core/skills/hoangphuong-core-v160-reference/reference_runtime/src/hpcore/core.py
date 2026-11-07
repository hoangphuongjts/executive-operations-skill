"""Local-only reference implementation for Core v15.2-v16.0.
No remote execution, subprocess, privileged actions, or built-in third-party bindings.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import hmac
import json
import os
import sqlite3
import time
import uuid
from typing import Callable

ROLES = {"planner", "critic", "integrator", "evaluator"}  # Roles are lenses, not independent agents.
SENSITIVE_ACTIONS = {"write", "publish", "delete", "payment", "admin", "external_network"}
ALL_ACTIONS = {"plan", "read", *SENSITIVE_ACTIONS}

class PolicyDenied(Exception):
    pass

@dataclass(frozen=True)
class Limits:
    max_steps: int = 8
    max_cost_usd: float = 0.50
    timeout_seconds: float = 60.0
    max_input_chars: int = 12000
    def validate(self):
        if not (1 <= self.max_steps <= 8): raise ValueError("max_steps must be 1..8")
        if not (0 <= self.max_cost_usd <= 100): raise ValueError("invalid cost")
        if not (0 < self.timeout_seconds <= 300): raise ValueError("invalid timeout")
        if not (1 <= self.max_input_chars <= 50000): raise ValueError("invalid input limit")

@dataclass(frozen=True)
class Request:
    task: str
    action: str = "plan"
    resource: str = "local:plan"
    approved: bool = False
    approval_token: str = ""
    estimated_cost_usd: float = 0.0

@dataclass
class Decision:
    allowed: bool
    reason: str
    task_id: str
    roles: list[str] = field(default_factory=list)
    evidence: str = "DESIGNED"

class Policy:
    def __init__(self, allowed_resources: set[str] | None = None, limits: Limits | None = None):
        self.allowed_resources = allowed_resources if allowed_resources is not None else {"local:plan", "local:demo"}
        self.limits = limits or Limits()
        self.limits.validate()

    def check(self, req: Request) -> None:
        if not req.task.strip() or len(req.task) > self.limits.max_input_chars: raise PolicyDenied("invalid task length")
        if req.action not in ALL_ACTIONS: raise PolicyDenied("unknown action denied")
        if req.resource not in self.allowed_resources: raise PolicyDenied("resource outside allowlist")
        if req.estimated_cost_usd < 0 or req.estimated_cost_usd > self.limits.max_cost_usd:
            raise PolicyDenied("cost ceiling exceeded")
        if req.action in SENSITIVE_ACTIONS:
            # An approval flag alone does not authorize real host writes; this prototype refuses them all.
            raise PolicyDenied("sensitive actions require external host authorization; prototype never executes")

class Router:
    @staticmethod
    def choose(task: str) -> list[str]:
        t = task.casefold()
        names = ["planner"]
        if any(k in t for k in ("lỗi", "bug", "security", "bảo mật", "audit", "kiểm toán", "risk")):
            names.append("critic")
        if any(k in t for k in ("api", "tích hợp", "integration", "plugin", "workflow")):
            names.append("integrator")
        if any(k in t for k in ("test", "benchmark", "đánh giá", "kiểm thử")):
            names.append("evaluator")
        return names[:4]

class AuditStore:
    """Local SQLite audit; no private task bodies; optional HMAC for tamper-evident chaining.
    This is NOT a provider-side immutable audit log.
    """
    def __init__(self, db: str | Path, secret: bytes | None = None):
        self.db = str(db)
        self.secret = secret
        with sqlite3.connect(self.db) as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT, time_utc TEXT NOT NULL,
                task_id TEXT NOT NULL, task_hash TEXT NOT NULL, action TEXT NOT NULL,
                outcome TEXT NOT NULL, reason TEXT NOT NULL, previous_hash TEXT NOT NULL,
                entry_hash TEXT NOT NULL)''')

    def record(self, req: Request, outcome: str, reason: str, task_id: str) -> str:
        ts = datetime.now(timezone.utc).isoformat()
        th = sha256(req.task.encode('utf-8')).hexdigest()
        with sqlite3.connect(self.db, timeout=10) as conn:
            conn.execute('BEGIN IMMEDIATE')
            row = conn.execute('SELECT entry_hash FROM events ORDER BY id DESC LIMIT 1').fetchone()
            prev = row[0] if row else "GENESIS"
            payload = json.dumps([ts, task_id, th, req.action, outcome, reason, prev], ensure_ascii=False, separators=(',', ':'))
            digest = hmac.new(self.secret, payload.encode(), 'sha256').hexdigest() if self.secret else sha256(payload.encode()).hexdigest()
            conn.execute('INSERT INTO events (time_utc,task_id,task_hash,action,outcome,reason,previous_hash,entry_hash) VALUES (?,?,?,?,?,?,?,?)', (ts, task_id, th, req.action, outcome, reason, prev, digest))
        return digest

    def verify(self) -> bool:
        with sqlite3.connect(self.db) as conn:
            rows = conn.execute('SELECT time_utc,task_id,task_hash,action,outcome,reason,previous_hash,entry_hash FROM events ORDER BY id').fetchall()
        prev = 'GENESIS'
        for ts, tid, th, action, outcome, reason, stored_prev, signature in rows:
            if prev != stored_prev: return False
            payload = json.dumps([ts, tid, th, action, outcome, reason, prev], ensure_ascii=False, separators=(',', ':'))
            expected = hmac.new(self.secret, payload.encode(), 'sha256').hexdigest() if self.secret else sha256(payload.encode()).hexdigest()
            if not hmac.compare_digest(expected, signature): return False
            prev = signature
        return True

class Orchestrator:
    def __init__(self, policy: Policy, audit: AuditStore, kill_switch: bool = True):
        self.policy, self.audit, self.kill_switch = policy, audit, kill_switch

    def run(self, req: Request) -> Decision:
        task_id = str(uuid.uuid4())
        if self.kill_switch:
            self.audit.record(req, "DENIED", "kill switch enabled", task_id)
            return Decision(False, "kill switch enabled", task_id, evidence="BLOCKED")
        try:
            self.policy.check(req)
        except PolicyDenied as e:
            self.audit.record(req, "DENIED", str(e), task_id)
            return Decision(False, str(e), task_id, evidence="BLOCKED")
        start = time.monotonic()
        roles = Router.choose(req.task)
        if len(roles) > self.policy.limits.max_steps or time.monotonic() - start > self.policy.limits.timeout_seconds:
            self.audit.record(req, "DENIED", "resource limits", task_id)
            return Decision(False, "resource limits", task_id, evidence="BLOCKED")
        self.audit.record(req, "PLANNED", "no external tool invoked", task_id)
        return Decision(True, "local plan only; no external tool invoked", task_id, roles, "OFFLINE_TESTED_LOCAL_PLAN")

class ToolRegistry:
    """Refuse-by-default tool discovery. No tool calls, only metadata planning."""
    def __init__(self): self._entries = {}
    def register(self, name: str, permission: str, description: str):
        if not name or permission not in ALL_ACTIONS: raise ValueError('invalid tool registration')
        self._entries[name] = {'permission': permission, 'description': description}
    def resolve(self, name: str, available_host_tools: set[str]) -> dict:
        if name not in self._entries or name not in available_host_tools:
            return {'status': 'external_tool_unavailable'}
        return {'status': 'HOST_VISIBLE_NOT_EXECUTED', **self._entries[name]}
