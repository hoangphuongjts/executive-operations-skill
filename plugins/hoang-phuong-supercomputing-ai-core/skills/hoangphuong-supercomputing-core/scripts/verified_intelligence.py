#!/usr/bin/env python3
"""v13.1 offline verification/evaluation/microbenchmark utility (stdlib only).

This file is inert while installed as a ChatGPT skill. It runs only when a user
or authorized executor explicitly invokes Python. Measurements are local and
are not claims about ChatGPT, quantum hardware, agents, or hosted QPS.
"""
from __future__ import annotations

import argparse
import bisect
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import platform
import random
import re
import sys
import time
from typing import Any

VERSION = '14.0.0'
SKILLS = ('hoangphuong','phattrienungdung','sanxuatnoidung','marketingtongluc',
          'trolydieuhanh','tudonghethong','phantichdautu')
PREFIX = Path('skills/hoangphuong-supercomputing-core')
ROLES = PREFIX / 'references/ROLES_64.md'
CAPABILITIES = PREFIX / 'references/CAPABILITY_MATRIX.json'
FIXTURE = PREFIX / 'fixtures/evaluation_demo.jsonl'


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def root_dir() -> Path:
    return Path(__file__).resolve().parents[3]


def record(name: str, ok: bool, detail: str) -> dict[str, Any]:
    return {'check': name, 'passed': bool(ok), 'detail': detail}


def parse_roles(text: str) -> list[int]:
    return [int(match) for match in re.findall(r'^\s*(\d{2})\.\s+\S', text, flags=re.M)]


def fnv_utf16(s: str) -> str:
    """Compare old/new Unicode skill text with a deterministic lightweight checksum."""
    h = 0xcbf29ce484222325
    data = s.encode('utf-16-le')
    for b in data:
        h = ((h ^ b) * 0x100000001b3) & 0xffffffffffffffff
    return f'{h:016x}'


def verify(root: Path) -> dict[str, Any]:
    root = Path(root)
    checks: list[dict[str, Any]] = []
    files: dict[str, Any] = {}
    for path in ('plugin.json', '.codex-plugin/plugin.json'):
        try:
            files[path] = json.loads((root / path).read_text(encoding='utf-8'))
            checks.append(record('parse:' + path, True, 'JSON valid'))
        except (OSError, ValueError) as exc:
            files[path] = {}
            checks.append(record('parse:' + path, False, type(exc).__name__))
    a,b = files['plugin.json'],files['.codex-plugin/plugin.json']
    current_version = a.get('version')
    valid_version = (isinstance(current_version, str) and re.fullmatch(r'\d+\.\d+\.\d+', current_version)
                     and tuple(map(int, current_version.split('.'))) >= (14, 0, 0))
    checks.append(record('manifest_version', bool(valid_version and current_version == b.get('version')),
                         f"versions={a.get('version')!r}/{b.get('version')!r}; expected >= {VERSION}"))
    checks.append(record('manifest_identity', a.get('name') == b.get('name') == 'hoang-phuong-supercomputing-ai-core',
                         f"names={a.get('name')!r}/{b.get('name')!r}"))
    display = a.get('extensions',{}).get('com.openai',{}).get('interface',{}).get('displayName')
    checks.append(record('display_name', display == 'hoangphuong-supercomputing-core', f'display={display!r}'))
    for skill in SKILLS:
        relative = f'skills/{skill}/SKILL.md'
        present = (root / relative).is_file()
        checks.append(record('legacy:' + skill, present, 'present' if present else 'missing'))
    try:
        numbers = parse_roles((root / ROLES).read_text(encoding='utf-8'))
        good = len(numbers)==64 and sorted(numbers)==list(range(1,65))
        checks.append(record('64_roles', good, f'{len(numbers)} numbered roles; unique={len(set(numbers))}'))
    except OSError as exc:
        checks.append(record('64_roles', False, type(exc).__name__))
    try:
        skilltext=(root / PREFIX/'SKILL.md').read_text(encoding='utf-8')
        modules = ('Recursive JIT Self-Patching','Distributed Quantum Neural Fabric',
                   'Automated Algorithm Discovery','Recursive Meta-Learning')
        checks.append(record('four_modules', all(s in skilltext for s in modules),
                             f'{sum(x in skilltext for x in modules)}/4 named modules'))
        checks.append(record('verified_intelligence_reference', 'VERIFIED INTELLIGENCE v13.1' in skilltext,
                             'Core skill references v13.1 verification rules'))
    except OSError as exc:
        checks.append(record('four_modules',False,type(exc).__name__))
        checks.append(record('verified_intelligence_reference',False,type(exc).__name__))
    try:
        hashes=json.loads((root/PREFIX/'references/LEGACY_INTEGRITY.json').read_text(encoding='utf-8'))['hashes']
        for relative,digest in hashes.items():
            try:
                found=fnv_utf16((root/relative).read_text(encoding='utf-8'))
                checks.append(record('preserved:' + relative, found==digest,
                                     'unchanged from v13.0 baseline' if found==digest else 'legacy content changed'))
            except OSError:
                checks.append(record('preserved:' + relative,False,'file missing'))
    except (OSError,ValueError,KeyError,TypeError) as exc:
        checks.append(record('legacy_integrity_baseline',False,type(exc).__name__))
    try:
        matrix=json.loads((root/CAPABILITIES).read_text(encoding='utf-8'))
        caps=matrix['capabilities']; allowed=set(matrix['capability_status_semantics'])
        unique_ids=len({c['id'] for c in caps})==len(caps)
        status_ok=all(c['status'] in allowed for c in caps)
        checks.append(record('capability_matrix', bool(caps) and unique_ids and status_ok,
                             f'{len(caps)} entries, unique_ids={unique_ids}, statuses_valid={status_ok}'))
    except (OSError,ValueError,KeyError,TypeError) as exc:
        checks.append(record('capability_matrix',False,type(exc).__name__))
    return {'tool':'Verified Intelligence Core','mode':'verify','release':VERSION,
            'checked_at_utc':now_utc(),'root':str(root),'checks':checks,
            'passed':sum(c['passed'] for c in checks),'total':len(checks),
            'status':'passed' if all(c['passed'] for c in checks) else 'failed',
            'limitations':['Structure checks only; original skill byte-equivalence needs release-to-release comparison',
                           'No inference, QPU, JIT, parallel-agent or production-service runtime is exercised']}


def evaluate(dataset: Path) -> dict[str, Any]:
    cases=[]
    for n,line in enumerate(Path(dataset).read_text(encoding='utf-8').splitlines(),1):
        if not line.strip(): continue
        case=json.loads(line)
        if not all(isinstance(case.get(k),str) for k in ('id','expected','actual')):
            raise ValueError(f'invalid required string fields at line {n}')
        if not isinstance(case.get('evidence',[]),list):
            raise ValueError(f'evidence must be a list at line {n}')
        good=case['expected'].strip().casefold()==case['actual'].strip().casefold()
        cases.append({'id':case['id'],'exact_match':good,
                      'evidence_supplied':bool(case.get('evidence'))})
    if not cases: raise ValueError('evaluation dataset must contain at least one case')
    return {'tool':'Verified Intelligence Core','mode':'evaluate','checked_at_utc':now_utc(),
            'dataset':str(dataset),'cases':cases,'count':len(cases),
            'exact_match_rate':sum(c['exact_match'] for c in cases)/len(cases),
            'evidence_coverage':sum(c['evidence_supplied'] for c in cases)/len(cases),
            'status':'measured_on_supplied_dataset',
            'limitations':['Exact match is not semantic correctness or factual ground truth',
                           'Evidence presence is not source validity',
                           'Demo cases are synthetic and cannot measure model accuracy']}


def percentile(values: list[int], pct: float) -> float:
    if not values: raise ValueError('percentile requires nonempty list')
    ranked=sorted(values)
    index=(len(ranked)-1)*pct/100
    lo=int(index);hi=min(lo+1,len(ranked)-1)
    return ranked[lo]+(ranked[hi]-ranked[lo])*(index-lo)


def linear_lookup(values: list[int], x: int) -> int:
    for i,value in enumerate(values):
        if value==x: return i
    return -1


def binary_lookup(values: list[int], x: int) -> int:
    pos=bisect.bisect_left(values,x)
    return pos if pos<len(values) and values[pos]==x else -1


def benchmark(size: int=4096, iterations: int=300, seed: int=131) -> dict[str,Any]:
    if not 16<=size<=100000: raise ValueError('size must be in [16, 100000]')
    if not 10<=iterations<=20000: raise ValueError('iterations must be in [10, 20000]')
    rng=random.Random(seed)
    values=list(range(0,size*2,2))
    queries=[rng.randrange(0,size*2+2) for _ in range(iterations)]
    expected=[linear_lookup(values,q) for q in queries]
    if expected!=[binary_lookup(values,q) for q in queries]:
        raise AssertionError('algorithms returned different answers')
    results={}
    for label, fn in [('linear_search_baseline',linear_lookup),('bisect_search_candidate',binary_lookup)]:
        times=[]
        start=time.perf_counter_ns()
        for q,correct in zip(queries,expected):
            begin=time.perf_counter_ns()
            found=fn(values,q)
            times.append(time.perf_counter_ns()-begin)
            if found!=correct: raise AssertionError('incorrect lookup result')
        elapsed=time.perf_counter_ns()-start
        results[label]={'operations':iterations, 'wall_ns':elapsed,'ops_per_second':round(iterations/(elapsed/1e9),2),
                        'p50_ns':round(percentile(times,50),2),'p95_ns':round(percentile(times,95),2),
                        'p99_ns':round(percentile(times,99),2)}
    return {'tool':'Verified Intelligence Core','mode':'benchmark','checked_at_utc':now_utc(),
            'environment':{'python':sys.version.split()[0], 'platform':platform.platform(),'pid':os.getpid()},
            'workload':{'size':size,'iterations':iterations,'seed':seed,'type':'single-process in-memory Python lookup'},
            'correctness':'passed','results':results,'status':'measured_local_microbenchmark',
            'limitations':['Not JIT, SIMD, QPU, P2P, parallelism or production service throughput',
                           'Timing includes Python overhead and measurement perturbation; compare on the same machine',
                           'Small synthetic workload, not a service SLA or independent benchmark']}


def report(root: Path, dataset: Path) -> dict[str,Any]:
    verification=verify(root)
    evaluation=evaluate(dataset)
    matrix=json.loads((root/CAPABILITIES).read_text(encoding='utf-8'))
    return {'tool':'Verified Intelligence Core','mode':'capability_report','release':VERSION,
            'checked_at_utc':now_utc(),'verification':{'status':verification['status'],
              'checks_passed':verification['passed'],'checks_total':verification['total']},
            'demo_evaluation':{'exact_match_rate':evaluation['exact_match_rate'],
              'cases':evaluation['count'],'is_synthetic':True},
            'capabilities':matrix['capabilities'],'status':'report_generated_not_hosted_runtime_verified',
            'limitations':['Capabilities list is declared configuration, not proof of deployment',
                           'Run a workload-specific benchmark and an independent real evaluation to make stronger claims']}


def main(argv: list[str]|None=None) -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=('verify','evaluate','benchmark','report'))
    parser.add_argument('--root',type=Path,default=root_dir(),help='unpacked plugin root')
    parser.add_argument('--dataset',type=Path,default=None,help='JSONL labeled cases')
    parser.add_argument('--size',type=int,default=4096,help='benchmark in-memory list size')
    parser.add_argument('--iterations',type=int,default=300,help='benchmark lookup count')
    parser.add_argument('--seed',type=int,default=131)
    parser.add_argument('--output',type=Path,default=None,help='explicit path to save JSON; otherwise stdout only')
    args=parser.parse_args(argv)
    try:
        dataset=args.dataset or args.root/FIXTURE
        if args.command=='verify': out=verify(args.root)
        elif args.command=='evaluate': out=evaluate(dataset)
        elif args.command=='benchmark': out=benchmark(args.size,args.iterations,args.seed)
        else: out=report(args.root,dataset)
        payload=json.dumps(out,ensure_ascii=False,indent=2)+'\n'
        if args.output:
            args.output.parent.mkdir(parents=True,exist_ok=True)
            args.output.write_text(payload,encoding='utf-8')
        else:
            sys.stdout.write(payload)
        return int(args.command=='verify' and out['status']!='passed')
    except (OSError, ValueError, KeyError, TypeError, AssertionError) as exc:
        print(json.dumps({'command':args.command,'status':'error','error':str(exc)},ensure_ascii=False),file=sys.stderr)
        return 2


if __name__=='__main__':
    sys.exit(main())
