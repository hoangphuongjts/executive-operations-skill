---
name: github500-architecture-blueprint
description: "Dùng khi nghiên cứu codebase và lập sơ đồ, ranh giới module, API, luồng dữ liệu và phương án mở rộng kiến trúc phần mềm."
---

# Github 500 — Architecture Blueprint

**Chế độ:** embedded_skill_guidance. **Nguồn phương pháp:** [github/awesome-copilot](https://github.com/github/awesome-copilot/blob/main/skills/architecture-blueprint-generator/SKILL.md). Không chạy mã hoặc gọi API ngoài theo mặc định.

## Phân tích kiến trúc dựa trên mã thật
1. Kiểm kê repo/đầu vào được cung cấp: file manifests, lockfiles, directories, imports và cấu hình chạy; phân biệt tệp đã đọc với tệp chưa có quyền truy cập.
2. Mô tả AS-IS (kiến trúc quan sát được) trước TO-BE (đề xuất), không suy đoán mô-đun tồn tại chỉ từ tên.
3. Xác định domain modules, dependency direction, boundaries, data flow, storage, auth, secrets, error handling, observability, versioning và deployment.
4. Vẽ sơ đồ C4-lite bằng Mermaid hoặc Markdown, kèm API contracts, trust boundaries và bảng rủi ro.
5. Kiểm tra circular dependencies, cohesion, coupling, backward compatibility, scalability và các trade-off thực tế.
6. Ghi ADR ngắn cho quyết định quan trọng: context, alternatives, decision, consequences, test criteria.
7. Chỉ tuyên bố `verified_by_runtime` khi có code/test/build thật; nếu không có repo hoặc quyền đọc thì tạo kiến trúc mẫu với nhãn `proposed`.

**Bàn giao**: AS-IS, TO-BE, diagram, interfaces, risks, phased rollout, tests, rollback. Không tự cài dependencies hay khởi động local server khi chỉ yêu cầu tư vấn.

## Kiểm tra bằng chứng và tích hợp
Đây là Skill hướng dẫn đã viết lại cho ChatGPT; các đoạn mã ở repo gốc và công cụ tùy chọn **không** được sao chép, cài hay chạy. Không đọc 500 hồ sơ cùng lúc. Khi cần, liên kết chuyên gia Core và các Skill khác theo tác vụ.

Xem `references/PROVENANCE.md`.
