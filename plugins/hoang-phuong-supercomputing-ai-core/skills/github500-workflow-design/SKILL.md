---
name: github500-workflow-design
description: "Dùng khi người dùng muốn biến tác vụ lặp lại hoặc video thao tác thành bản thiết kế workflow tự động hóa n8n, Make, Python hay công cụ được kết nối."
---

# Github 500 — Workflow Design

**Chế độ:** embedded_skill_guidance. **Nguồn phương pháp:** [github/awesome-copilot](https://github.com/github/awesome-copilot/blob/main/skills/automate-this/SKILL.md). Không chạy mã hoặc gọi API ngoài theo mặc định.

## Workflow tương thích ChatGPT
1. Xác định thao tác bắt đầu/kết thúc, trigger, tần suất, quyền nguồn dữ liệu và ngoại lệ; nếu có video/screenshot chỉ phân tích nội dung thực tế được cung cấp.
2. Viết lại quy trình hiện tại thành các bước có `input → action → output` và phân loại thao tác người dùng / xử lý dữ liệu / gọi API / phê duyệt.
3. Chọn hình thức **no-code**, **low-code** hoặc **script** theo công cụ host sẵn có; không giả định đã có ffmpeg, Whisper, n8n, browser hoặc quyền hệ thống.
4. Thiết kế DAG, retry/backoff, idempotency, checkpoint, rate limiting, secret handling, logging và đường rollback.
5. Các thao tác gửi công khai, sửa/xóa, chuyển tiền, thay đổi dữ liệu chỉ chạy nếu được người dùng cho phép cụ thể và công cụ có khả năng xác thực.
6. Tạo sơ đồ workflow bằng Markdown/Mermaid, JSON mẫu có phân biệt giả lập, bảng mapping từng node và kế hoạch test âm tính.
7. Khi được yêu cầu triển khai và có công cụ, thực hiện trên môi trường thực và ghi `tested`; nếu chưa có, giao bản thiết kế với nhãn `not_deployed`.

**Kết quả**: mục tiêu, trigger, nodes, inputs, outputs, dependencies, costs, rollback, trạng thái từng node. Không tự chạy cron, server, Docker hoặc API ngoài.

## Kiểm tra bằng chứng và tích hợp
Đây là Skill hướng dẫn đã viết lại cho ChatGPT; các đoạn mã ở repo gốc và công cụ tùy chọn **không** được sao chép, cài hay chạy. Không đọc 500 hồ sơ cùng lúc. Khi cần, liên kết chuyên gia Core và các Skill khác theo tác vụ.

Xem `references/PROVENANCE.md`.
