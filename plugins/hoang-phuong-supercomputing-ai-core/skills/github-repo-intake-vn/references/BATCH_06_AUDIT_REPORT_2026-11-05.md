# Báo cáo kiểm tra batch 06 — 2026-11-05

Đã xử lý tuần tự Cụm 1, hạng 17–20 tại commit đã ghim. Cả bốn repo bị loại khỏi Cụm 1 vì giấy phép, chức năng hoặc dependency không phù hợp. Không có mã upstream nào được chạy, nhập hoặc cài.

| Hạng | Repo / commit | License | Kết luận |
|---:|---|---|---|
| 17 | [tondevrel/scientific-agent-skills](https://github.com/tondevrel/scientific-agent-skills/commit/6e89d9e8c84188050bd50c420e48b639be484bb9) | MIT ở root; BSD-3-Clause trong skill PyTorch | Bộ sưu tập 62 SKILL.md chủ yếu là hướng dẫn thư viện khoa học. Skill `pytorch-research` thiên về kỹ thuật PyTorch và có xung đột license giữa manifest nội bộ với LICENSE gốc; không nhập. Repository không có mã Python chạy kèm các skill, nhưng có cấu hình plugin/MCP; không kích hoạt. |
| 18 | [chinhproductivity/folder-organization-skill](https://github.com/chinhproductivity/folder-organization-skill/commit/21ad09a712ec6243d6713de9a09c75f002c99469) | Không khai báo | Skill tổ chức folder/file, lệch chức năng Cụm 1. Pinned tree không có LICENSE hoặc manifest dependency. Không nhập. |
| 19 | [Dsadd4/AgentFigureGallery](https://github.com/Dsadd4/AgentFigureGallery/commit/0b55f26fd575a00b5ebacb619d953b0a008e0126) | MIT | Trùng mục đích với hai skill lập kế hoạch hình đã có. CLI cần Python 3.10+ và kho tham chiếu ngoài; installer có thể clone/pull, tạo venv, cài package và tải kho dữ liệu. Không chạy hoặc nhập. |
| 20 | [guhaohao0991/PaperClaw](https://github.com/guhaohao0991/PaperClaw/commit/39e819422747ec177edf68a842998e6f036f3df5) | Chưa xác minh: README gắn badge MIT nhưng pinned tree không có LICENSE | Skill tạo agent nghiên cứu OpenClaw, chồng lấn paper reading/literature review hiện có; ví dụ sử dụng API, ghi file và lịch tìm kiếm hằng ngày/hằng tuần. Script chỉ được xem tĩnh, không chạy hoặc nhập. |

## Giới hạn kiểm tra

Đã kiểm tra commit, license, dạng skill, trùng lặp và cấu hình/dependency liên quan đến ứng viên. Static triage trong phạm vi nêu trên không thay thế kiểm toán bảo mật toàn repo; do đó `source_code_audited` vẫn là `false` cho cả bốn dòng.
