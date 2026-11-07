"""Command-line driver for the offline-first Auto-Evolution Engine."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from .evaluation import load_evidence, compare_runs, write_release_candidate
from .engine import (scan_skills, diagnose, create_proposals, stage_proposal, apply_proposal,
                     restore_backup, audit_tree, fetch_github_metadata, search_github_repositories, _write_json)


def parser():
    p=argparse.ArgumentParser(prog='hpcore-evolution',description='MVP kiểm toán / đề xuất / cập nhật Skill an toàn')
    p.add_argument('--root',required=True,help='Thư mục gốc chứa các thư mục con skill-name/SKILL.md')
    p.add_argument('--reports',required=True,help='Thư mục báo cáo, phải nằm ngoài root')
    sub=p.add_subparsers(dest='command',required=True)
    sub.add_parser('scan',help='Chỉ quét, không ghi vào mã nguồn')
    sub.add_parser('cycle',help='Quét, đánh giá và tạo proposal, KHÔNG tự áp dụng')
    q=sub.add_parser('stage',help='Tạo bản dự thảo cập nhật; không sửa nguồn')
    q.add_argument('proposal_id')
    q=sub.add_parser('apply',help='Sửa Skill trong nguồn, bắt buộc phê duyệt ID')
    q.add_argument('proposal_id');q.add_argument('--approve',required=True,help='Nhập chính xác proposal_id')
    q=sub.add_parser('restore',help='Khôi phục bản sao lưu, bắt buộc xác nhận')
    q.add_argument('backup_id');q.add_argument('--approve',required=True)
    sub.add_parser('audit',help='Xuất danh mục hash SHA256 toàn cây')
    q=sub.add_parser('research',help='Chỉ lấy metadata public GitHub; cần bật quyền mạng')
    q.add_argument('repository',help='owner/repo');q.add_argument('--allow-network',action='store_true')
    q=sub.add_parser('discover',help='Tìm repo metadata trên GitHub, chỉ khi bật mạng')
    q.add_argument('query',help='Từ khóa tra cứu');q.add_argument('--allow-network',action='store_true');q.add_argument('--limit',type=int,default=5)
    q=sub.add_parser('evaluate',help='So sánh 2 kết quả đánh giá có nguồn, KHÔNG triển khai')
    q.add_argument('--baseline',required=True,help='JSON baseline')
    q.add_argument('--candidate',required=True,help='JSON candidate')
    return p


def main(argv=None):
    args=parser().parse_args(argv)
    root=Path(args.root).expanduser().resolve(strict=True)
    reports=Path(args.reports).expanduser().resolve()
    if reports==root or reports.is_relative_to(root):
        parser().error('Reports phải nằm ngoài thư mục root')
    if args.command=='scan':
        answer={'status':'read_only_scan','skills':scan_skills(root)}
    elif args.command=='cycle':
        skills=scan_skills(root);issues=diagnose(skills);proposals=create_proposals(issues)
        answer={'status':'proposals_only_not_deployed','skills_scanned':len(skills),'issues':issues,'proposals':proposals,
                'important':'Các đánh giá chỉ dựa trên metadata và file; không đo trí thông minh mô hình.'}
        _write_json(reports/'inventory.json',{'skills':skills})
        _write_json(reports/'assessment.json',answer)
    elif args.command=='stage':
        proposals=create_proposals(diagnose(scan_skills(root)))
        match=next((x for x in proposals if x['id']==args.proposal_id),None)
        if match is None:raise ValueError('ID không còn hợp lệ hoặc không tồn tại')
        answer=stage_proposal(root,reports,match)
    elif args.command=='apply':
        answer=apply_proposal(root,reports,args.proposal_id,approval=args.approve)
    elif args.command=='restore':
        answer=restore_backup(root,reports,args.backup_id,approval=args.approve)
    elif args.command=='audit':
        answer=audit_tree(root);_write_json(reports/'integrity.json',answer)
    elif args.command=='evaluate':
        answer=compare_runs(load_evidence(args.baseline),load_evidence(args.candidate))
        _write_json(reports/'evaluation.json',answer)
        answer['release_review_file']=str(write_release_candidate(reports,answer))
    elif args.command=='research':
        answer=fetch_github_metadata(args.repository,allow_network=args.allow_network)
        _write_json(reports/'github_candidate.json',answer)
    elif args.command=='discover':
        answer={'status':'discovery_only_not_installed','candidates':search_github_repositories(args.query,allow_network=args.allow_network,limit=args.limit)}
        _write_json(reports/'github_discovery.json',answer)
    else:raise ValueError('Unknown command')
    print(json.dumps(answer,ensure_ascii=False,indent=2))
    return 0

if __name__=='__main__':raise SystemExit(main())
