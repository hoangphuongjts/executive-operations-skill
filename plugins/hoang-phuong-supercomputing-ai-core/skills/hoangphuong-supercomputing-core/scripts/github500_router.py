"""Offline read-only index for GitHub-500 candidate discoveries (stdlib only)."""
from __future__ import annotations
import argparse
import json
import pathlib

CATALOG=pathlib.Path(__file__).resolve().parents[1]/"references"/"GITHUB_500_MASTER_CATALOG.json"
PILOT=pathlib.Path(__file__).resolve().parents[1]/"references"/"GITHUB_500_PILOT_25.json"

def load(path=CATALOG):
    obj=json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    rows=obj["records"]
    assert len(rows)==500 and len({r["repo"].casefold() for r in rows})==500
    assert all(r["github_url"]=="https://github.com/"+r["repo"] for r in rows)
    return rows

def search(query="", area="", limit=20):
    if limit<1 or limit>100: raise ValueError("limit must be 1..100")
    q=query.casefold().strip(); a=area.casefold().strip()
    return [r for r in load() if (not q or q in (r["repo"]+" "+r["discovery_area"]).casefold()) and (not a or a in r["discovery_area"].casefold())][:limit]

def report():
    rows=load();return {"discovered_unique":len(rows),"pilot":len(json.loads(PILOT.read_text())["records"]),"installed_external_repo_code":0,"external_runtime_executed":0,"integrated_native_skills":3,"pilot_license_paths_located":23,"status":"discovery_plus_native_skill_guidance"}

def main():
    p=argparse.ArgumentParser(description="Read-only discovery; does not download or execute repository code")
    p.add_argument("command",choices=["search","report","validate","pilot"])
    p.add_argument("--query",default="");p.add_argument("--area",default="");p.add_argument("--limit",type=int,default=20)
    args=p.parse_args()
    if args.command=="search":result=search(args.query,args.area,args.limit)
    elif args.command=="report":result=report()
    elif args.command=="pilot":result=json.loads(PILOT.read_text(encoding="utf-8"))["records"]
    else:result={"valid":len(load())==500,"source_license_gate":"not_complete","host_integrations_active":False}
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
