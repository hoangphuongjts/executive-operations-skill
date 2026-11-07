#!/usr/bin/env python3
"""Local offline metadata search for the Unified Capabilities Hub. No API calls."""
import argparse, json, pathlib, re, unicodedata
ROOT=pathlib.Path(__file__).resolve().parents[3]
CAT='skills/hoangphuong-supercomputing-core/references/UNIFIED_CAPABILITIES_CATALOG.json'

def load(root=ROOT):
    return json.loads((pathlib.Path(root)/CAT).read_text(encoding='utf-8'))

def validate(data):
    err=[]
    skills=data.get('skill_sources',[]);plugins=data.get('owned_plugins',[]);tools=data.get('connector_namespaces',[])
    uris=[x.get('uri') for x in skills]
    if len(skills)!=172 or len(set(uris))!=172:err.append('skill count/uniqueness')
    if len(plugins)!=11 or len({p.get('plugin_id') for p in plugins})!=11:err.append('owned plugin count/uniqueness')
    if len(tools)!=19 or len({t.get('namespace') for t in tools})!=19:err.append('tool group count/uniqueness')
    if any(not x.get('uri','').startswith('skills://plugins/') for x in skills):err.append('invalid skill uri')
    if any('hoang-phuong-supercomputing-ai-core' in x.get('uri','') for x in skills):err.append('core skill included in external list')
    if any(x.get('copy_into_core') is not False for x in skills):err.append('unsafe source copy flag')
    if any(x.get('status')!='catalog_visible_only' for x in skills):err.append('unverified availability state')
    if any(x.get('integration_mode')!='read_original_skill_on_demand_via_host' or x.get('source_preserved') is not True for x in skills):err.append('unsafe skill federation')
    if any(not x.get('not_a_connection_confirmation') for x in tools):err.append('tool connection overclaim')
    if any(x.get('local_code_or_credentials_copied') is not False for x in tools):err.append('credential transfer claim')
    if not data.get('global_rules',{}).get('no_vps_external_api_by_default'):err.append('runtime policy missing')
    return {'status':'pass' if not err else 'fail','errors':err,'skill_count':len(skills),'other_owned_plugins':len(plugins),'connector_namespaces':len(tools)}

def norm(s):
    return ''.join(ch for ch in unicodedata.normalize('NFKD',str(s).lower().replace('đ','d')) if not unicodedata.combining(ch))

OWNER_ALIASES={
    'channel-growth-agent-vn':['xay kenh','kenh','youtube','tiktok','shorts'],
    'app-69dd11f3e50c8191b1ca48d03cf7e2ad':['youtube','kenh','seo video','video'],
    'content-ai-vietnam':['noi dung','bai viet','kich ban','quang cao','marketing','seo','content'],
    'heygen':['video','long tieng','phu de','giong doc','avatar'],
    'ai-coding-vietnamese-kit':['lap trinh','phan mem','kiem thu','bao mat','code','debug'],
    'superpowers':['lap trinh','debug','phan bien','ke hoach','code'],
    'google-drive':['tai lieu','bang tinh','trinh chieu','google drive','docs'],
    'plugin-creator':['plugin','skill','agent','tac tu','cong cu'],
    'software-rebuild-ai-vn':['dich nguoc','phan mem','ma nguon','exe'],
    'video-shotcraft-vn':['video','canh quay','dung phim'],
    'moneyprinter-vn':['video','youtube','tiktok'],
    'voxcpm-voice-vn':['giong doc','giong noi','giong hat','am thanh'],
    'openai-templates':['mau tai lieu','bao cao','ke hoach','bieu mau','tai chinh'],
    'spreadsheets-router':['bang tinh','excel','xlsx'],
    'pdf-router':['pdf','tai lieu'],
    'documents-router':['word','docx','tai lieu'],
    'presentations-router':['slide','powerpoint','thuyet trinh'],
    'hyperframes-vn-chatgpt':['video','khung hinh','dung phim'],
    'app-6a3293e129088191abf0875820e839da':['higgsfield','thiet ke','anh','website'],
    'ai-tool-manager-vn':['plugin','skill','agent','cong cu'],
}
def score(query,entry):
    qtokens=[x for x in re.split(r'[^a-z0-9]+',norm(query)) if len(x)>1]
    v=norm(' '.join((entry.get('slug',''),entry.get('source_plugin',''))).replace('-',' '))
    words=set(re.split(r'[^a-z0-9]+',v))
    matches=sum(3 for t in qtokens if t in words)
    phrase=norm(query).strip()
    if phrase and phrase in v:matches+=5
    query_terms=set(qtokens)
    for alias in OWNER_ALIASES.get(entry.get('source_plugin'),[]):
        if set(alias.split()).issubset(query_terms):matches+=4
    return matches

def search(data,query,limit=8):
    found=[(score(query,s),s) for s in data['skill_sources']]
    selected=[]; per_source={}
    for p,x in sorted(found,key=lambda z:(-z[0],z[1]['uri'])):
        if p<=0:continue
        owner=x['source_plugin']
        if per_source.get(owner,0)>=2:continue
        per_source[owner]=per_source.get(owner,0)+1
        selected.append(dict(x,search_score=p))
        if len(selected)>=limit:break
    return selected

def plan(data,task,max_skills=4):
    selected=search(data,task,max_skills)
    clusters=[]
    for item in selected:
        for group in item['clusters']:
            if group not in clusters:clusters.append(group)
    return {'task':task,'status':'catalog_recommendation_only','selected_skill_uris':[x['uri'] for x in selected],
            'suggested_core_clusters':clusters[:4], 'available_tools_verified':False,
            'requires_original_skill_read':True,'external_execution':False}

def connection_status(data, namespace, probe=None):
    row=next((x for x in data['connector_namespaces'] if x['namespace'].casefold()==namespace.casefold()),None)
    if not row:
        return {'namespace':namespace,'status':'not_listed'}
    # The probe describes a single past session, never a live connectivity check.
    if row.get('verified_read_in_session'):
        return {'namespace':row['namespace'],'status':'read_verified_at_snapshot_only','live_connection_now':'unknown'}
    return {'namespace':row['namespace'],'status':'tool_interface_visible_at_snapshot_only','live_connection_now':'unknown'}

def mount(data,query,max_skills=4):
    p=plan(data,query,max_skills)
    p['mode']='federated_host_dispatch'
    p['read_skill_uris_on_demand']=p.pop('selected_skill_uris')
    p['source_plugins_unmodified']=True
    p['no_credential_or_code_transfer']=True
    p['host_tool_call_requires_current_permission']=True
    return p

def main():
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=['validate','search','plan','mount','connection','report']);
    ap.add_argument('--root',default=str(ROOT));ap.add_argument('--query',default='');ap.add_argument('--limit',type=int,default=8)
    a=ap.parse_args(); d=load(a.root)
    if a.command=='validate':out=validate(d)
    elif a.command=='report':out={'release':d['release'],'snapshot_date':d['snapshot_date'],**validate(d),'semantics':d['integration_kind']}
    elif a.command=='search':out=search(d,a.query,a.limit)
    elif a.command=='mount':out=mount(d,a.query,min(a.limit,4))
    elif a.command=='connection':out=connection_status(d,a.query)
    else:out=plan(d,a.query,min(a.limit,4))
    print(json.dumps(out,ensure_ascii=False,indent=2))
    return 1 if isinstance(out,dict) and out.get('status')=='fail' else 0
if __name__=='__main__':raise SystemExit(main())
