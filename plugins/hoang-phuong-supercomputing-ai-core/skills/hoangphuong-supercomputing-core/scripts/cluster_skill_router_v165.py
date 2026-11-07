#!/usr/bin/env python3
"""Non-destructive, opt-in cluster classifier for Hoang Phuong Core.
It never installs, executes, or auto-updates untrusted skills or plugins.
"""
import argparse
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT.parents[1]
REGISTRY = ROOT / "references" / "CLUSTER_16_ASSET_REGISTRY.json"
CANDIDATES = ROOT / "references" / "GITHUB_16x24_CANDIDATES.json"

KEYWORDS = {
 1:["khoa hoc","scientific research","literature review","hypothesis","experiment design","trich dan","academic research"],
 2:["kien truc he thong","architecture","system design","distributed systems","api gateway","architecture blueprint"],
 3:["lap trinh","software engineer","codebase","coding","fullstack","unit test code","refactor","spec kit"],
 4:["kiem thu","testing","quality assurance","regression","property test","sast","test automation"],
 5:["hpc","performance benchmark","latency","cpu profiling","high performance computing","throughput"],
 6:["quantum","luong tu","cryptography","p2p encryption","homomorphic","quantum circuit"],
 7:["machine learning","algorithm","ai model","prompt engineering","model evaluation","deep learning"],
 8:["workflow","tu dong hoa","devops","operations","process automation","n8n","docker","coordination"],
 9:["user experience","ux","product management","seo","marketing","crm","sales","ecommerce","growth"],
 10:["data analytics","dataset","knowledge graph","rag","sql","retrieval","data science","customer support"],
 11:["ai agent","multi agent","agent framework","agent orchestration","tool connector","plugin","agent runtime"],
 12:["security","bao mat","legal compliance","policy","audit contract","prompt injection","risk compliance"],
 13:["video","content creation","social media","storyboard","music rights","voiceover","youtube","remotion"],
 14:["finance","dau tu","trading","financial","business strategy","accounting","cash flow","valuation"],
 15:["cad","3d printing","iot","agriculture","nong nghiep","livestock","hardware","farm management"],
 16:["benchmark evaluation","evaluation framework","release audit","quality gate","hallucination","test evaluation"]
}
def norm(s):
    return re.sub(r"\s+"," ", "".join(c for c in unicodedata.normalize("NFKD",s.lower()) if not unicodedata.combining(c))).strip()
def classify(text, known_id=None, registry_path=REGISTRY):
    data=json.loads(Path(registry_path).read_text(encoding="utf-8"))
    if known_id:
        found=[i for i in data["items"] if i["id"]==known_id]
        if found:
            return {"decision":"verified_existing_registry_mapping","cluster_id":found[0]["primary_cluster"],
                    "secondary_clusters":found[0]["secondary_clusters"],"item_id":known_id}
    q=norm(text)
    scores={k:sum(2 if " " in key else 1 for key in words if re.search(r"(?<![a-z0-9])"+re.escape(norm(key))+r"(?![a-z0-9])",q))
            for k,words in KEYWORDS.items()}
    high=max(scores.values(),default=0)
    matches=sorted(k for k,v in scores.items() if v==high and v>0)
    if high<2 or len(matches)!=1:
        return {"decision":"requires_human_review","cluster_id":None,
                "reason":"no_high_confidence_match_or_ambiguous","scores":{str(k):v for k,v in scores.items() if v>0}}
    primary=matches[0]
    secondary=[k for k,v in scores.items() if k!=primary and v>=2]
    return {"decision":"suggested_not_installed","cluster_id":primary,
            "secondary_clusters":secondary,"scores":{str(k):v for k,v in scores.items() if v>0}}
def validate():
    r=json.loads(REGISTRY.read_text(encoding="utf-8"))
    c=json.loads(CANDIDATES.read_text(encoding="utf-8"))
    assert len(r["clusters"])==16
    assert sorted(x["id"] for x in r["clusters"])==list(range(1,17))
    roles=[x for x in r["items"] if x["kind"]=="agent_role_profile"]
    assert len(roles)==128 and {x["id"] for x in roles}=={f"agent-{i:03d}" for i in range(1,129)}
    core=[x for x in r["items"] if x["kind"]=="core_skill"]
    overlays=[x for x in r["items"] if x["kind"]=="core_skill_overlay"]
    external=[x for x in r["items"] if x["kind"]=="external_personal_plugin"]
    skill_names={p.parent.name for p in (PLUGIN_ROOT/"skills").glob("*/SKILL.md")}
    core_ids=[x["id"] for x in core]
    assert len(core)==41 and len(set(core_ids))==41
    assert all(x.get("installed_in_core") is True for x in core)
    assert set(core_ids)<=skill_names
    assert len(overlays)==16 and len(external)==15
    records=c["records"]
    repo_cluster_pairs={(x["repo"].casefold(),x["cluster_id"]) for x in records}
    unique_repos={x["repo"].casefold() for x in records}
    assert len(records)==384 and len(repo_cluster_pairs)==384
    assert all(len([e for e in records if e["cluster_id"]==g])==24 for g in range(1,17))
    integrated=[x for x in records if x.get("installed") is True]
    assert len(integrated)==8
    assert all(x.get("integrated_core_skill") in skill_names for x in integrated)
    assert all(not x.get("source_code_audited",False) for x in integrated)
    return {"result":"passed","clusters":16,"role_profiles":128,"existing_skills":len(core),
            "proposed_new_skills":len(overlays),"github_candidate_records":len(records),
            "integrated_candidate_skills":len(integrated),"unique_github_repositories":len(unique_repos),
            "cross_cluster_duplicate_records":len(records)-len(unique_repos),"github_installed":0}

def audit_counts():
    r=json.loads(REGISTRY.read_text(encoding="utf-8"))
    c=json.loads(CANDIDATES.read_text(encoding="utf-8"))
    by_group={}
    for g in range(1,17):
        cur=sum(x["kind"]=="core_skill" and x["primary_cluster"]==g for x in r["items"])
        proposed=sum(x["kind"]=="core_skill_overlay" and x["primary_cluster"]==g for x in r["items"])
        accepted=sum(x.get("decision")=="approved_and_packaged" and x["cluster_id"]==g for x in c["records"])
        by_group[str(g)]={"existing_skills":cur,"overlay_proposed":proposed,"github_accepted":accepted,
                          "target":24,"remaining_after_overlay_if_published":max(0,24-cur-proposed)}
    return by_group
def scan_skill_tree(skill_root):
    """Read local SKILL.md files and propose classifications; no file mutation."""
    root=Path(skill_root)
    if not root.is_dir():
        raise ValueError("Skill root does not exist")
    output=[]
    for skill in sorted(root.glob("*/SKILL.md")):
        s=skill.read_text(encoding="utf-8",errors="replace")[:20000]
        name=skill.parent.name
        desc_match=re.search(r'^description:\s*(.*)$',s,re.M)
        desc=(desc_match.group(1) if desc_match else "")
        proposed=classify(" ".join([name,desc,s[:500]]),known_id=name)
        output.append({"skill":name,"path":str(skill),"classification":proposed})
    return output

def main():
    ap=argparse.ArgumentParser()
    sp=ap.add_subparsers(dest="cmd",required=True)
    sp.add_parser("validate");sp.add_parser("report")
    cl=sp.add_parser("classify");cl.add_argument("text");cl.add_argument("--known-id")
    sc=sp.add_parser("scan");sc.add_argument("--skill-root",required=True)
    args=ap.parse_args()
    if args.cmd=="validate":print(json.dumps(validate(),ensure_ascii=False))
    if args.cmd=="report":print(json.dumps(audit_counts(),ensure_ascii=False,indent=2))
    if args.cmd=="classify":print(json.dumps(classify(args.text,args.known_id),ensure_ascii=False,indent=2))
    if args.cmd=="scan":print(json.dumps(scan_skill_tree(args.skill_root),ensure_ascii=False,indent=2))
if __name__=="__main__":main()
