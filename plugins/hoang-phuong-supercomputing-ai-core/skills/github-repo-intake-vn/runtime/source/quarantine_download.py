"""Download a pinned GitHub source archive into quarantine ONLY. No extraction/execution."""
from __future__ import annotations
import argparse, hashlib, json, os, pathlib, re, tempfile, urllib.request, zipfile

REPO = re.compile(r'^[A-Za-z0-9_.-]{1,100}/[A-Za-z0-9_.-]{1,100}$')
SHA = re.compile(r'^[a-fA-F0-9]{40}$')
MAX_ARCHIVE = 40 * 1024 * 1024

def validate(repo: str, commit: str) -> None:
    if not REPO.fullmatch(repo) or '..' in repo or not SHA.fullmatch(commit):
        raise ValueError('Exact owner/repo and 40-character commit SHA required')

def archive_url(repo: str, commit: str) -> str:
    validate(repo,commit)
    return f'https://api.github.com/repos/{repo}/zipball/{commit}'

def download(repo: str, commit: str, output: pathlib.Path, opener=None, limit=MAX_ARCHIVE):
    validate(repo, commit)
    output = pathlib.Path(output)
    if output.exists():
        raise FileExistsError('Refuse overwriting a previously captured archive')
    if output.suffix.lower() != '.zip':
        raise ValueError('Output must be a .zip file')
    if output.parent.is_symlink():
        raise ValueError('Output parent cannot be a symlink')
    output.parent.mkdir(parents=True, exist_ok=True)
    opener = opener or urllib.request.urlopen
    req=urllib.request.Request(archive_url(repo,commit),headers={'User-Agent':'hpcore-github-intake/0.1','Accept':'application/vnd.github+json'})
    fd,tmp=tempfile.mkstemp(prefix='.hpcore-',suffix='.tmp',dir=output.parent)
    total=0; digest=hashlib.sha256()
    try:
        with os.fdopen(fd,'wb') as dest, opener(req,timeout=30) as response:
            final_url=response.geturl() if hasattr(response,'geturl') else archive_url(repo,commit)
            from urllib.parse import urlparse
            host=urlparse(final_url).hostname
            if host not in {'api.github.com','codeload.github.com'}:
                raise ValueError('Unexpected redirect host')
            while True:
                block=response.read(min(65536,limit-total+1))
                if not block: break
                total+=len(block)
                if total>limit: raise ValueError('Archive exceeds maximum size')
                digest.update(block); dest.write(block)
        if not zipfile.is_zipfile(tmp):raise ValueError('Response is not a ZIP archive')
        with zipfile.ZipFile(tmp) as z:
            members=z.infolist()
            if len(members)>10000:raise ValueError('Archive has too many entries')
            total_raw=0
            for m in members:
                rel=pathlib.PurePosixPath(m.filename)
                if m.filename.startswith('/') or '..' in rel.parts or '\\' in m.filename:
                    raise ValueError('Unsafe ZIP entry path')
                total_raw+=m.file_size
                if total_raw>500*1024*1024:raise ValueError('Archive uncompressed size exceeds limit')
        os.replace(tmp,output)
    finally:
        if os.path.exists(tmp):os.unlink(tmp)
    return {'repository':repo,'commit':commit.lower(),'archive':str(output),'sha256':digest.hexdigest(), 'size_bytes':total,'status':'QUARANTINED_UNTRUSTED_NOT_INSTALLED','execution':'never'}

def main():
    parser=argparse.ArgumentParser(description='Download pinned GitHub ZIP to quarantine; never execute or extract.')
    parser.add_argument('--repo',required=True)
    parser.add_argument('--commit',required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result=download(args.repo,args.commit,pathlib.Path(args.output))
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
