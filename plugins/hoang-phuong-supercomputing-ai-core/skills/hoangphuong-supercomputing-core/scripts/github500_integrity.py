"""Local offline checksum utility for GitHub500 pilot. No network, no shell, no execution of repo contents."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys

EXCLUDE = {'.git','__pycache__','node_modules','.venv','.pytest_cache'}
SKIP_FILES={'INTEGRITY.json','.DS_Store','Thumbs.db'}

def _hash_bytes(data:bytes)->str:
    return hashlib.sha256(data).hexdigest()

def _validate_relative(path:str)->None:
    p=Path(path)
    if not path or p.is_absolute() or '..' in p.parts or p.as_posix()!=path or chr(92) in path:
        raise ValueError('unsafe relative path')

def snapshot(root:Path)->dict:
    root=Path(root)
    if not root.is_dir() or root.is_symlink():
        raise ValueError('root must be an existing real directory')
    out={}
    for p in sorted(root.rglob('*')):
        rel=p.relative_to(root)
        if any(part in EXCLUDE for part in rel.parts):
            continue
        if p.is_symlink():
            raise ValueError(f'symlink rejected: {rel.as_posix()}')
        if not p.is_file() or p.name in SKIP_FILES:
            continue
        key=rel.as_posix()
        _validate_relative(key)
        out[key]=_hash_bytes(p.read_bytes())
    digest=_hash_bytes(json.dumps(out,sort_keys=True,separators=(',',':')).encode('utf-8'))
    return {'schema_version':1,'algorithm':'sha256','file_count':len(out),'files':out,'manifest_digest':digest}

def verify(root:Path, manifest:dict)->dict:
    if manifest.get('schema_version')!=1 or manifest.get('algorithm')!='sha256':
        raise ValueError('unsupported manifest')
    recorded=manifest.get('files')
    if not isinstance(recorded,dict):
        raise ValueError('invalid files field')
    if manifest.get('file_count')!=len(recorded):
        raise ValueError('invalid file count')
    for rel,h in recorded.items():
        _validate_relative(rel)
        if not isinstance(h,str) or len(h)!=64 or any(c not in '0123456789abcdef' for c in h):
            raise ValueError('invalid SHA-256 digest')
    expected=_hash_bytes(json.dumps(recorded,sort_keys=True,separators=(',',':')).encode('utf-8'))
    if manifest.get('manifest_digest')!=expected:
        raise ValueError('manifest digest mismatch')
    cur=snapshot(root)['files']
    old=set(recorded);new=set(cur)
    errors={'missing':sorted(old-new),'added':sorted(new-old),'modified':sorted(k for k in old&new if recorded[k]!=cur[k])}
    return {'passed':not any(errors.values()),'errors':errors,'compared':len(old)}

def main(argv=None)->int:
    parser=argparse.ArgumentParser(description='Offline checksum audit; no network')
    sub=parser.add_subparsers(dest='cmd',required=True)
    for x in ('snapshot','verify'):
        p=sub.add_parser(x)
        p.add_argument('--root',required=True)
        p.add_argument('--output' if x=='snapshot' else '--manifest',required=True)
    args=parser.parse_args(argv)
    try:
        if args.cmd=='snapshot':
            doc=snapshot(Path(args.root))
            output=Path(args.output)
            if output.is_symlink():raise ValueError('manifest output cannot be a symlink')
            output.write_text(json.dumps(doc,indent=2,sort_keys=True)+'\n',encoding='utf-8')
            print(json.dumps({'status':'snapshot_created','file_count':doc['file_count']}))
            return 0
        doc=json.loads(Path(args.manifest).read_text(encoding='utf-8'))
        res=verify(Path(args.root),doc)
        print(json.dumps(res))
        return 0 if res['passed'] else 1
    except (OSError,ValueError,json.JSONDecodeError) as e:
        print(json.dumps({'status':'error','reason':str(e)}),file=sys.stderr)
        return 2
if __name__=='__main__':
    raise SystemExit(main())
