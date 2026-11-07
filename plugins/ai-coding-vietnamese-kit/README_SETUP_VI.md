# AI Coding ChatGPT Plugin – hướng dẫn sử dụng

Bản đóng gói cá nhân từ `AI_Coding_ChatGPT_Kit.zip` trên Google Drive. Giữ nguyên file nguồn của bạn. Đây là gói plugin theo cấu trúc Agent Plugins portable, chưa được cài vào tài khoản ChatGPT.

**Gói này gồm**: 40 skill lập trình (đã thêm tiền tố vào tên để tránh trùng), 4 vai trò agent chuyển thành skill, 1 skill điều phối, 1 skill hướng dẫn thiết lập.

**Không bao gồm runtime trong plugin**: `aider.zip` và `mini-swe-agent.zip` có trong tệp ZIP gốc và cần được cài riêng trên máy hoặc trong môi trường an toàn. Việc cài plugin này không cài Python và không chạy agent nền.

## Cài đặt vào ChatGPT
- Nếu có quyền tạo plugin, cài Plugin Creator từ mục Plugins. Gửi cho Plugin Creator bản ZIP này hoặc thông tin trong `PROMPT_PLUGIN_CREATOR.txt` để tạo bản cá nhân; làm theo giao diện hiện có để xem lại và kích hoạt plugin.
- Nếu workspace cấp quyền **Upload plugin**, có thể dùng Admin Console > Plugins > Add > Upload plugin theo tài liệu OpenAI. Tài khoản cá nhân có thể không có mục upload; không thể ghi plugin trực tiếp vào tài khoản chỉ bằng cách đưa ZIP vào cuộc trò chuyện.
- Sau khi cài thành công, gọi `@ai-coding-vietnamese-kit` (hoặc tên mà giao diện hiển thị) và yêu cầu thiết lập.

## Kích hoạt kiểm tra
Yêu cầu: "Dùng AI Coding Kit phân tích một ứng dụng quản lý công việc, lập kế hoạch triển khai và chạy review bảo mật cho mô hình dữ liệu."

## Kiểm tra
- `plugin.json` ở thư mục gốc, `skills/<tên>/SKILL.md` cho từng skill.
- Tên skill được chuẩn hóa để tránh trùng và phù hợp cách định tuyến.
- Không có script tự khởi chạy, hook, MCP server, secret hoặc quyền hệ thống đi kèm.
- Mã nguồn trong file ZIP gốc chưa được thực thi và chưa được thẩm định sâu về bảo mật/chuỗi cung ứng.

Tài liệu tham khảo: https://developers.openai.com/plugins/build/plugins và https://help.openai.com/en/articles/20001256-plugins-in-chatgpt
