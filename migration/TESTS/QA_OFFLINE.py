#!/usr/bin/env python3
"""Read-only, offline validation of the 17-package migration kit. No plugin code executed."""
from pathlib import Path
from collections import defaultdict
import hashlib, io, json, re, sys, zipfile
ROOT=Path(__file__).resolve().parents[1]
errors=[];checks=0

def expect(condition,what):
    global checks
    checks+=1
    if not condition:errors.append(what)

def parse_frontmatter(text):
    m=re.match(r'\A---\s*\r?\n(.*?)\r?\n---(?:\r?\n|\s*$)',text,re.S)
    if not m:return None
    lines=m.group(1).splitlines()
    keys={}
    for line in lines:
        r=re.match(r'^(name|description)\s*:\s*(.*)$',line)
        if r:keys[r.group(1)]=r.group(2).strip().strip('"')
    return keys

items=json.loads((ROOT/'MANIFESTS'/'PLUGIN_EXPORT_MATRIX.json').read_text(encoding='utf8'))
expect(len(items)==17,'expected 17 plugin inventory rows')
assert (ROOT/'ORIGINAL_BACKUP'/'HoangPhuong_ChatGPT_Full_Portable_2026-11-07.zip').exists()
for p in items:
    if not p['import_file']:continue
    fname=ROOT/p['import_file']
    expect(fname.is_file(),f'missing candidate: {p["name"]}')
    with zipfile.ZipFile(fname) as z:
        expect(z.testzip() is None, f'ZIP CRC failure: {p["name"]}')
        files=z.namelist()
        expect('plugin.json' in files,f'no root manifest: {p["name"]}')
        manifest=json.loads(z.read('plugin.json'))
        expect(manifest.get('$schema')=='https://agent-plugins.org/schemas/1.0.0/plugin.schema.json',f'root schema mismatch: {p["name"]}')
        expect(manifest.get('name')==p['name'],f'wrong name: {p["name"]}')
        expect(manifest.get('version')==p['source_version'],f'version mismatch: {p["name"]}')
        skills=[x for x in files if re.fullmatch(r'skills/[^/]+/SKILL.md',x)]
        expect(len(skills)==p['portable_skill_count'],f'number of skills mismatched: {p["name"]}')
        for sk in skills:
            front=parse_frontmatter(z.read(sk).decode('utf8'))
            expect(front is not None,f'frontmatter missing: {sk}')
            if front:
                expect(front.get('name')==sk.split('/')[1],f'name mismatch: {sk}')
                expect(bool(front.get('description')),f'description missing: {sk}')
        interface=manifest.get('extensions',{}).get('com.openai',{}).get('interface',{})
        sd=interface.get('shortDescription')
        expect(sd is None or len(sd)<=30, f'shortDescription >30: {p["name"]}')
        for f in files:
            expect(not f.startswith('/') and '..' not in Path(f).parts,f'unsafe ZIP path: {f}')
        expect(not any(x.endswith('.pyc') for x in files), f'unexpected Python cache in staging: {p["name"]}')

with zipfile.ZipFile(ROOT/'STAGING_IMPORT_CANDIDATES'/'hoang-phuong-supercomputing-ai-core__16.0.50.zip') as z:
    root='skills/hoangphuong-supercomputing-core/'
    agents=sorted(f for f in z.namelist() if re.fullmatch(root+r'profiles/agent-\d{3}\.json',f))
    expect(len(agents)==128,'not 128 agent profiles')
    for n,f in enumerate(agents,1):
        p=json.loads(z.read(f))
        expect(p.get('id')==n and p.get('key')==f'agent-{n:03d}',f'agent profile id error {n}')
        expect(1<=p.get('group_id',0)<=16,f'agent group error {n}')
    registry=json.loads(z.read(root+'references/CLUSTER_16_ASSET_REGISTRY.json'))
    expect(len(registry['clusters'])==16,'not 16 clusters')
    cluster_ids=sorted(x for c in registry['clusters'] for x in c['agent_ids'])
    expect(cluster_ids==list(range(1,129)),'agent IDs not assigned once to clusters')
    cmds=json.loads(z.read(root+'references/STUDY_108_BASELINE.json'))
    code_set=set(c['code'] for c in cmds)
    expect(len(cmds)==108 and len(code_set)==108,'108 baseline command failed')
    expect('/mindmap' in code_set,'example /mindmap missing')
    expect(len([x for x in code_set if x.startswith('/m')])>=2,'/m is not a prefix in study codes')
    expect(len([x for x in code_set if x.startswith('/g')])>=2,'/g is not a prefix in study codes')
    sk='skills/revidapi-reup-video-vn/SKILL.md'
    front=parse_frontmatter(z.read(sk).decode('utf8'))
    expect(front and front.get('name')=='revidapi-reup-video-vn', 'patched skill frontmatter missing')

result={'status':'PASS' if not errors else 'FAIL','assertions':checks,'failed':len(errors),'errors':errors,
        'scope':'OFFLINE_STATIC_ONLY','target_account_host_import':'NOT_TESTED','live_skill_invocation':'NOT_TESTED',
        'oauth_mcp_network':'NOT_TESTED','production_mutations':0}
print(json.dumps(result,ensure_ascii=False,indent=2))
sys.exit(1 if errors else 0)
