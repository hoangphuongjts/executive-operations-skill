# HOÀNG PHƯƠNG AI EBOOK LIBRARY v1.0 — staging

**Gói staging cá nhân, không phải plugin cloud đã chạy.** Mã nguồn Python 3.11+ chỉ dùng thư viện chuẩn; không cài package pip, không dùng API AI trả phí.

## Chức năng đã viết

- MCP stdio với 10 tools cho thư viện local, Google Books search, OAuth, metadata Uploads, bookshelf và web reader.
- Web reader tiếng Việt, đọc EPUB an toàn ở chế độ **văn bản đơn giản**, đọc PDF bằng viewer của trình duyệt, nhập EPUB/PDF 50 MiB/tệp và chống trùng bằng SHA-256.
- Google Books API public search và Google Play Books metadata *chỉ sau khi OAuth thành công*.
- OAuth Desktop PKCE: scope `https://www.googleapis.com/auth/books`, token giữ trong RAM của từng process (không lưu token/refresh token).
- SQLite local lưu metadata và tiến độ; không sửa/xóa Play Sách.

## Cách chạy offline trên Windows

1. Cài Python 3.11+ từ python.org, bật `Add Python to PATH`.
2. Giải nén gói. Mở PowerShell tại thư mục `hoang-phuong-ai-ebook-library`.
3. Chạy: `python server\web_app.py`.
4. Mở http://127.0.0.1:8765/ trên **chính máy đang chạy ứng dụng**.
5. Nhấn **Thêm sách**, chọn EPUB/PDF cá nhân. Dữ liệu cục bộ mặc định ở `%USERPROFILE%\HoangPhuongEbookLibrary`.

Để chạy MCP stdio thủ công: `python -u server\mcp_server.py`; cấu hình host đọc `mcp.json` khi được host hỗ trợ. Lệnh `ebook_reader_start` mở web UI trên một cổng loopback bất kỳ.

## Liên kết Google Books/Play Sách

1. Trong Google Cloud Console, tạo dự án (theo quota và điều khoản Google); bật Books API nếu Google yêu cầu; cấu hình OAuth consent screen và tạo **OAuth client type Desktop app**.
2. Đặt biến môi trường `GOOGLE_OAUTH_CLIENT_ID` bằng Client ID **không phải secret** của ứng dụng Desktop. Không nhập mật khẩu, token, hay OAuth client secret vào ChatGPT.
3. Nếu cần tìm Google Books công khai, đặt biến môi trường `GOOGLE_BOOKS_API_KEY` (key không đưa vào mã nguồn; kiểm soát quota và restrictions).
4. Khởi chạy lại server; bấm **Kết nối Google**; trình duyệt chuyển tới Google, xác nhận quyền truy cập. Quay lại URL thư viện ban đầu, chọn **Play Sách đã tải lên**.
5. `volumes/useruploaded` và `volumes/mybooks?acquireMethod=UPLOADED` xuất hiện trong đặc tả Google Books do Google phát hành; phải kiểm thử OAuth thực tế để biết API còn trả về metadata cho tài khoản hay không. 403/404 có thể xảy ra.
6. API trả về metadata **không đảm bảo** tải được bản EPUB/PDF gốc lên ứng dụng. Dùng tệp gốc để đọc nội bộ nếu API không cung cấp toàn văn hợp pháp.

Lệnh PowerShell mẫu (chỉ áp dụng cửa sổ hiện tại):

```powershell
$env:GOOGLE_OAUTH_CLIENT_ID="YOUR_DESKTOP_OAUTH_CLIENT_ID.apps.googleusercontent.com"
$env:GOOGLE_BOOKS_API_KEY="YOUR_RESTRICTED_BOOKS_API_KEY"
python .\server\web_app.py
```

## Kiểm thử

Chạy `python -m unittest discover -s tests -v` từ thư mục plugin. Bài test dùng thư mục tạm, không dùng tài khoản Google, không tạo phí.

## Bảo mật và giới hạn đã biết

- Ứng dụng chỉ bind `127.0.0.1`; mặc định không thể truy cập qua Internet/điện thoại khác.
- OAuth không ghi access token ra đĩa. Phần mềm web reader riêng và MCP server riêng chạy ở hai process sẽ **không tự dùng chung phiên OAuth**.
- Trình đọc EPUB hiện **chỉ render văn bản**, không tái hiện chính xác ảnh/kiểu chữ của EPUB, tránh script độc hại.
- Chưa triển khai TTS, AI tóm tắt tự động, đồng bộ đám mây, Android/iOS native, Google Play Books full-text download.
- Không chạy `mcp.json` trực tiếp trên ChatGPT Web nếu host không hỗ trợ stdio. Plugin cá nhân lưu trên tài khoản có thể sử dụng Skill, nhưng MCP server chỉ hoạt động khi host local hỗ trợ.
- Bản này chưa thử OAuth với tài khoản thật của bạn. Không khẳng định đồng bộ sách Uploads thực tế đã thành công.
- Tệp nhập **được sao chép** vào thư mục riêng của app. Không chạm file gốc hay tài khoản Google.

## Nguồn chính thức

- https://developers.google.com/books/docs/v1/reference/
- https://developers.google.com/books/docs/v1/using
- https://code.googlesource.com/google-api-go-client/+/refs/heads/master/books/v1/books-api.json
- https://developers.google.com/books/docs/viewer/developers_guide
