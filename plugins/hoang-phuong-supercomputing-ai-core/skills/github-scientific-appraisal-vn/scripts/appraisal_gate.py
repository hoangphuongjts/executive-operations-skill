"""Offline structural audit for research claims; not a scientific quality score.

Safely checks the completeness of a bounded JSON record. It does not run code,
fetch URLs, verify cited evidence or make decisions about the truth of claims.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

MAX_BYTES = 2_000_000
MAX_CLAIMS = 1000
ALLOWED_TYPES = {'descriptive', 'predictive', 'causal'}
REQUIRED = ('id', 'claim', 'source_locator', 'study_design', 'outcome', 'sample_size', 'uncertainty', 'claim_type', 'reviewer')
OBSERVATIONAL = {'observational', 'cross-sectional', 'case-control', 'cohort', 'survey', 'case_series'}

def inspect_claims(payload: object) -> dict:
    if not isinstance(payload, list) or len(payload) > MAX_CLAIMS:
        raise ValueError('Expected an array of <= 1000 claim records')
    alerts = []
    seen = set()
    for i, item in enumerate(payload):
        if not isinstance(item, dict):
            raise ValueError(f'Claim {i} must be an object')
        ident = item.get('id')
        if not isinstance(ident, str) or not ident.strip() or len(ident)>128:
            raise ValueError(f'Claim {i} needs a short text id')
        if ident in seen:
            raise ValueError(f'Duplicate id: {ident}')
        seen.add(ident)
        for field in REQUIRED:
            value = item.get(field)
            if value is None or (isinstance(value, str) and not value.strip()):
                alerts.append({'id': ident, 'code': 'MISSING_FIELD', 'field': field})
        typ = item.get('claim_type')
        if typ is not None and typ not in ALLOWED_TYPES:
            alerts.append({'id': ident, 'code': 'INVALID_CLAIM_TYPE', 'field': 'claim_type'})
        if typ == 'causal' and str(item.get('study_design', '')).strip().lower() in OBSERVATIONAL:
            alerts.append({'id': ident, 'code': 'CAUSAL_INFERENCE_LIMIT', 'field': 'study_design'})
        n = item.get('sample_size')
        if isinstance(n, bool) or (n is not None and (not isinstance(n, int) or n < 1)):
            alerts.append({'id': ident, 'code': 'INVALID_SAMPLE_SIZE', 'field': 'sample_size'})
    return {'status':'STRUCTURAL_REVIEW_ONLY', 'count':len(payload), 'findings':alerts,
            'scientific_validity_verified':False, 'external_access':False}

def audit_file(input_path: Path, output_path: Path|None=None) -> dict:
    path = Path(input_path)
    if path.stat().st_size > MAX_BYTES:raise ValueError('Input exceeds 2 MB')
    result = inspect_claims(json.loads(path.read_text(encoding='utf-8')))
    if output_path is not None:
        dest=Path(output_path)
        if dest.resolve() == path.resolve(): raise ValueError('Refuse to overwrite the input')
        if dest.exists(): raise FileExistsError('Refuse to overwrite existing report')
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return result

def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument('input', type=Path)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    print(json.dumps(audit_file(args.input,args.output),ensure_ascii=False,indent=2))
if __name__=='__main__':main()
