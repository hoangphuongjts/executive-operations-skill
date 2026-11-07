# Hồ sơ nguồn — Claude Code Video Toolkit VN

Ngày kiểm tra: 2026-11-05.

- Upstream: https://github.com/wilwaldon/Claude-Code-Video-Toolkit
- Branch: main
- Commit: a6e9e5225d85585472666598297f47d9584f9a97 (2026-02-26T00:36:16Z)
- README blob SHA: 57220d0a9b0ebc88c726578b1f11747c2de25ae8
- Tree root được connector trả về gồm đúng một file `README.md`.
- GitHub repository metadata trả `license=null`. README nhắc `MIT` và trỏ `LICENSE`, nhưng root không có LICENSE. Chưa xác minh quyền tái phân phối README; Skill này được viết mới và chỉ tham chiếu URL/tóm tắt.
- Bản chất nguồn: danh mục 8 công cụ với đường dẫn trỏ tới upstream khác; không có mã engine/runner/dependency manifest trong repo root.
- Đã xem: metadata repo, 1 commit, root file list và toàn bộ README. Chưa tiến hành audit code hay license của 8 công cụ riêng, không chạy install hooks, package manager, test render hay benchmark.
- Phạm vi tích hợp đề xuất: plugin Skill tham chiếu, không sao chép source upstream và không cấp quyền thực thi.
- Chính sách trạng thái: `metadata_checked` cho repo danh mục, `reference_skill_packaged` cho adapter, không đánh dấu `source_audited` cho mọi repo được liên kết.
- Tài sản có trước: giữ nguyên toàn bộ; không thay đổi thiết lập điều khiển CLI/MCP.
