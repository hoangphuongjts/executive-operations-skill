#!/usr/bin/env python3
"""Re-run existing QA without executing any plugin program or calling external service."""
from pathlib import Path
from zipfile import ZipFile
import tempfile, subprocess,sys
base=Path(__file__).resolve().parents[1]
a=base/'archive'/'HoangPhuong_ChatGPT_Migration_STAGING_v2_2026-11-07.zip'
with tempfile.TemporaryDirectory(prefix='hpcore-qa-') as d:
    with ZipFile(a) as z:
        for x in z.infolist():
            pp=Path(x.filename)
            if pp.is_absolute() or '..' in pp.parts: raise ValueError('unsafe path')
        z.extractall(d)
    result=subprocess.run([sys.executable,str(Path(d)/'TESTS'/'QA_OFFLINE.py')],cwd=d)
    sys.exit(result.returncode)
