"""Offline, pure function reference router. No network, no provider/host calls."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
REGISTRY=ROOT/'references'/'AGENT_WORKFLOW_16_CANONICAL.json'
POLICY=ROOT/'references'/'STAGING_RUNTIME_POLICY.json'
def route(task, requested_skill=None, role_id=None, write=False, approved=False, cost_usd=0, live=False, tool_available=False):
    if not isinstance(task,str) or not task.strip():return {'state':'blocked','reason':'missing_task'}
    r=json.loads(REGISTRY.read_text(encoding='utf8'));p=json.loads(POLICY.read_text(encoding='utf8'))
    if cost_usd>p['cost_limit_usd']:return {'state':'blocked','reason':'cost_limit'}
    if write and not approved:return {'state':'blocked','reason':'approval_required'}
    if role_id is not None and role_id not in [i for c in r['clusters'] for i in c['agent_ids']]:return {'state':'blocked','reason':'unknown_role'}
    if live and p['kill_switch_default']:return {'state':'blocked','reason':'kill_switch'}
    matches=[x for x in r['external_skill_canonical_crosswalk'] if x['skill_uri']==requested_skill] if requested_skill else []
    if requested_skill and not matches:return {'state':'blocked','reason':'unknown_skill'}
    if matches:c=matches[0]['core_cluster_id']
    elif role_id is not None:c=next(x['cluster_id'] for x in r['clusters'] if role_id in x['agent_ids'])
    else:return {'state':'needs_source_selection','reason':'ambiguous_task'}
    w=next(w for w in r['workflows'] if w['cluster_id']==c)
    return {'state':'guidance_only','reason':'runtime_disabled' if not tool_available else 'not_authorized_for_execution','cluster_id':c,'workflow_id':w['id'],'recommended_role_ids':w['recommended_agent_role_ids'],'runtime_executed':False,'paid_calls':0}
