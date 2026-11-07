#!/usr/bin/env python3
"""Offline tests against source tree, candidates and sha256 manifest. No network or plugin runtime."""
from pathlib import Path
from zipfile import ZipFile
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
items=json.loads((ROOT/'migration/MANIFESTS/PLUGIN_EXPORT_MATRIX.json').read_text(encoding='utf-8'))
errors=[]; checks=0

def require(p,why):
 global checks
 checks+=1
 if not p: errors.append(why)

require(len(items)==17,'17 owned plugin entries')
for p in items:
 name=p['name']; asset=p.get('import_file')
 if not asset:
  require(name=='dev-8e2c158c632881918d6f75b1f38a2f7d','Missing portable archive without Site provenance')
  continue
 f=ROOT/'packages'/Path(asset).name
 require(f.is_file(),f'Package missing: {name}')
 if not f.is_file():continue
 with ZipFile(f) as z:
  require(z.testzip() is None,f'CRC failed: {name}')
  manifest=json.loads(z.read('plugin.json'))
  require(manifest['name']==name and manifest['version']==p['source_version'],f'Manifest identity drift: {name}')
  for member in z.infolist():
   if member.is_dir(): continue
   path=ROOT/'plugins'/name/member.filename
   require(path.is_file(),f'Unpacked missing: {name}/{member.filename}')
   if path.is_file():require(hashlib.sha256(z.read(member)).digest()==hashlib.sha256(path.read_bytes()).digest(),f'Unpacked modified: {name}/{member.filename}')
   require('..' not in Path(member.filename).parts and not member.filename.startswith('/'),f'Unsafe zip entry: {member.filename}')
  require(len([s for s in z.namelist() if re.fullmatch(r'skills/[^/]+/SKILL.md',s)])==p['portable_skill_count'],f'Skill count mismatch: {name}')

manifest=ROOT/'SHA256SUMS.txt'
if manifest.is_file():
 for line in manifest.read_text(encoding='utf8').splitlines():
  if not line.strip():continue
  digest,path=line.split('  ',1)
  f=ROOT/path
  require(f.is_file(),f'Missing SHA file: {path}')
  if f.is_file(): require(hashlib.sha256(f.read_bytes()).hexdigest()==digest,f'SHA mismatch: {path}')
print(json.dumps({'status':'PASS' if not errors else 'FAIL','checks':checks,'errors':errors[:30], 'scope':'OFFLINE_STATIC_ONLY','github_remote_created':False,'chatgpt_target_import':'NOT_TESTED'},ensure_ascii=False,indent=2))
sys.exit(bool(errors))
