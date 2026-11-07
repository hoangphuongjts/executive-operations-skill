"""v15.0 controlled agent pilot: offline planner only, no model or network execution.
External live runtime remains opt-in and requires a separate audited deployment.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
import json
import os
from pathlib import Path

@dataclass(frozen=True)
class PilotConfig:
    enabled: bool=False
    external_execution_allowed: bool=False
    max_agents: int=8
    max_calls: int=10
    max_cost_usd: float=0.0
    max_tokens: int=8000
    timeout_s: int=30
    require_approval: bool=True
    kill_switch: bool=True


def pilot_plan(agent_ids: list[int], config: PilotConfig=PilotConfig(),
               approved: bool=False, model_endpoint: str | None=None) -> dict:
    if len(agent_ids)<4 or len(agent_ids)>min(8,config.max_agents) or len(set(agent_ids))!=len(agent_ids):
        return {'status':'rejected','reason':'pilot_requires_4_to_8_distinct_agents'}
    if any(type(x) is not int or x<1 or x>128 for x in agent_ids):
        return {'status':'rejected','reason':'invalid_agent_id'}
    if config.max_calls>10 or config.max_calls<1 or config.timeout_s>60 or config.timeout_s<1 or config.max_tokens>16000 or config.max_tokens<128:
        return {'status':'rejected','reason':'invalid_resource_bounds'}
    base={'agent_ids':agent_ids,'requested_model_calls_cap':config.max_calls,
          'cost_ceiling_usd':config.max_cost_usd,'runtime':'external_only','model_calls_executed':0}
    if config.kill_switch:return {'status':'disabled_by_kill_switch',**base}
    if not config.enabled or not config.external_execution_allowed:return {'status':'dry_run',**base}
    if config.require_approval and not approved:return {'status':'approval_required',**base}
    if not model_endpoint:return {'status':'external_endpoint_required',**base}
    if not model_endpoint.startswith('https://'):
        return {'status':'rejected','reason':'https_required',**base}
    if config.max_cost_usd<=0:return {'status':'rejected','reason':'positive_cost_budget_required',**base}
    # Deliberately never call the endpoint from a Skill. The external host must
    # independently validate credentials, egress, usage and approvals.
    return {'status':'ready_for_separate_runtime_integration_not_executed',**base}

if __name__=='__main__':
    print(json.dumps(pilot_plan([9,17,25,32]),ensure_ascii=False,indent=2))
