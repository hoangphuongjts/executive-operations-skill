"""Read-only discovery and guarded, reversible local Skill documentation repair.

No autonomous code execution, package installs, cloud publishing or model access.
"""
from __future__ import annotations
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import os
import re
import shutil
import urllib.error
import urllib.parse
import urllib.request

MAX_SKILL_BYTES = 1024 * 1024
VERIFICATION_MARKER = '## Kiểm chứng và giới hạn'
VERIFICATION_APPEND = '''\n\n## Kiểm chứng và giới hạn\n\n- Phân biệt các phần đã thiết kế, đã tạo tệp, đã kiểm thử và đã triển khai thực tế.\n- Chỉ báo kết quả kiểm thử khi có lệnh, môi trường và bằng chứng thực thi; không suy diễn từ mô tả Skill.\n- Không tự chạy mã từ nguồn ngoài, cấp quyền, mua dịch vụ hoặc sửa hệ thống ngoài phạm vi đã cho phép.\n- Khi thay đổi chức năng, yêu cầu bài kiểm thử hồi quy và phương án khôi phục.\n'''


def _sha(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _resolve_root(root: str | Path) -> Path:
    p = Path(root).expanduser().resolve(strict=True)
    if not p.is_dir():
        raise ValueError('Skill root phải là thư mục hiện hữu')
    return p


def _safe_path(root: str | Path, relpath: str, *, require_file=True) -> Path:
    """Reject traversal, absolute input, and any symlink component."""
    base = _resolve_root(root)
    rel = Path(relpath)
    if rel.is_absolute() or not rel.parts or any(x in ('.', '..') for x in rel.parts):
        raise ValueError('Đường dẫn không được phép')
    cur = base
    for part in rel.parts:
        cur = cur / part
        if cur.is_symlink():
            raise ValueError('Từ chối symlink trong đường dẫn')
    target = cur.resolve(strict=require_file)
    if not target.is_relative_to(base):
        raise ValueError('Truy cập ngoài thư mục Skill')
    if require_file and (not target.is_file() or target.stat().st_size > MAX_SKILL_BYTES):
        raise ValueError('Không phải tệp hợp lệ hoặc kích thước vượt giới hạn')
    return target


def safe_read(root: str | Path, relative_path: str) -> str:
    return _safe_path(root, relative_path).read_text(encoding='utf-8')


def _append_verification_section(content: str) -> str:
    """Append the standard section while preserving the file's line endings."""
    newline = '\r\n' if '\r\n' in content else '\n'
    append = VERIFICATION_APPEND.replace('\n', newline)
    return content.rstrip('\r\n') + append


def _parse_frontmatter(content: str) -> dict:
    """Conservative plain YAML subset, no YAML evaluation or trust of nested content."""
    if not content.startswith('---\n'):
        return {}
    end = content.find('\n---\n', 4)
    if end < 0:
        return {}
    data = {}
    for line in content[4:end].splitlines():
        match = re.match(r'^(name|description):\s*(.+)$', line)
        if match:
            data[match.group(1)] = match.group(2).strip().strip('"\'')
    return data


def scan_skills(root: str | Path) -> list[dict]:
    base = _resolve_root(root)
    results = []
    # Do not recurse through arbitrary files or symlinks: only direct skills/<id>/SKILL.md.
    for folder in sorted(base.iterdir()):
        if folder.is_symlink() or not folder.is_dir():
            continue
        file = folder / 'SKILL.md'
        if file.is_symlink() or not file.is_file():
            continue
        if file.stat().st_size > MAX_SKILL_BYTES:
            continue
        relative = file.relative_to(base).as_posix()
        raw = _safe_path(base, relative).read_bytes()
        content = raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')
        fm = _parse_frontmatter(content)
        tests = folder / 'tests'
        has_tests = tests.is_dir() and not tests.is_symlink() and any(
            p.is_file() and not p.is_symlink() and p.suffix == '.py' for p in tests.iterdir()
        )
        results.append({
            'path': relative,
            'folder': folder.name,
            'name': fm.get('name', ''),
            'description': fm.get('description', ''),
            'sha256': _sha(raw),
            'has_verification': bool(re.search(r'^##\s+(?:Kiểm chứng|Verification|Testing|Kiểm thử)', content, re.MULTILINE | re.IGNORECASE)),
            'has_tests': has_tests,
            'bytes': file.stat().st_size,
            'status': 'source_metadata_scanned',
        })
    return results


def diagnose(skills: list[dict]) -> list[dict]:
    issues: list[dict] = []
    for s in skills:
        if not s['name'] or s['name'] != s['folder']:
            issues.append({'path': s['path'], 'code': 'frontmatter_name_mismatch', 'severity': 'high', 'evidence': 'Tên frontmatter thiếu hoặc khác tên thư mục', 'repair_type': 'manual_review'})
        if not s['description']:
            issues.append({'path': s['path'], 'code': 'missing_description', 'severity': 'high', 'evidence': 'Không tìm thấy description một dòng trong frontmatter', 'repair_type': 'manual_review'})
        if not s['has_verification']:
            issues.append({'path': s['path'], 'code': 'missing_verification_section', 'severity': 'medium', 'evidence': 'Thiếu mục kiểm chứng/giới hạn rõ ràng', 'repair_type': 'append_verification', 'base_sha256': s['sha256']})
        if not s['has_tests']:
            issues.append({'path': s['path'], 'code': 'tests_not_detected', 'severity': 'low', 'evidence': 'Không thấy test Python trong thư mục tests/ trực thuộc Skill; chưa kết luận thiếu mọi loại test', 'repair_type': 'manual_review'})
    order = {'high': 0, 'medium': 1, 'low': 2}
    return sorted(issues, key=lambda item: (order[item['severity']], item['path'], item['code']))


def create_proposals(issues: list[dict]) -> list[dict]:
    result = []
    for issue in issues:
        if issue['repair_type'] != 'append_verification':
            continue
        identity = f"{issue['path']}|{issue['code']}|{issue['base_sha256']}"
        result.append({
            'id': _sha(identity.encode())[:20],
            'path': issue['path'],
            'base_sha256': issue['base_sha256'],
            'repair_type': issue['repair_type'],
            'status': 'proposed_only',
            'reason': issue['evidence'],
        })
    return result


def _write_json(path: Path, content: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(content, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def stage_proposal(root: str | Path, reports: str | Path, proposal: dict) -> dict:
    if proposal['repair_type'] != 'append_verification':
        raise ValueError('Loại cập nhật không được hỗ trợ')
    original = _safe_path(root, proposal['path'])
    raw = original.read_bytes()
    if _sha(raw) != proposal['base_sha256']:
        raise ValueError('Tệp đã đổi, cần chạy scan lại')
    text = raw.decode('utf-8')
    if VERIFICATION_MARKER in text or re.search(r'^##\s+(?:Verification|Testing|Kiểm thử)', text, re.M | re.I):
        raise ValueError('Mục kiểm chứng đã tồn tại')
    expected = create_proposals([{
        'path': proposal['path'], 'code': 'missing_verification_section',
        'base_sha256': proposal['base_sha256'], 'repair_type': 'append_verification',
        'evidence': proposal.get('reason', ''),
    }])[0]['id']
    if proposal['id'] != expected:
        raise ValueError('Proposal ID không hợp lệ')
    out = Path(reports).expanduser().resolve()
    if out.is_relative_to(_resolve_root(root)):
        raise ValueError('Báo cáo phải nằm ngoài thư mục nguồn')
    folder = out / 'staged' / proposal['id']
    if folder.exists():
        raise FileExistsError('Proposal đã staged, không tự ghi đè')
    folder.mkdir(parents=True)
    candidate = _append_verification_section(text)
    (folder/'SKILL.md').write_bytes(candidate.encode('utf-8'))
    manifest = {**proposal, 'status': 'staged', 'candidate_sha256': _sha(candidate.encode('utf-8')), 'staged_at': _now()}
    _write_json(folder/'proposal.json', manifest)
    return manifest


def _load_stage(reports: Path, proposal_id: str) -> dict:
    if not re.fullmatch(r'[0-9a-f]{20}', proposal_id):
        raise ValueError('Proposal ID không hợp lệ')
    stage = reports / 'staged' / proposal_id
    if stage.is_symlink() or (stage/'SKILL.md').is_symlink() or (stage/'proposal.json').is_symlink():
        raise ValueError('Symlink không được phép')
    data = json.loads((stage/'proposal.json').read_text(encoding='utf-8'))
    if data['id'] != proposal_id or data['repair_type'] != 'append_verification':
        raise ValueError('Manifest không hợp lệ')
    return data


def apply_proposal(root: str | Path, reports: str | Path, proposal_id: str, *, approval: str) -> dict:
    if approval != proposal_id:
        raise PermissionError('Yêu cầu xác nhận ID đúng từ người vận hành')
    reports = Path(reports).expanduser().resolve(strict=True)
    if reports.is_relative_to(_resolve_root(root)):
        raise ValueError('Thư mục báo cáo không được nằm trong nguồn')
    data = _load_stage(reports, proposal_id)
    expected_id = _sha(f"{data['path']}|missing_verification_section|{data['base_sha256']}".encode())[:20]
    if expected_id != proposal_id:
        raise ValueError('Proposal metadata đã bị sửa đổi')
    target = _safe_path(root, data['path'])
    original = target.read_bytes()
    if _sha(original) != data['base_sha256']:
        raise ValueError('Nguồn đã bị thay đổi, không ghi đè')
    candidate = (reports/'staged'/proposal_id/'SKILL.md').read_bytes()
    if _sha(candidate) != data['candidate_sha256']:
        raise ValueError('Candidate bị sửa sau lúc staging')
    expected_text = _append_verification_section(original.decode('utf-8'))
    if candidate.decode('utf-8') != expected_text:
        raise ValueError('Candidate không khớp thay đổi an toàn đã định nghĩa')
    backup_id = _sha((proposal_id + '|' + data['base_sha256']).encode())[:24]
    backup_dir = reports/'backups'/backup_id
    if backup_dir.exists():
        raise FileExistsError('Backup ID đã tồn tại; dừng để tránh ghi đè')
    backup_dir.mkdir(parents=True)
    (backup_dir/'original.md').write_bytes(original)
    _write_json(backup_dir/'backup.json', {'backup_id': backup_id, 'path': data['path'], 'original_sha256': data['base_sha256'], 'updated_sha256': data['candidate_sha256'], 'created_at': _now()})
    temp = target.with_name(target.name+'.evolution.tmp')
    if temp.exists() or temp.is_symlink():
        raise FileExistsError('Tệp tạm đã tồn tại')
    try:
        with temp.open('xb') as f:
            f.write(candidate)
        os.replace(temp, target)
    finally:
        if temp.exists():
            temp.unlink()
    result = {'status': 'local_doc_patch_applied', 'path': data['path'], 'backup_id': backup_id, 'sha256': data['candidate_sha256'], 'applied_at': _now()}
    _write_json(reports/'applied'/f'{proposal_id}.json', result)
    return result


def restore_backup(root: str | Path, reports: str | Path, backup_id: str, *, approval: str) -> dict:
    if approval != backup_id or not re.fullmatch('[0-9a-f]{24}', backup_id):
        raise PermissionError('Yêu cầu xác nhận backup ID đúng')
    reports = Path(reports).expanduser().resolve(strict=True)
    folder = reports/'backups'/backup_id
    if folder.is_symlink() or (folder/'original.md').is_symlink() or (folder/'backup.json').is_symlink():
        raise ValueError('Không cho phép symlink')
    data = json.loads((folder/'backup.json').read_text(encoding='utf-8'))
    if data['backup_id'] != backup_id:
        raise ValueError('ID không khớp')
    target = _safe_path(root, data['path'])
    if _sha(target.read_bytes()) != data['updated_sha256']:
        raise ValueError('Tệp đã thay đổi sau cập nhật, không được rollback đè lên')
    original = (folder/'original.md').read_bytes()
    if _sha(original) != data['original_sha256']:
        raise ValueError('Bản sao lưu đã bị thay đổi')
    temp = target.with_name(target.name+'.restore.tmp')
    with temp.open('xb') as f: f.write(original)
    os.replace(temp, target)
    return {'status':'restored', 'path': data['path'], 'sha256': data['original_sha256']}


def audit_tree(root: str | Path) -> dict:
    base = _resolve_root(root)
    entries = []
    for item in sorted(base.rglob('*')):
        if item.is_symlink():
            entries.append({'path': item.relative_to(base).as_posix(), 'status': 'symlink_skipped'})
        elif item.is_file():
            rel = item.relative_to(base).as_posix()
            try:
                raw = _safe_path(base,rel).read_bytes()
            except (ValueError, OSError):
                entries.append({'path':rel, 'status':'unsafe_or_oversized_skipped'})
                continue
            entries.append({'path': rel, 'sha256':_sha(raw)})
    blob = json.dumps(entries, sort_keys=True, ensure_ascii=False).encode('utf-8')
    return {'tree_sha256': _sha(blob), 'files': entries, 'scanned_at': _now()}


@dataclass(frozen=True)
class GitHubCandidate:
    owner: str
    repo: str
    commit: str
    license: str
    updated_at: str
    html_url: str


def candidate_report(candidate: GitHubCandidate) -> dict:
    return {**asdict(candidate), 'status': 'metadata_only', 'can_install': False, 'requires': ['review source files', 'verify license and dependencies', 'run isolated tests', 'human deployment approval']}


def fetch_github_metadata(repository: str, *, allow_network: bool=False) -> dict:
    """Explicit opt-in public metadata only. No fetching code, no writes, no install."""
    if not allow_network:
        raise PermissionError('Kết nối mạng cần --allow-network')
    if not re.fullmatch(r'[A-Za-z0-9_.-]{1,80}/[A-Za-z0-9_.-]{1,80}', repository):
        raise ValueError('Tên repo phải theo dạng owner/repo')
    url = 'https://api.github.com/repos/' + repository
    req = urllib.request.Request(url, headers={'Accept':'application/vnd.github+json','User-Agent':'HPCoreEvolutionMVP/0.1','X-GitHub-Api-Version':'2022-11-28'})
    with urllib.request.urlopen(req, timeout=8) as resp:
        if resp.status != 200:
            raise RuntimeError('API không trả 200')
        raw = resp.read(131073)
        if len(raw) > 131072:
            raise ValueError('Phản hồi vượt giới hạn dữ liệu')
    data=json.loads(raw)
    return candidate_report(GitHubCandidate(
        owner=str(data.get('owner',{}).get('login','')),
        repo=str(data.get('name','')),
        commit='not_verified',
        license=str((data.get('license') or {}).get('spdx_id','unknown')),
        updated_at=str(data.get('pushed_at','')),
        html_url=str(data.get('html_url','')),
    ))


def search_github_repositories(query: str, *, allow_network: bool=False, limit: int=5) -> list[dict]:
    """Read-only research discovery (no source review, clone, installation or execution)."""
    if not allow_network:
        raise PermissionError('Kết nối mạng cần --allow-network')
    if not 2 <= len(query) <= 120 or any(ord(c) < 32 for c in query):
        raise ValueError('Truy vấn không hợp lệ')
    if not 1 <= limit <= 10:
        raise ValueError('Giới hạn từ 1 đến 10')
    parameters = urllib.parse.urlencode({'q': query, 'per_page': limit})
    url = 'https://api.github.com/search/repositories?' + parameters
    request = urllib.request.Request(url, headers={'Accept': 'application/vnd.github+json', 'User-Agent':'HPCoreEvolutionMVP/0.1', 'X-GitHub-Api-Version':'2022-11-28'})
    with urllib.request.urlopen(request, timeout=8) as response:
        raw = response.read(512001)
        if len(raw) > 512000:
            raise ValueError('Phản hồi vượt giới hạn dữ liệu')
    results = json.loads(raw).get('items', [])
    if not isinstance(results, list):
        raise ValueError('Phản hồi API không hợp lệ')
    return [candidate_report(GitHubCandidate(
        owner=str((item.get('owner') or {}).get('login', '')),
        repo=str(item.get('name','')),
        commit='not_verified',
        license=str((item.get('license') or {}).get('spdx_id', 'unknown')),
        updated_at=str(item.get('pushed_at','')),
        html_url=str(item.get('html_url','')),
    )) for item in results[:limit] if isinstance(item,dict)]
