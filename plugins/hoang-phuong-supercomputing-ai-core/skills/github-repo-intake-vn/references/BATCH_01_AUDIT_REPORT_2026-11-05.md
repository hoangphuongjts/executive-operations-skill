# Batch 01 — 384 repo / skill candidates
Ngày đối chiếu: 2026-11-05

## Phạm vi và nguyên tắc
CSV được nêu trong yêu cầu không có tại /mnt/data; batch này dùng registry skills/hoangphuong-supercomputing-core/references/GITHUB_16x24_CANDIDATES.json trong plugin. Registry có 384 repo, chia 16 cụm × 24 vị trí. Repo là nguồn khám phá; mỗi Skill được chọn riêng. Không tải hoặc thực thi mã upstream trong batch này.

## Repo 1 — K-Dense-AI/scientific-agent-skills
- Branch main; commit đã ghim: [a25cf9ec00e2745d03f8704acf6f6919694ccd9a](https://github.com/K-Dense-AI/scientific-agent-skills/commit/a25cf9ec00e2745d03f8704acf6f6919694ccd9a), ngày 2026-11-02.
- Giấy phép tại commit: MIT, LICENSE.md, copyright K-Dense Inc. 2025.
- Cây nguồn: 177 SKILL.md, 776 tệp script, 5 manifest/dependency file; cây GitHub không bị cắt ngắn.
- Đã kiểm tra nội dung skill skills/research-grants/SKILL.md và các tài liệu tham chiếu về yêu cầu, cấu trúc, tiêu chí đánh giá và nguyên tắc viết.
- Skill được chọn: research-grant-proposal-vn, cụm 01. Đây là bản hướng dẫn tiếng Việt có provenance và giấy phép; thư mục nguồn đã chọn không có script hay manifest dependency.
- Không chép script, lệnh tải/cài package, API tạo hình hoặc quy định tài trợ cụ thể có thể lỗi thời. Mã còn lại trong repo chưa được kiểm toán toàn diện; không tính repo này là đã source-security-audited.

## Repo 2 — Tyche-MKR/scientific-agent-skills
- Branch main; commit: [4cdd606c79074c34322dd908caa03c26058e9c60](https://github.com/Tyche-MKR/scientific-agent-skills/commit/4cdd606c79074c34322dd908caa03c26058e9c60), ngày 2026-08-31.
- Giấy phép tại commit: MIT, cùng dòng copyright K-Dense Inc. 2025.
- Cây nguồn: 163 SKILL.md, 685 tệp script, 3 manifest/dependency file.
- So với repo 1, có 159 thư mục skill trùng tên; 0 trong 159 cặp SKILL.md có cùng blob SHA. Đây là mức trùng chức năng cao, chưa chứng minh nội dung giống hệt. Chưa cài; các skill duy nhất cần xét riêng.

## Repo 3 — K-Dense-AI/claude-skills-mcp
- Branch main; commit: [72a7b502237cb3e697d3944be1b778498eed2d87](https://github.com/K-Dense-AI/claude-skills-mcp/commit/72a7b502237cb3e697d3944be1b778498eed2d87), ngày 2026-07-20.
- Giấy phép Apache-2.0.
- Cây nguồn có 0 SKILL.md, 38 tệp mã/script và 4 manifest hoặc lockfile Python.
- Kết luận cho mục tiêu cài Skill: loại khỏi danh sách Skill vì đây là MCP server/ứng dụng độc lập, không phải gói Skill. Không cài dependencies hoặc chạy mã. Việc source-security audit của ứng dụng chưa thực hiện.

## Repo 4 — google-deepmind/science-skills
- Branch main; commit: [4de6786171f1479026da5d3a00f110703c8ba35e](https://github.com/google-deepmind/science-skills/commit/4de6786171f1479026da5d3a00f110703c8ba35e), ngày 2026-10-23.
- LICENSE ghi Apache-2.0 cho phần mềm và CC-BY cho tài liệu; SKILL_LICENSES.md nêu điều khoản dữ liệu bên thứ ba theo từng skill.
- Cây nguồn: 40 SKILL.md, 66 tệp script, 3 manifest pyproject.toml ở cấp skill.
- Chưa cài. Cần rà soát từng skill, scripts, API, dependencies và điều khoản dữ liệu trước khi chọn.

## Tình trạng sau khi đóng gói
- Skill mới từ registry: 1, thuộc cụm 01; đã gắn attribution và MIT notice.
- Repo được tích hợp một Skill: 1/384 sau khi release được Plugin Creator xác nhận.
- Repo bị loại khỏi tập Skill: 1 (repo 3, không có SKILL.md).
- Pending: 382 repo; trong đó repo 2 và 4 đã xem metadata/cấu trúc nhưng chưa hoàn tất source audit.
- Repo đã source-security-audited toàn diện: 0/384.
- Không có mã upstream được chạy hoặc đóng gói.
- Các số coverage cụm trong CLUSTER_16_STATUS.json tính Skill đã đăng ký; agent profile, 16 skill điều phối cụm, router mặc định và công cụ kiểm kê không được tính là Skill chuyên môn trong chỉ tiêu 24.