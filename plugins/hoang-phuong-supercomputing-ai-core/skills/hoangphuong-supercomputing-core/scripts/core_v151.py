"""Hoang Phuong Core v15.1: offline, stdlib-only governance and routing.
Does not execute models, workflows, network calls or plugin connectors.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
CORE = Path('skills/hoangphuong-supercomputing-core')
SKILLS = ('hoangphuong','phattrienungdung','sanxuatnoidung','marketingtongluc','trolydieuhanh','tudonghethong','phantichdautu')
SKILL_RULES = {
    'github500-agent-governance': ('quyen agent','phan quyen','governance','approval','kiem soat quyen'),
    'github500-agent-evaluation': ('benchmark','danh gia agent','kiem thu ai','agent eval','rubric','test suite'),
    'github500-agent-supply-chain': ('supply chain','chuoi cung ung','malware','license','sha-256','checksum'),
    'github500-architecture-blueprint': ('kien truc phan mem','architecture','microservice','so do code','api design'),
    'github500-citation-verification': ('trich dan','bibtex','citation','doi','pmid'),
    'github500-command-library': ('/gh500-','slash code github500'),
    'github500-competitor-analysis': ('doi thu','competitor','phan tich doi thu','thi phan'),
    'github500-experimental-design': ('thiet ke thuc nghiem','doe','randomization','block design'),
    'github500-exploratory-data': ('eda','du lieu thieu','outlier','kham pha du lieu','data analysis'),
    'github500-hypothesis-research': ('gia thuyet','nghien cuu khoa hoc','hypothesis'),
    'github500-lab-cad-planning': ('cad','stl','in 3d','gia do','jig','bambu lab'),
    'github500-prompt-refiner': ('viet prompt','sua prompt','toi uu prompt','prompt refiner'),
    'github500-prompt-safety': ('prompt injection','rui ro prompt','an toan prompt','lo du lieu'),
    'github500-workflow-design': ('tu dong hoa','workflow','n8n','make.com','automation'),
    'github500-ab-testing': ('a/b','ab test','split test','conversion rate','cro'),
}
SLASH_ALIAS_PREFIX = '/gh500-'
STUDY_BASELINE = ROOT / CORE / 'references/STUDY_108_BASELINE.json'
STUDY_PROVENANCE = ROOT / CORE / 'references/STUDY_108_PROVENANCE.json'


def study_baseline_health(root: Path=ROOT)->dict[str,Any]:
    p=root/CORE/'references/STUDY_108_BASELINE.json'
    meta=root/CORE/'references/STUDY_108_PROVENANCE.json'
    if not p.is_file() or not meta.is_file():return {'status':'failed','reason':'authoritative_study_baseline_missing'}
    try:
        data=json.loads(p.read_text(encoding='utf-8'))
        proof=json.loads(meta.read_text(encoding='utf-8'))
        names=[x['code'] for x in data]
        if len(data)!=108 or len(set(names))!=108 or not all(x.startswith('/') and not x.startswith('/gh500-') for x in names):
            return {'status':'failed','reason':'study_registry_count_or_conflict'}
        if not all(isinstance(x['function'],str) and bool(x['function'].strip()) for x in data):
            return {'status':'failed','reason':'invalid_study_function'}
        digest=hashlib.sha256(p.read_bytes()).hexdigest()
        if digest!=proof.get('baseline_sha256'):return {'status':'failed','reason':'study_snapshot_hash_changed'}
        return {'status':'passed','codes':108,'sha256':digest,'note':'same-file snapshot integrity, not external signature'}
    except (ValueError,KeyError,TypeError):return {'status':'failed','reason':'invalid_study_baseline'}

WRITE_ACTIONS = frozenset({'create','update','delete','send','publish','install','execute','start','connect','purchase','transfer','pay','share','archive','merge','deploy'})
IRREVERSIBLE = frozenset({'delete','publish','send','purchase','transfer','pay','share','deploy'})


def fold(s: str) -> str:
    s = str(s).replace('Đ','D').replace('đ','d').casefold()
    s = ''.join(c for c in unicodedata.normalize('NFKD',s) if not unicodedata.combining(c))
    return re.sub(r'\s+',' ',s).strip()


def _contains_phrase(haystack: str, phrase: str) -> bool:
    p = re.escape(fold(phrase))
    if phrase.startswith('/'): return phrase.casefold() in haystack
    return re.search(r'(?<![a-z0-9])'+p+r'(?![a-z0-9])',haystack) is not None


def route(task: str, available: list[str] | None = None) -> dict[str,Any]:
    """Conservative rule router. Unknown/mixed/negative intent abstains."""
    if not isinstance(task,str) or not task.strip():
        return {'status':'abstained','reason':'empty_request','candidates':[]}
    q=fold(task)
    # Slash code priority. Do not reinterpret any of the 108 study commands.
    if task.lstrip().startswith('/') and not task.lstrip().casefold().startswith(SLASH_ALIAS_PREFIX):
        token=task.lstrip().split(maxsplit=1)[0]
        health=study_baseline_health()
        if health['status']=='passed':
            study=json.loads(STUDY_BASELINE.read_text(encoding='utf-8'))
            hit=next((x for x in study if x['code']==token),None)
            if hit:
                return {'status':'study_command','code':token,'original_function':hit['function'],
                        'source':'user_library_108_baseline','execution':'instructions_only'}
        return {'status':'reserved_study_command','reason':'unknown_code_or_registry_not_valid','candidates':[]}
    scores=[]
    for skill,terms in SKILL_RULES.items():
        if available is not None and skill not in available: continue
        matches=[t for t in terms if _contains_phrase(q,t)]
        if matches: scores.append({'skill':skill,'score':sum(1+min(2,len(t)//11) for t in matches),'matches':matches})
    scores.sort(key=lambda x:(-x['score'],x['skill']))
    if not scores:return {'status':'abstained','reason':'no_evidence','candidates':[]}
    top=scores[0]
    if len(scores)>1 and top['score']==scores[1]['score']:
        return {'status':'ambiguous','reason':'equal_score','candidates':scores[:3]}
    if re.search(r'(?<!\w)(khong|dung|cam|never|do not)(?!\w).{0,26}(su dung|dung|run|goi|call|kich hoat)',q):
        return {'status':'needs_review','reason':'negated_or_constrained_intent','candidates':scores[:3]}
    return {'status':'selected','skill':top['skill'],'confidence':'heuristic_not_probability',
            'candidates':scores[:3],'execution':'instruction_only','host_invocation_required':True}


def action_gate(action: str, scope: str, approved: bool=False,
                host_tool_available: bool=False, scoped_permission: bool=False,
                cost_usd: float=0.0, cost_ceiling_usd: float=0.0) -> dict[str,Any]:
    """Policy recommendation only: the host must enforce permissions separately."""
    a=fold(action)
    if a not in WRITE_ACTIONS|{'read','search','inspect','plan','analyze'}:
        return {'decision':'deny','reason':'unknown_action'}
    if not isinstance(scope,str) or not scope.strip():
        return {'decision':'deny','reason':'missing_scope'}
    if cost_usd < 0 or cost_ceiling_usd < 0:return {'decision':'deny','reason':'invalid_budget'}
    if cost_usd>cost_ceiling_usd:return {'decision':'deny','reason':'cost_limit'}
    if not host_tool_available:
        return {'decision':'plan_only','reason':'host_tool_unavailable'}
    if a in WRITE_ACTIONS and not (approved and scoped_permission):
        return {'decision':'approval_required','reason':'write_requires_explicit_authorization'}
    if a in {'purchase','pay','transfer'} and cost_ceiling_usd == 0:
        return {'decision':'deny','reason':'financial_operations_disabled'}
    return {'decision':'permitted_by_policy_only','reason':'host_must_still_authorize',
            'irreversible':a in IRREVERSIBLE}


def verify_study_codes(authoritative: Path | None, candidate: Path | None) -> dict[str,Any]:
    """Fail-closed: original 108-code source never inferred from GitHub aliases."""
    if authoritative is None or candidate is None or not authoritative.is_file() or not candidate.is_file():
        return {'status':'blocked','reason':'both_authoritative_and_candidate_108_code_lists_required','verified':0}
    try:
        a=json.loads(authoritative.read_text(encoding='utf-8'))
        b=json.loads(candidate.read_text(encoding='utf-8'))
    except (ValueError,OSError) as exc:
        return {'status':'blocked','reason':'invalid_json','detail':str(exc)[:80]}
    if not isinstance(a,list) or not isinstance(b,list) or len(a)!=108 or len(b)!=108:
        return {'status':'failed','reason':'expected_108_entries_in_each_registry'}
    def canonical(items):
        if not all(isinstance(x,dict) and isinstance(x.get('code'),str) and isinstance(x.get('function'),str) for x in items):
            raise ValueError('requires_code_and_function_strings')
        names=[x['code'] for x in items]
        if len(set(names))!=108 or not all(x.startswith('/') for x in names):
            raise ValueError('duplicate_or_non_slash_code')
        return {x['code']:x['function'] for x in items}
    try: aa,bb=canonical(a),canonical(b)
    except ValueError as exc: return {'status':'failed','reason':str(exc)}
    if aa!=bb:return {'status':'failed','reason':'code_or_function_changed','mismatches':sorted(set(aa)^set(bb) | {k for k in aa.keys()&bb.keys() if aa[k]!=bb[k]})[:20]}
    return {'status':'passed','verified':108,'sha256':hashlib.sha256(json.dumps(aa,ensure_ascii=False,sort_keys=True).encode()).hexdigest()}


def _version_tuple(value: str) -> tuple[int, int, int] | None:
    if not isinstance(value, str) or not re.fullmatch(r"\d+\.\d+\.\d+", value):
        return None
    return tuple(int(part) for part in value.split("."))


def current_release_version(root: Path=ROOT) -> str | None:
    """Return the matched plugin version only when both manifests identify this plugin."""
    versions=[]
    for name in ("plugin.json", ".codex-plugin/plugin.json"):
        path=root/name
        try:
            manifest=json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return None
        if manifest.get("name")!="hoang-phuong-supercomputing-ai-core":
            return None
        version=manifest.get("version")
        if _version_tuple(version) is None:
            return None
        versions.append(version)
    return versions[0] if len(versions)==2 and versions[0]==versions[1] else None


def doctor(root: Path=ROOT)->dict[str,Any]:
    problems=[]; warnings=[]; evidence={}; root=root.resolve()
    release_version=current_release_version(root)
    if release_version is None:
        problems.append('manifest_version_parity_failure')
    else:
        evidence['plugin_version']=release_version
        if _version_tuple(release_version) < (15,1,3): problems.append('plugin_version_too_old')
    for name in SKILLS:
        if not (root/'skills'/name/'SKILL.md').is_file(): problems.append('missing_original_skill:'+name)
    rolesfile=root/CORE/'references/AGENTS_128.json'
    if not rolesfile.is_file(): problems.append('agent_registry_missing')
    else:
        try:
            roles=json.loads(rolesfile.read_text(encoding='utf-8'))['roles']
            ids=[int(x['id']) for x in roles]
            if ids!=list(range(1,129)):problems.append('agent_ids_invalid')
            evidence['agent_count']=len(roles)
            groups={x['group'] for x in roles}; evidence['cluster_count']=len(groups)
            if groups!=set(range(1,17)):problems.append('cluster_ids_invalid')
        except (ValueError,KeyError,TypeError) as exc:problems.append('agent_registry_invalid:'+type(exc).__name__)
    catalog=root/CORE/'references/GITHUB_500_MASTER_CATALOG.json'
    if not catalog.is_file(): problems.append('catalog_missing')
    else:
        try:
            entries=json.loads(catalog.read_text(encoding='utf-8'))['records']
            ids=[x['repo'] for x in entries]
            if len(entries)!=500 or len(set(ids))!=500: problems.append('catalog_500_identity_failure')
            evidence['discovered_repos']=len(entries)
        except (ValueError,KeyError,TypeError):problems.append('catalog_invalid')
    for fname in ('plugin.json','.codex-plugin/plugin.json'):
        p=root/fname
        if not p.is_file():problems.append('missing_manifest:'+fname);continue
        try:
            m=json.loads(p.read_text(encoding='utf-8'))
            if release_version is not None and m['version']!=release_version:problems.append('version_mismatch:'+fname)
            if m['name']!='hoang-phuong-supercomputing-ai-core':problems.append('identity_changed:'+fname)
        except (ValueError,KeyError):problems.append('invalid_manifest:'+fname)
    mx=root/CORE/'references/CAPABILITY_MATRIX.json'
    if not mx.is_file():problems.append('capability_matrix_missing')
    else:
        try:
            cap=json.loads(mx.read_text(encoding='utf-8'))
            if release_version is None or cap.get('release')!=release_version:problems.append('matrix_release_mismatch')
        except ValueError:problems.append('capability_matrix_invalid')
    for skill in SKILL_RULES:
        if not (root/'skills'/skill/'SKILL.md').is_file():problems.append('missing_adapted_skill:'+skill)
    study=study_baseline_health(root)
    if study['status']!='passed':problems.append('study_108_baseline_invalid')
    else:evidence['study_codes']=study['codes']
    warnings.append('study_108_import_is_verified_against_user_library_snapshot_not_independent_current_project_state')
    warnings.append('live_runtime_and_external_connectors_not_certified_by_offline_doctor')
    return {'status':'passed' if not problems else 'failed','problems':problems,'warnings':warnings,'evidence':evidence,'mode':'embedded_skills_only'}


def plan(task: str, available: list[str] | None=None)->dict[str,Any]:
    choice=route(task,available)
    return {'version':current_release_version(),'mode':'embedded_skills_only','routing':choice,
            'execution':'not_executed','requires_host_permission':True,
            'agent_roles':'select_1_to_4_from_registry_on_demand',
            'steps':['classify','verify_tool_current_session','evaluate_license_and_risk','request_approval_if_write','invoke_host_tool_when_authorized','verify_output','audit_log'],
            'rollback':'preserve_original_plugins_and_source_documents'}



def verify_delta_manifest(root: Path=ROOT)->dict[str,Any]:
    """Validate release overlay hashes; this does not authenticate publisher identity."""
    root=root.resolve()
    m=root/CORE/'references/V151_DELTA_SHA256.json'
    if not m.is_file():return {'status':'failed','reason':'manifest_missing'}
    try: entries=json.loads(m.read_text(encoding='utf-8'))['files']
    except (ValueError,KeyError,TypeError):return {'status':'failed','reason':'manifest_invalid'}
    failures=[]
    for rel,expected in entries.items():
        if not isinstance(rel,str) or not isinstance(expected,str) or not re.fullmatch(r'[0-9a-f]{64}',expected):
            failures.append('bad_entry');continue
        f=root/rel
        if f.is_symlink() or not f.resolve().is_relative_to(root) or not f.is_file():
            failures.append('missing_or_unsafe_path:'+rel);continue
        if hashlib.sha256(f.read_bytes()).hexdigest()!=expected:
            failures.append('digest_mismatch:'+rel)
    return {'status':'passed' if not failures else 'failed','checked':len(entries),'issues':failures,
            'qualification':'integrity_against_release_manifest_only_not_signature'}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('command',choices=['route','plan','doctor','gate','codes','verify-delta','study-health'])
    ap.add_argument('--task',default='');ap.add_argument('--action',default='read');ap.add_argument('--scope',default='')
    ap.add_argument('--approved',action='store_true');ap.add_argument('--host-available',action='store_true');ap.add_argument('--scoped-permission',action='store_true')
    ap.add_argument('--authoritative',type=Path);ap.add_argument('--candidate',type=Path)
    args=ap.parse_args()
    if args.command=='route':out=route(args.task)
    elif args.command=='plan':out=plan(args.task)
    elif args.command=='doctor':out=doctor()
    elif args.command=='study-health':out=study_baseline_health()
    elif args.command=='verify-delta':out=verify_delta_manifest()
    elif args.command=='gate':out=action_gate(args.action,args.scope,args.approved,args.host_available,args.scoped_permission)
    else:out=verify_study_codes(args.authoritative,args.candidate)
    print(json.dumps(out,ensure_ascii=False,indent=2))
    if out.get('status')=='failed':raise SystemExit(2)

if __name__=='__main__':main()
