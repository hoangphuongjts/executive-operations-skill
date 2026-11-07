# Sử dụng Content AI Việt Nam trên Gemini

Đây là **hướng dẫn kèm ngay trong plugin**, để lần xuất Gemini sau không còn cần ghép thủ công. Phiên bản plugin: 0.3.3.

## Gemini Web / Gems
1. Truy cập `https://gemini.google.com`, mở Gems và tạo Gem mới.
2. Sao chép nguyên `gemini/GEM_INSTRUCTIONS.txt` vào trường Instructions.
3. Thêm các tài liệu skill/Knowledge do người dùng được quyền truy cập. Nếu sử dụng bản Google Drive từ lần xuất trước, đảm bảo nguồn đã cập nhật cùng phiên bản; tài liệu cũ không tự đổi khi plugin cập nhật.
4. Xem thử, lưu Gem; không giả định các plugin/API/MCP ChatGPT được chuyển theo.

## Gemini CLI
1. Trong gói xuất tương thích CLI, giữ `.gemini/skills/` và tệp `GEMINI.md` ở gốc dự án.
2. Mở Gemini CLI trong dự án, kiểm tra kỹ năng với `/skills list`, reload nếu cần.
3. Không chạy script chưa kiểm tra, không chép token/private keys vào Knowledge.

## Khi cần cả hai bộ
Gói hợp nhất chứa hướng dẫn phối hợp riêng và skill của cả hai plugin, không ghi đè các file khác nhau. Đọc `gemini/EXPORT_POLICY.md`.

## Giới hạn
Đóng gói không đồng nghĩa đã cài và chạy trên tài khoản Gemini. Công cụ dựng MP4, TTS, kết nối tài khoản, analytics và đăng bài đều cần xác thực năng lực/quyền thực tế.
