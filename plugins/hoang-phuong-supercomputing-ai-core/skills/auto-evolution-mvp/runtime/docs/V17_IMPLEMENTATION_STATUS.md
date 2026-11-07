# v17 Autonomous Evolution — kế hoạch có kiểm chứng

**Ngày:** 2026-11-05. **Bản triển khai:** Auto-Evolution Engine MVP 0.2.0, Plugin 16.0.8 (nếu bản vá tài khoản được chấp nhận).

## 8 vai trò và ranh giới thực thi

| Vai trò v17 | Trạng thái hiện tại | Bằng chứng / ranh giới |
|---|---|---|
| 01 Capability Discovery | Implemented offline | `scan_skills`, CLI `cycle`, chỉ skill local một cấp |
| 02 Weakness Detector | Implemented basic heuristic | `diagnose`: name, description, verification, Python tests; **không đo trí thông minh** |
| 03 Global Research | Network-opt-in metadata | `discover/research`, GitHub public API; **không quét toàn cầu, không tải repo** |
| 04 Socratic Critic | Prompt / role guidance | Chưa là subprocess / model riêng |
| 05 Architecture Designer | Prompt / role guidance | Chưa tự sinh kiến trúc qua LLM |
| 06 Code & Integration Engineer | Constrained patch prototype | Stage/apply chỉ bổ sung mục tài liệu định sẵn, không tự viết code |
| 07 Evaluation & Security Auditor | Implemented offline evidence gate | `evaluation.py` so sánh cùng frozen dataset, chặn regressed tasks/security blockers; không chứng thực reviewer ngoài |
| 08 Evolution Controller | Implemented gated local CLI | scan → proposal → stage → explicit approval → apply/restore; review record không cho phép deploy |

Không thành phần nào nói trên đã chứng minh là **Agent LLM độc lập**. Không có scheduler, API-key manager, tự huấn luyện, tự cài GitHub, GitHub Actions live hoặc triển khai server.

## Top 3 điểm yếu (kiểm toán dựa trên mã và Skill hiện có)

1. **Chất lượng suy luận thiếu benchmark thật:** bộ kiểm kê chỉ dựa cấu trúc file; cần tập nhiệm vụ thật độc lập và đo với model backend. Trạng thái: chưa giải quyết hoàn toàn.
2. **Thiếu cổng đánh giá/so sánh để tránh lùi chất lượng:** trước 0.2.0 không có module đối chiếu baseline/candidate bằng cùng dataset + fail closed; **đã bổ sung mã và 11 test offline**.
3. **Không có runtime nghiên cứu + build + deploy tự trị:** GitHub integration mới là metadata opt-in, patch chỉ sửa doc; production/ChatGPT update vẫn dùng quyền host và quy trình riêng. Trạng thái: blocked by runtime/auth/eval resources.

## Triển khai kế tiếp

- B1: Kết nối model API có quyền, budget, egress allowlist, sandbox độc lập, tuyệt đối không đưa secrets vào prompt.
- B2: Thu thập bộ benchmark hold-out thật, reviewer độc lập, nguồn dữ liệu và provenance log có thể xác minh; không dùng JSON tự khai là bằng chứng mạnh.
- B3: CI gate chạy test, regression, dependency/security scan, license review, provenance checks, build package; phát hành chỉ với explicit host approval.
- B4: Scheduler nếu người dùng thiết lập; chỉ chạy scan/report mặc định; không tự phát hành.

## Điểm nghiệm thu

- 27/27 unit tests offline (16 bộ cũ + 11 bộ mới) trong sandbox hiện tại; compilation OK.
- Đã chạy một demo tổng hợp 5 task với kết quả 3→4; các con số này là dữ liệu ví dụ, **không phải hiệu năng AI**.
- `candidate_review_*.json` có `can_deploy: false` ngay cả khi qua gate.
- Nâng phiên bản gói plugin là thay đổi metadata/Skill, **không đồng nghĩa runtime tự động đã chạy**.
