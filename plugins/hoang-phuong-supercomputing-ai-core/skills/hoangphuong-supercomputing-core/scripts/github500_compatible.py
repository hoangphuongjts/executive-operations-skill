"""GitHub500 v14.7 native adapter checker (offline, no external execution/network)."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[3]
REGISTRY=ROOT/'skills/hoangphuong-supercomputing-core/references/GITHUB_500_V147_COMPATIBLE_SKILLS.json'

def validate(root:Path=ROOT)->dict:
    data=json.loads((root/'skills/hoangphuong-supercomputing-core/references/GITHUB_500_V147_COMPATIBLE_SKILLS.json').read_text(encoding='utf-8'))
    skills=data['entries']; issues=[]
    if len(skills)!=12: issues.append('adapter_count_not_12')
    if len({s['name'] for s in skills})!=len(skills):issues.append('duplicate_names')
    if data.get('execution_mode')!='embedded_skills_only':issues.append('wrong_mode')
    for field in ('auto_run_external_repos','auto_register_slash_commands','external_api_calls','original_108_code_names_changed','original_core_agent_ids_changed'):
        if data.get('safety',{}).get(field) is not False:issues.append('unsafe_flag:'+field)
    root_path=root.resolve()
    for item in skills:
        name=item['name'];path=item['skill_path']
        if not re.fullmatch(r'github500-[a-z][a-z0-9-]*',name):issues.append('bad_name:'+str(name));continue
        if path!=f'skills/{name}/SKILL.md':issues.append('bad_path:'+name);continue
        full=root/path
        if full.resolve().is_relative_to(root_path) is False:issues.append('outside_root:'+name);continue
        if not full.is_file():issues.append('missing_skill:'+name);continue
        s=full.read_text(encoding='utf-8')
        if not s.startswith('---\nname: '+name+'\n'):issues.append('invalid_frontmatter:'+name)
        if 'description:' not in s.split('---',2)[1]:issues.append('missing_description:'+name)
        if not (full.parent/'references/PROVENANCE.md').is_file():issues.append('missing_provenance:'+name)
        if not re.fullmatch('[0-9a-f]{40}',item['source_sha1']):issues.append('invalid_sha:'+name)
        if item['license']!='MIT':issues.append('license_not_mit:'+name)
        if '/generatehandwrittenimage' in s:issues.append('study_code_overlap:'+name)
    org=json.loads((root/'skills/hoangphuong-supercomputing-core/references/AGENTS_128.json').read_text())
    if len(org['roles'])!=128:issues.append('original_agents_changed')
    catalog=json.loads((root/'skills/hoangphuong-supercomputing-core/references/GITHUB_500_MASTER_CATALOG.json').read_text())
    if len(catalog['records'])!=500:issues.append('original_catalog_changed')
    return {'passed':not issues,'skill_count':len(skills),'issues':issues,'catalog_count':len(catalog['records'])}

def route(query:str,root:Path=ROOT)->dict:
    q=query.casefold()
    mapping={
        'github500-agent-governance':['quyền agent','phân quyền','tool approval','agent governance','kiểm soát quyền'],
        'github500-agent-evaluation':['benchmark','đánh giá agent','chấm điểm ai','kiểm thử ai','agent eval'],
        'github500-prompt-safety':['prompt injection','rủi ro prompt','an toàn prompt','lộ dữ liệu'],
        'github500-workflow-design':['tự động hóa','workflow','n8n','quay màn hình','automation'],
        'github500-prompt-refiner':['viết prompt','sửa prompt','tối ưu prompt','prompt hay hơn'],
        'github500-architecture-blueprint':['kiến trúc phần mềm','sơ đồ code','architecture','blueprint'],
        'github500-hypothesis-research':['giả thuyết','nghiên cứu khoa học','hypothesis'],
        'github500-exploratory-data':['eda','dữ liệu thiếu','khám phá dữ liệu','data analysis'],
        'github500-citation-verification':['trích dẫn','doi','bibtex','citation'],
        'github500-lab-cad-planning':['cad','stl','in 3d','giá đỡ','jig','thiết kế 3d'],
        'github500-competitor-analysis':['đối thủ','competitor','so sánh thương hiệu'],
        'github500-command-library':['/gh500-','slash code github500']
    }
    matched=[(sum(term in q for term in terms),name) for name,terms in mapping.items()]
    matched=[(n,name) for n,name in matched if n]
    matched.sort(key=lambda x:(-x[0],x[1]))
    return {'skill':matched[0][1] if matched else None,'candidates':[x[1] for x in matched[:3]],'execution':'instruction_only','host_slash_command_registered':False}

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('command',choices=['validate','route']);a.add_argument('--query',default='');args=a.parse_args()
    print(json.dumps(validate() if args.command=='validate' else route(args.query),ensure_ascii=False,indent=2))
