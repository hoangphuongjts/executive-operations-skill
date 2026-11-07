"""Compare user-provided evaluation evidence without invoking an AI or claiming certification.

This is a *reporting gate*, not an authorization mechanism: the caller must verify
provenance and permissions independently of JSON supplied by an agent.
"""
from __future__ import annotations
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

EVALUATORS = {'independent_human_reviewed', 'execution_test', 'golden_answer_verified'}
MAX_EVIDENCE_BYTES = 2 * 1024 * 1024


def load_evidence(path: str | Path) -> dict:
    file = Path(path).expanduser().resolve(strict=True)
    if not file.is_file() or file.is_symlink() or file.stat().st_size > MAX_EVIDENCE_BYTES:
        raise ValueError('Evidence phải là file thường nhỏ hơn 2 MiB')
    evidence = json.loads(file.read_text(encoding='utf-8'))
    validate_evidence(evidence)
    return evidence


def validate_evidence(e: dict) -> None:
    if not isinstance(e, dict):
        raise ValueError('Evidence phải là object')
    for key in ('run_id', 'dataset_id', 'dataset_sha256', 'evaluator', 'environment', 'model_version', 'measured_at'):
        if not isinstance(e.get(key), str) or not e[key].strip():
            raise ValueError(f'Thiếu trường chứng cứ: {key}')
    if not re.fullmatch(r'[a-f0-9]{64}', e['dataset_sha256']):
        raise ValueError('Dataset hash phải là sha256 hex')
    if e['evaluator'] not in EVALUATORS:
        raise ValueError('Chỉ chấp nhận bằng chứng test/golden/human review, không tự chấm model')
    tasks = e.get('tasks')
    if not isinstance(tasks, list) or not (1 <= len(tasks) <= 10000):
        raise ValueError('Tasks rỗng hoặc quá giới hạn')
    ids = set()
    for task in tasks:
        if not isinstance(task, dict) or not isinstance(task.get('id'), str) or not task['id'].strip() or type(task.get('passed')) is not bool:
            raise ValueError('Task phải có id và passed boolean')
        if task['id'] in ids:
            raise ValueError('Trùng task id')
        ids.add(task['id'])
    blockers = e.get('security_blockers')
    if not isinstance(blockers, list) or any(not isinstance(x, str) or not x for x in blockers):
        raise ValueError('security_blockers phải là danh sách')
    try:
        datetime.fromisoformat(e['measured_at'].replace('Z','+00:00'))
    except ValueError as exc:
        raise ValueError('Sai timestamp') from exc


def compare_runs(baseline: dict, candidate: dict) -> dict:
    validate_evidence(baseline)
    validate_evidence(candidate)
    if baseline['run_id'] == candidate['run_id']:
        raise ValueError('Baseline và candidate không được cùng run_id')
    for name in ('dataset_id', 'dataset_sha256'):
        if baseline[name] != candidate[name]:
            raise ValueError('Hai lần đo phải cùng bộ dữ liệu kiểm thử đã đóng băng')
    b = {x['id']:x['passed'] for x in baseline['tasks']}
    c = {x['id']:x['passed'] for x in candidate['tasks']}
    if b.keys()!=c.keys():
        raise ValueError('Không được thay đổi tập task khi so sánh')
    lost = sorted(k for k in b if b[k] and not c[k])
    gains = sorted(k for k in b if not b[k] and c[k])
    blocked = len(candidate['security_blockers'])>0
    decision = 'blocked_security' if blocked else 'blocked_regression' if lost else 'candidate_eligible_for_review' if gains else 'no_verified_gain'
    return {
        'status':'offline_evidence_compared_not_deployed',
        'decision':decision,
        'dataset_id':baseline['dataset_id'],'dataset_sha256':baseline['dataset_sha256'],
        'task_count':len(b),'baseline_passed':sum(b.values()),'candidate_passed':sum(c.values()),
        'improved_tasks':len(gains),'regressed_tasks':len(lost),
        'gain_task_ids':gains,'regression_task_ids':lost,
        'security_blockers':candidate['security_blockers'],
        'evaluator_claims':[baseline['evaluator'],candidate['evaluator']],
        'note':'Evidence được đọc từ JSON do người vận hành cung cấp; chưa chứng thực độc lập nguồn gốc, chưa chạy model, chưa cấp quyền triển khai.'
    }


def assess_candidate(comparison: dict, *, approval: bool = False) -> dict:
    return {
        'can_deploy':False,
        'stage':'review_only',
        'candidate_quality_gate': comparison.get('decision') == 'candidate_eligible_for_review',
        'approval_noted':bool(approval),
        'reason':'Approval in this offline module is NOT a ChatGPT host authorization or a production deploy action.'
    }


def write_release_candidate(reports: str | Path, comparison: dict) -> Path:
    folder = Path(reports).expanduser().resolve()
    folder.mkdir(parents=True, exist_ok=True)
    record = {
        'stage':'review_only',
        'comparison':comparison,
        'approval': 'required_on_target_host',
        'can_deploy':False,
        'created_at':datetime.now(timezone.utc).isoformat(),
    }
    raw = json.dumps(record, ensure_ascii=False, sort_keys=True, indent=2)+'\n'
    identifier=sha256(json.dumps(comparison,sort_keys=True).encode()).hexdigest()[:16]
    target=folder/f'candidate_review_{identifier}.json'
    if target.exists():
        if json.loads(target.read_text(encoding='utf-8'))['comparison'] == comparison:
            return target
        raise FileExistsError('Review filename collision')
    with target.open('x', encoding='utf-8') as f:
        f.write(raw)
    return target
