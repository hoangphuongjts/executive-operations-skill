---
name: nango-video-ai-vn
description: Dùng khi người dùng muốn bổ sung Nango vào hệ thống VIDEO AI, n8n, Google Drive, YouTube, TikTok, Facebook, Gemini, HyperFrames hoặc MoneyPrinter mà không thay thế module đang chạy.
---

# Nango và hệ thống VIDEO AI

## Sơ đồ mức khái niệm
ChatGPT / AI Agent → Nango management cấu hình hoặc runtime tool calling → API đích (được người dùng ủy quyền) → dữ liệu/trạng thái theo dõi.
Riêng render video chạy tại hệ thống HyperFrames/Herk Edit Kit/Video ShotCraft hoặc engine khác. Nango không phải engine dựng MP4, không có quyền mặc định vào ổ `C:\AI-VIDEO` trên máy Windows.

## Quy tắc tích hợp
- Không thay thế hoặc cài đè `C:\AI-VIDEO` hay cấu hình/plugin sẵn có.
- Chia 2 giai đoạn: khám phá & kết nối chỉ-đọc; sau khi duyệt mới bật các action ghi dữ liệu.
- Ưu tiên lưu nội dung nháp lên Drive qua phương thức đã được ủy quyền; đảm bảo dùng tài nguyên có quyền thương mại.
- Đăng YouTube/TikTok/Facebook chỉ khi được người dùng phê duyệt từng nội dung, nền tảng và tài khoản. Không dùng cookie session để né API chính thức.
- Nango không cấp thêm quyền cho tài khoản Google/Meta/TikTok; mỗi dịch vụ phải được ủy quyền riêng qua cơ chế hỗ trợ.
- Đối chiếu logs/IDs/tình trạng trước khi báo một hành động thành công.
