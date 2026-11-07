import argparse
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from .core import AuditStore, Orchestrator, Policy, Request, ToolRegistry


def main():
    parser = argparse.ArgumentParser(description='Hoang Phuong Core local reference prototype')
    parser.add_argument('command', choices=['doctor', 'plan', 'audit-verify'])
    parser.add_argument('--task', default='Thiết kế kiến trúc và kiểm thử API')
    parser.add_argument('--db', default='hpcore_audit.sqlite3')
    parser.add_argument('--enable-local-plan', action='store_true')
    args = parser.parse_args()
    if args.command == 'doctor':
        out = {'version': '16.0.0-prototype', 'status': 'local-only', 'default_kill_switch': True,
               'remote_runtime': 'NOT_DEPLOYED', 'original_plugin_modified': False,
               'original_registry_verified': False}
    else:
        audit = AuditStore(args.db)
        if args.command == 'plan':
            d = Orchestrator(Policy(), audit, kill_switch=not args.enable_local_plan).run(Request(args.task))
            out = vars(d)
        else:
            out = {'audit_chain_valid': audit.verify(), 'warning': 'local hash chain is not immutable hosted logging'}
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == '__main__': main()
