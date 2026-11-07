---
name: github500-agent-governance
description: "Dùng để quản trị quyền, phê duyệt thao tác và kiểm toán khi AI Agent cần truy cập công cụ, dữ liệu hoặc phối hợp nhiều agent."
---

# Github 500 — Agent Governance

**Chế độ:** embedded_skill_guidance. **Nguồn phương pháp:** [github/awesome-copilot](https://github.com/github/awesome-copilot/blob/main/skills/agent-governance/SKILL.md). Không chạy mã hoặc gọi API ngoài theo mặc định.

## Kết quả cần tạo
Một **bảng chính sách quyền**, danh sách rủi ro, cơ chế phê duyệt, kiểm soát chi phí và dấu vết kiểm toán có thể truy xuất.

## Quy trình
1. Liệt kê agent, công cụ, dữ liệu và hành động dự kiến. Ghi rõ nguồn quyền của từng công cụ; đừng suy đoán quyền chỉ từ tên.
2. Gắn hành động vào `read_only`, `write_reversible`, `write_irreversible`, `network`, `payment` hoặc `admin`; mặc định từ chối quyền chưa khai báo.
3. Áp dụng nguyên tắc **least privilege**: allowlist cho tài nguyên và đường dẫn, quota số lần gọi, timeout, bộ lọc dữ liệu nhạy cảm, giới hạn chi phí.
4. Với gửi email, đăng bài, mua hàng, xóa/sửa dữ liệu hay thao tác trên hệ thống ngoài, chỉ thực hiện khi người dùng cho phép và host thực sự cấp quyền.
5. Lập threat model cho prompt injection, data exfiltration, privilege escalation, mạo danh agent, replay và trạng thái lỗi.
6. Khi nhiều agent trao đổi, kiểm soát cả ủy quyền **giữa các agent**; agent được giao việc không được tự cấp quyền rộng hơn cho agent khác.
7. Tạo bảng log dự kiến: thời điểm, tool, lý do, quyền, tác động, yêu cầu phê duyệt, kết quả thực thi thật hoặc `not_executed`.
8. Đề xuất rollback/kill switch và thử các tình huống bị từ chối, thiếu xác thực, vượt quota trước khi sản xuất.

**Mẫu bàn giao**: Action | Scope | Tool thật | Permission | Approval | Evidence | Decision | Risk. Giữ nguyên `embedded_skills_only`; đây là policy hướng dẫn, không phải tường lửa thực thi.

## Kiểm tra bằng chứng và tích hợp
Đây là Skill hướng dẫn đã viết lại cho ChatGPT; các đoạn mã ở repo gốc và công cụ tùy chọn **không** được sao chép, cài hay chạy. Không đọc 500 hồ sơ cùng lúc. Khi cần, liên kết chuyên gia Core và các Skill khác theo tác vụ.

Xem `references/PROVENANCE.md`.
