#!/usr/bin/env python3
"""Research Excellence Academy 14.3. Offline metadata auditing, no external API or model training."""
from __future__ import annotations
import argparse
from datetime import date,datetime,timezone
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
CORE=Path('skills/hoangphuong-supercomputing-core')
RUBRIC={'accuracy':25,'scientific_method':20,'evidence_licenses':20,
        'counterexamples':15,'reproducibility':15,'ethics_safety':5}
PURPOSES={'quote','rag','training','redistribution','commercial'}
LICENSES={'CC0-1.0','CC-BY-4.0','MIT','Apache-2.0'}  # conservative *metadata* gate, not legal advice

def read_json(p):
    if p.stat().st_size>1024*1024:raise ValueError('metadata too large')
    d=json.loads(p.read_text(encoding='utf8'))
    if not isinstance(d,dict):raise ValueError('JSON object required')
    return d

def read_jsonl(p):
    if p.stat().st_size>1024*1024:raise ValueError('metadata too large')
    data=[json.loads(x) for x in p.read_text(encoding='utf8').splitlines() if x.strip()]
    if len(data)>512 or any(not isinstance(x,dict) for x in data):raise ValueError('invalid JSONL record')
    return data

def check_license(source,purpose):
    if purpose not in PURPOSES:raise ValueError('invalid purpose')
    faults=[]
    if source.get('license_id') not in LICENSES:faults.append('license_unreviewable')
    if source.get('review_status')!='human_reviewed':faults.append('human_review_missing')
    for field in ['source_id','title','canonical_url','rights_holder','license_evidence_url','reviewer_id','reviewed_at']:
        if not isinstance(source.get(field),str) or not source[field].strip():faults.append('missing_'+field)
    for field in ['canonical_url','license_evidence_url']:
        if not isinstance(source.get(field),str) or not source[field].startswith('https://'):
            faults.append('https_required_'+field)
    try:date.fromisoformat(source.get('reviewed_at',''))
    except (TypeError,ValueError):faults.append('invalid_review_date')
    uses=source.get('allowed_uses')
    if not isinstance(uses,list) or any(x not in PURPOSES for x in uses):faults.append('invalid_allowed_uses')
    elif purpose not in uses:faults.append('purpose_not_permitted')
    if source.get('license_id')=='CC-BY-4.0' and not source.get('attribution'):
        faults.append('attribution_missing')
    return {'source_id':source.get('source_id'),'purpose':purpose,
            'metadata_gate_passed':not faults,'reasons':sorted(set(faults)),
            'legal_rights_verified':False}

def licenses(root,purpose='rag'):
    sources=read_json(root/CORE/'academy/source_registry.json').get('sources')
    if not isinstance(sources,list) or len(sources)>512:raise ValueError('bad registry')
    ids=[s.get('source_id') for s in sources]
    if any(not isinstance(x,str) or not x for x in ids) or len(ids)!=len(set(ids)):
        raise ValueError('invalid/duplicate source_id')
    checks=[check_license(s,purpose) for s in sources]
    ok=[c['source_id'] for c in checks if c['metadata_gate_passed']]
    return {'status':'metadata_only_reviewed_not_legally_verified' if ok else 'no_approved_sources',
            'sources_count':len(sources),'approved_metadata_count':len(ok),
            'source_ids_passing_metadata_gate':ok,'checks':checks,
            'note':'Check verifies claimed metadata only; it cannot authenticate rights or the reviewer.'}

def validate(root):
    issues=[]
    try:
        roles=read_json(root/CORE/'references/AGENTS_128.json')['roles']
        if [r['id'] for r in roles]!=list(range(1,129)) or len({r['name'].casefold() for r in roles})!=128:
            issues.append('roles_128_not_unique')
        for g in range(1,17):
            if sum(r['group']==g for r in roles)!=8:issues.append(f'group_{g}_not_8')
        for r in roles:
            p=read_json(root/CORE/f"profiles/agent-{r['id']:03d}.json")
            if (p.get('id'),p.get('name'))!=(r['id'],r['name']):issues.append('profile_mismatch_'+str(r['id']))
        clusters=read_json(root/CORE/'academy/cluster_curricula.json')['clusters']
        if [c['group_id'] for c in clusters]!=list(range(1,17)):
            issues.append('curriculum_16_groups_missing')
        for c in clusters:
            g=c['group_id']
            if c['agent_ids']!=list(range(8*(g-1)+1,8*g+1)):
                issues.append('cluster_membership_'+str(g))
        plans=read_jsonl(root/CORE/'academy/agent_eval_plans_128.jsonl')
        if [p['agent_id'] for p in plans]!=list(range(1,129)):
            issues.append('plans_128_ids')
        for p,r in zip(plans,roles):
            if (p['role'],p['group_id'])!=(r['name'],r['group']):issues.append('plan_identity_'+str(r['id']))
            if p.get('assessment_status')!='not_evaluated' or p.get('rubric')!=RUBRIC:
                issues.append('false_eval_or_rubric_'+str(r['id']))
        pilot=read_json(root/CORE/'academy/pilot_025_032.json')
        if pilot.get('pilot_ids')!=list(range(25,33)) or len(pilot.get('agents',[]))!=8:
            issues.append('pilot_25_32_invalid')
        for id,r in enumerate(pilot.get('agents',[]),25):
            if (r.get('agent_id')!=id or r.get('name')!=roles[id-1]['name'] or
                r.get('evaluations_completed')!=0 or len(r.get('training_4_stages',[]))!=4 or
                r.get('rubric')!=RUBRIC):issues.append('pilot_mismatch_'+str(id))
        mode=read_json(root/CORE/'references/EMBEDDED_128_MODE.json')
        if mode.get('mode')!='embedded_skills_only' or any(mode.get(x) is not False for x in
           ['runtime_execution_default','external_model_api_default','gateway_default',
            'docker_default','persistent_agent_memory_default']):issues.append('embedded_mode_changed')
        manifests=[read_json(root/name) for name in ['plugin.json','.codex-plugin/plugin.json']]
        if (manifests[0]['version']!=manifests[1]['version'] or
            tuple(map(int,manifests[0]['version'].split('.')))<(14,3,0) or
            manifests[0]['name']!=manifests[1]['name'] or
            mode['release']!=manifests[0]['version']):issues.append('manifest_mismatch')
        for s in ['hoangphuong','phattrienungdung','sanxuatnoidung','marketingtongluc',
                  'trolydieuhanh','tudonghethong','phantichdautu']:
            if not (root/f'skills/{s}/SKILL.md').is_file():issues.append('original_skill_missing_'+s)
        status=read_json(root/CORE/'academy/ACADEMY_STATUS.json')
        if any(status.get(x)!=0 for x in ['pilot_evaluation_results','certified_agents','fine_tuned_models','external_agent_processes_started','api_calls_executed']):
            issues.append('fabricated_progress')
        if not isinstance(read_json(root/CORE/'academy/source_registry.json').get('sources'),list):
            issues.append('source_registry_invalid')
    except (OSError,KeyError,TypeError,ValueError,json.JSONDecodeError) as exc:
        issues.append('validation_error_'+str(exc)[:160])
    return {'status':'pass' if not issues else 'fail','errors':issues,
            'expected':{'roles':128,'clusters':16,'pilots':8,'evaluation_plans':128},
            'model_training_or_evaluation_executed':False}

def pilot(root,id):
    if type(id)!=int or not 25<=id<=32:raise ValueError('pilot role ID must be 25..32')
    a=read_json(root/CORE/'academy/pilot_025_032.json')['agents']
    return {'status':'plan_only_not_evaluated','agent':next(x for x in a if x['agent_id']==id)}

def assess_records(records,approved_sources):
    if not isinstance(records,list) or len(records)>512:raise ValueError('invalid review records')
    bad=[];groups={}
    for idx,r in enumerate(records):
        try:
            id=r['agent_id'];case=r['case_id'];rev=r['reviewer_id'];digest=r['artifact_sha256'];score=r['scores']
            if type(id)!=int or not 1<=id<=128 or not re.fullmatch('[A-Za-z0-9_-]{3,48}',case):raise ValueError('bad agent/case')
            if not re.fullmatch('[A-Za-z0-9_.-]{3,60}',rev):raise ValueError('bad reviewer')
            if r.get('reviewer_type')!='human_domain_expert':raise ValueError('human expert attestation missing')
            date.fromisoformat(r['reviewed_at'])
            if not re.fullmatch('[0-9a-f]{64}',digest):raise ValueError('bad artifact digest')
            if not isinstance(score,dict) or score.keys()!=RUBRIC.keys():raise ValueError('wrong rubric')
            if any(type(score[k])!=int or not 0<=score[k]<=v for k,v in RUBRIC.items()):raise ValueError('score outside rubric')
            sources=r.get('evidence_source_ids')
            if not isinstance(sources,list) or not sources or any(x not in approved_sources for x in sources):raise ValueError('source not metadata-approved')
            if type(r.get('critical_issue'))!=bool:raise ValueError('critical issue needs explicit boolean')
            groups.setdefault((id,case,digest),[]).append(r)
        except (KeyError,TypeError,ValueError) as exc:bad.append({'index':idx,'issue':str(exc)})
    result=[]
    for (id,case,digest),recs in sorted(groups.items()):
        scores=[sum(x['scores'].values()) for x in recs]
        distinct=len({r['reviewer_id'] for r in recs})==len(recs)
        critical=any(x['critical_issue'] for x in recs)
        candidate=len(recs)>=2 and distinct and min(scores)>=85 and not critical
        result.append({'agent_id':id,'case_id':case,'artifact_sha256':digest,'scores':scores,
                       'reviewer_count':len(recs),'critical_issue':critical,
                       'status':'candidate_pending_external_identity_and_quality_check' if candidate else
                          'blocked_critical_issue' if critical else 'not_yet_eligible',
                       'expert_degree_certified':False,'reviewers_independently_verified':False})
    return {'status':'human_supplied_scores_checked_only','cases':result,'invalid_records':bad,
            'limitations':['No reviewer identity/degree verification','No substantive scientific grading by this code',
                           'No legal ownership validation; all source metadata self-attested']}

def assess(root,results):
    if results.stat().st_size>1024*1024:raise ValueError('results file too large')
    data=json.loads(results.read_text(encoding='utf8'))
    accepted=set(licenses(root,'quote')['source_ids_passing_metadata_gate'])
    return assess_records(data,accepted)

def debate_check(claims):
    if not isinstance(claims,list) or len(claims)>32:raise ValueError('invalid claims')
    issues=[]
    for i,c in enumerate(claims):
        if not isinstance(c,dict):issues.append([i,'not_object']);continue
        for field in ['claim','alternative','falsification_test','counterexample','status']:
            if not isinstance(c.get(field),str) or not c[field].strip():issues.append([i,'missing_'+field])
        if c.get('status') not in {'hypothesis','unverified','tested','refuted'}:issues.append([i,'status_invalid'])
        if c.get('status')=='tested' and not c.get('execution_trace'):issues.append([i,'tested_without_trace'])
        if c.get('status')=='refuted' and not c.get('refutation_evidence'):issues.append([i,'refuted_without_evidence'])
    return {'status':'pass' if not issues else 'fail','issues':issues,
            'actual_scientific_correctness_verified':False}

def report(root):
    return {'status':'pass' if validate(root)['status']=='pass' else 'fail',
            'version':read_json(root/'plugin.json').get('version','unknown'),'checked_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
            'structure':validate(root),'license_metadata':licenses(root,'rag'),
            'academy_status':read_json(root/CORE/'academy/ACADEMY_STATUS.json'),
            'external_api_used':False,'actual_agent_accuracy_measured':False}

def main():
    ap=argparse.ArgumentParser(description='Research Academy offline audit, no AI API')
    ap.add_argument('action',choices=['validate','licenses','pilot','assess','debate-check','report'])
    ap.add_argument('--root',type=Path,default=ROOT)
    ap.add_argument('--id',type=int)
    ap.add_argument('--purpose',choices=sorted(PURPOSES),default='rag')
    ap.add_argument('--results',type=Path)
    ap.add_argument('--claims',type=Path)
    ap.add_argument('--output',type=Path)
    x=ap.parse_args()
    try:
        if x.action=='validate':res=validate(x.root)
        elif x.action=='licenses':res=licenses(x.root,x.purpose)
        elif x.action=='pilot':res=pilot(x.root,x.id)
        elif x.action=='assess':
            if x.results is None:ap.error('--results required')
            res=assess(x.root,x.results)
        elif x.action=='debate-check':
            if x.claims is None:ap.error('--claims required')
            res=debate_check(read_json(x.claims)['claims'])
        else:res=report(x.root)
    except (OSError,ValueError,TypeError,KeyError,json.JSONDecodeError) as e:
        res={'status':'error','message':str(e)[:200]}
    encoded=json.dumps(res,ensure_ascii=False,indent=2)+'\n'
    if x.output:
        x.output.parent.mkdir(parents=True,exist_ok=True)
        x.output.write_text(encoded,encoding='utf8')
    print(encoded,end='')
    return 1 if res['status'] in {'fail','error'} or res.get('invalid_records') else 0
if __name__=='__main__':raise SystemExit(main())
