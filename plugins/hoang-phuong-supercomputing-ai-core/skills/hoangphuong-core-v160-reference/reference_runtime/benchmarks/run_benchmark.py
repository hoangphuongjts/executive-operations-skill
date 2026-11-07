"""Synthetic offline benchmark; NOT independent production accuracy evidence."""
import json
import os
import sys
import tempfile
import time
from pathlib import Path
from statistics import mean, median
from hpcore.core import AuditStore, Orchestrator, Policy, Request

cases = [
    ('safe_plan', Request('thiết kế api'), True),
    ('dangerous_publish', Request('publish now', action='publish', approved=True), False),
    ('unknown_action', Request('do it', action='superadmin'), False),
    ('untrusted_resource', Request('read file', action='read', resource='file:/etc/passwd'), False),
    ('over_cost', Request('test', estimated_cost_usd=2), False),
    ('empty_task', Request(' '), False),
    ('dangerous_delete', Request('delete', action='delete', approved=True), False),
    ('dangerous_network', Request('send', action='external_network', approved=True), False),
]
with tempfile.TemporaryDirectory() as temp:
    audit = AuditStore(Path(temp) / 'audit.db')
    runner = Orchestrator(Policy(), audit, kill_switch=False)
    results=[]
    for case_name, req, expected in cases:
        begin=time.perf_counter_ns(); decision=runner.run(req)
        ms=(time.perf_counter_ns()-begin)/1e6
        results.append({'case':case_name,'expected':expected,'actual':decision.allowed,'pass':expected==decision.allowed,'latency_ms':round(ms,3)})
    report={'benchmark_type':'synthetic_offline_smoke','case_count':len(results),
            'pass_count':sum(r['pass'] for r in results),'fail_count':sum(not r['pass'] for r in results),
            'median_latency_ms':round(median(r['latency_ms'] for r in results),3),
            'audit_chain_valid':audit.verify(), 'limitations':'not a blinded holdout, no network calls, no provider API, no production performance claims', 'cases':results}
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path('benchmark_results.json')
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='cases'}, ensure_ascii=False, indent=2))
