# Báo cáo kiểm chứng — HOÀNG PHƯƠNG AI EBOOK LIBRARY v1.0.0

Ngày: 2026-11-07 (Asia/Bangkok)

## Phạm vi hoàn thành trong bản sao staging

| Hạng mục | Bằng chứng | Trạng thái |
| --- | --- | --- |
| Source Python MCP | `server/mcp_server.py`, 10 tool definitions | Đã triển khai; xác nhận handshake JSON-RPC qua stdio |
| Web Reader tiếng Việt | `web/index.html`, `server/web_app.py` | Đã triển khai; HTTP smoke test đạt, **chưa browser E2E** |
| EPUB | `server/library.py` | Parser EPUB spine, loại script/style, chapter text; fixture test đạt |
| PDF | PDF header check, same-origin iframe | Mã nguồn đã tạo; cần kiểm chứng hiển thị trong trình duyệt thật |
| Import file | Web multipart + MCP allowlist | HTTP manual smoke test thành công, 50 MiB giới hạn |
| Lưu tiến độ | SQLite local | HTTP POST thử thực tế đạt |
| Google public search | API method + tests validation | Chưa gọi API thật vì chưa có API key |
| Google Uploads | `volumes/useruploaded` và fallback `volumes/mybooks?acquireMethod=UPLOADED` | Phương thức có trong Google Discovery JSON, có adapter và mock test; chưa OAuth tài khoản thật |
| Google OAuth | Desktop OAuth 2.0 PKCE | Mã nguồn đã tạo; chưa được người dùng cấp OAuth client ID và chưa xác minh callback Google thật |
| Bảo mật local | 127.0.0.1, Host/Origin restrictions, SHA-256, giới hạn kích thước, text-only EPUB | Test chặn Host và Origin đạt; cần kiểm toán độc lập trước production |

## Kết quả thử nghiệm

- `python -m unittest discover -s tests -v`: **13/13 PASS**.
- Manual HTTP: POST `/api/import` EPUB thành công; GET chapters thành công; POST progress thành công.
- MCP stdin: `initialize`, `tools/list`, `ebook_status` đều trả JSON hợp lệ; 10 công cụ được liệt kê.
- Browser E2E: **BLOCKED** bởi `ERR_BLOCKED_BY_ADMINISTRATOR` khi Playwright Chromium truy cập cả `localhost` lẫn file URL. Không được coi là PASS.
- Không gọi các API có phí, không cần kết nối Google, không thay đổi production. Không thử nghiệm trên thư viện Play Sách thật.

## Hạng mục chưa kiểm chứng / chưa làm

- OAuth thật, Google Uploads metadata thực tế, kết nối tài khoản và download nội dung ebook từ Play Sách.
- MCP stdio khả dụng trên ChatGPT Web/mobile: chưa, phụ thuộc host hỗ trợ local plugin. Account plugin lưu thành công không tự khởi chạy local stdio.
- Embedded MCP App native trong ChatGPT: chưa có; bản này cung cấp web reader localhost.
- TTS, AI tóm tắt tự động từ ebook, EPUB layout đầy đủ, tìm kiếm toàn văn, sync/cloud, quyền truy cập từ điện thoại khác.
- Browser PDF rendering E2E và accessibility audit độc lập.

## Chặn phát hành production

Chỉ cân nhắc sau khi có OAuth credentials do người dùng tự cấu hình, xác minh endpoint Uploads với account thật, kiểm thử browser trên Windows, kiểm toán độc lập bảo mật, xác nhận host MCP phù hợp và người dùng duyệt phát hành.
