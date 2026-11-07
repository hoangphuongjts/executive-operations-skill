"""Read-only-by-default offline candidate curator and risk scanner; Python 3.10+ stdlib."""
from __future__ import annotations
import argparse, collections, hashlib, json, re, pathlib, datetime, sys

REPLACEMENTS = {
    (3, 'k-dense-ai/scientific-agent-skills'): ('pallets/flask', 'source_duplicate_cross_cluster'),
    (16, 'zapier/automationbench'): ('promptfoo/promptfoo', 'source_duplicate_cross_cluster'),
    (9, '18f/ux-guide'): ('uswds/uswds', 'archived_repository_observed'),
    (10, 'linzeqipku/snowgraph'): ('apache/airflow', 'archived_repository_observed'),
}
CLUSTER_NAMES = [
 'Tri thức & phương pháp khoa học', 'Kiến trúc hệ thống', 'Kỹ thuật phần mềm',
 'Kiểm thử & kiểm định', 'Hiệu năng & HPC', 'Lượng tử, mật mã & P2P',
 'AI & thuật toán', 'Điều phối & vận hành', 'Sản phẩm & UX', 'Dữ liệu & tri thức',
 'Agent & công cụ', 'An toàn & bảo mật', 'Nội dung & đa phương thức',
 'Tài chính & quyết định', '3D, thiết bị & IoT', 'Đánh giá & chất lượng'
]
RISK_PATTERNS = {
 'shell_pipe': re.compile(r'\b(?:curl|wget)\b[^\n]{0,180}\|\s*(?:bash|sh|powershell)',re.I),
 'python_exec': re.compile(r'\b(?:eval|exec)\s*\(', re.I),
 'env_read': re.compile(r'\b(?:os\.environ|process\.env|\.env)\b',re.I),
 'subprocess': re.compile(r'\b(?:subprocess\.|os\.system\(|child_process)',re.I),
 'remote_download': re.compile(r'\b(?:requests\.get\(|urllib\.request|fetch\()',re.I),
 'destructive_command': re.compile(r'\b(?:rm\s+-rf|rmdir\s+/s|shutil\.rmtree)\b',re.I),
}
TEXT_EXT={'.py','.js','.ts','.sh','.ps1','.json','.yaml','.yml','.toml','.md','.txt'}
CHECK_FILES={'Dockerfile','Makefile','package.json','pyproject.toml','requirements.txt','setup.py','setup.cfg','mcp.json','.github/workflows'}

def canonical(s):
    s=s.strip().rstrip('/').removesuffix('.git')
    s=re.sub(r'^https?://(?:www\.)?github\.com/', '', s, flags=re.I)
    return s.lower()

def curate(document):
    records=document['records']; seen=set(); original_counts=collections.Counter(); outcome=[]; changes=[]
    for record in records:
        x=dict(record); c=x['cluster_id']; original_counts[c]+=1
        old=canonical(x['repo']); new,reason=REPLACEMENTS.get((c,old),(None,None))
        if old in seen and new is None: raise ValueError(f'Unexpected repeated repo without vetted replacement candidate: {x["repo"]} cluster {c}')
        if new:
            changes.append({'cluster_id':c,'rank':x['rank'],'previous_repo':x['repo'],'candidate_repo':new,'reason':reason,'status':'metadata_review_only; not source audited'})
            x['repo']=new; x['url']='https://github.com/'+new
            x['license']='unverified_in_full'
            x['decision']='replacement_metadata_pending_source_audit'
            x['source_code_audited']=False
            x['skill_format_confirmed']=False
            x['installed']=False
            x['replacement_reason']=reason
        key=canonical(x['repo'])
        if key in seen: raise ValueError('Still duplicated: '+key)
        seen.add(key)
        outcome.append(x)
    counts=collections.Counter(x['cluster_id'] for x in outcome)
    if len(records)!=384 or any(counts[c]!=24 for c in range(1,17)):
        raise ValueError('Source is not a 16×24 list; never silently fabricate records')
    return outcome,changes

def scan_checkout(root, limit_files=2500, limit_bytes=800_000):
    root=pathlib.Path(root).resolve(strict=True)
    if not root.is_dir(): raise ValueError('Requires a local repository directory')
    findings=[]; scanned=0; skipped=0; files_seen=[]
    for path in root.rglob('*'):
        if path.is_symlink():
            findings.append({'path':str(path.relative_to(root)),'rule':'symlink_not_followed','line':None});continue
        if not path.is_file():continue
        relative=path.relative_to(root)
        if any(part in {'.git','node_modules','.venv','dist','build','__pycache__'} for part in relative.parts):continue
        scanned+=1
        if scanned>limit_files: raise ValueError('Exceeded file count limit; perform manual triage')
        rel=relative.as_posix()
        if path.stat().st_size>limit_bytes: skipped+=1;continue
        if path.suffix.lower() not in TEXT_EXT and path.name not in CHECK_FILES:continue
        try: content=path.read_text(encoding='utf-8')
        except (UnicodeError,OSError):skipped+=1;continue
        files_seen.append(rel)
        for lineno,line in enumerate(content.splitlines(),1):
            for name,pattern in RISK_PATTERNS.items():
                if pattern.search(line):
                    findings.append({'path':rel,'rule':name,'line':lineno})
                    if len(findings)>=2000: raise ValueError('Exceeded findings cap')
    return {'checkout':str(root),'files_scanned':scanned,'text_files_read':len(files_seen),'skipped_large_or_nontext':skipped,'risk_flags':findings,'status':'static_flags_only_not_security_certified','notes':'No script execution or dependency resolution; findings are review indicators, not proven vulnerabilities.'}

def write_json(path,value):
    p=pathlib.Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def main(argv=None):
    p=argparse.ArgumentParser();sub=p.add_subparsers(dest='command',required=True)
    c=sub.add_parser('curate');c.add_argument('--input',required=True);c.add_argument('--output',required=True)
    a=sub.add_parser('scan');a.add_argument('--checkout',required=True);a.add_argument('--output',required=True)
    args=p.parse_args(argv)
    if args.command=='curate':
        source=pathlib.Path(args.input);document=json.loads(source.read_text(encoding='utf-8'))
        rows,changes=curate(document)
        obj={**{k:v for k,v in document.items() if k not in ('records','accepted_skills','installed_skills_from_candidates')},
             'discovery_entries':len(rows),'accepted_skills':0,'installed_skills_from_candidates':0,
             'note':'Curated candidate identities only. Not approved Skill packages.',
             'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
             'duplicate_replacements':changes,'records':rows}
        write_json(args.output,obj)
        print(json.dumps({'records':len(rows),'unique':len({canonical(x['repo']) for x in rows}),'replacements':len(changes),'output':args.output}))
    else:
        obj=scan_checkout(args.checkout);write_json(args.output,obj)
        print(json.dumps({'flags':len(obj['risk_flags']),'text_read':obj['text_files_read'],'output':args.output}))
if __name__=='__main__':main()
