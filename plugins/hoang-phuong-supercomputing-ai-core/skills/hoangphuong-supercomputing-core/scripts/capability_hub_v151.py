"""v15.1 federated capability planner, no arbitrary tool execution or secret transfer."""
from __future__ import annotations
import hashlib
import json
from datetime import datetime,timezone
from pathlib import Path
from typing import Any


def resolve(source: dict[str,Any], host_tools: set[str], action: str='read',
            approved: bool=False, scoped_permission: bool=False)->dict[str,Any]:
    # A snapshot reference is never a functional connector.
    if not isinstance(source,dict):return {'status':'invalid_source'}
    source_id=source.get('uri') or source.get('tool_name')
    if not isinstance(source_id,str) or not source_id.strip():return {'status':'invalid_source'}
    if source_id.startswith('skills://'):
        return {'status':'skill_guidance_only','source':source_id,'execution':'not_executed',
                'next':'read_exact_source_skill_in_current_host'}
    if source_id not in host_tools:return {'status':'external_tool_unavailable','source':source_id}
    high_risk={'send','publish','delete','install','deploy','purchase','pay','transfer','share','update','create','execute'}
    if action not in high_risk|{'read','inspect','search','list','plan'}:
        return {'status':'denied_unknown_action','source':source_id}
    if action in high_risk and not (approved and scoped_permission):
        return {'status':'approval_required','source':source_id,'execution':'not_executed'}
    return {'status':'host_invocation_eligible','source':source_id,'action':action,
            'execution':'not_executed','next':'invoke_through_host_with_native_permissions'}


def audit_record(action: str, target: str, outcome: str, evidence: str='') -> dict:
    # Omit secrets, full prompts, personal records and OAuth data by design.
    safe=lambda s: str(s)[:180].replace('\n',' ')
    return {'schema':'v15.1','timestamp_utc':datetime.now(timezone.utc).isoformat(),
            'action':safe(action),'target_sha256':hashlib.sha256(target.encode('utf-8')).hexdigest(),
            'outcome':safe(outcome),'evidence':safe(evidence),'secrets_recorded':False}


def capability_report(root: Path)->dict:
    p=root/'skills/hoangphuong-supercomputing-core/references/UNIFIED_CAPABILITIES_CATALOG.json'
    if not p.exists():return {'status':'missing_snapshot','host_tools_verified':0}
    data=json.loads(p.read_text(encoding='utf-8'))
    return {'status':'snapshot_only','snapshot_release':data.get('release'),
            'catalog_external_skills':data.get('external_skill_count'),
            'owned_plugins_at_snapshot':data.get('other_owned_plugin_count'),
            'host_tools_verified':0,'live_tool_probe_required':True,
            'not_a_unified_backend':True}
