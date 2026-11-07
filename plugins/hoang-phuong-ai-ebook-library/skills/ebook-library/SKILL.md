---
name: ebook-library
description: Hỗ trợ người dùng tìm sách Google Books, xem danh mục ebook đã tải lên Google Play Sách, quản lý thư viện EPUB/PDF cục bộ, đọc sách, đánh dấu tiến độ và học tập từ tài liệu có quyền truy cập.
---

# HOÀNG PHƯƠNG AI EBOOK LIBRARY — Quy trình vận hành

## Nguyên tắc
- Trả lời bằng tiếng Việt. Chỉ báo công cụ đã chạy nếu nhận được phản hồi công cụ thật.
- Phân biệt (a) metadata Google Books, (b) sách Uploads được Google API liệt kê, (c) nội dung EPUB/PDF cục bộ, (d) sách trả phí/DRM.
- Không nhận mình đã tải được nội dung ebook từ Google Play Sách chỉ vì API trả về metadata.
- Không vượt DRM, cào web, lấy nội dung không có quyền, chuyển nội dung có bản quyền sang AI ngoài khi chưa được đồng ý.
- Không sử dụng tool sửa/xóa thư viện Google. Công cụ cung cấp bởi plugin chỉ đọc metadata Google.
- Mọi liên kết đến tài khoản Google phải qua consent OAuth do người dùng trực tiếp cấp.

## Bước 1: Xác định trạng thái
- Gọi `ebook_status`. Báo số ebook local thực tế và trạng thái tài khoản Google.
- Nếu công cụ MCP chưa sẵn có, hướng dẫn mở web reader local. Plugin đã lưu trong tài khoản không đồng nghĩa MCP stdio đã chạy trên ChatGPT Web.

## Bước 2: Google Books / Google Play Sách
- Dùng `ebook_google_search` để tìm public metadata.
- Khi muốn xem Uploads, chỉ gọi `ebook_google_uploads` nếu đã có OAuth. Nếu chưa, yêu cầu người dùng chọn `ebook_google_auth_start` và cấp quyền.
- API ưu tiên `/books/v1/volumes/useruploaded`. Nếu trả 404, thử `/books/v1/volumes/mybooks?acquireMethod=UPLOADED`.
- Không khẳng định hai endpoint đều còn được hỗ trợ trong mọi tài khoản/2026 nếu chưa kiểm thử thực tế. Kết quả có thể rỗng hoặc trả 403.
- Có thể dùng `ebook_google_shelves` cho các kệ sách Google.
- Nếu không có truy cập nội dung tệp từ Google Play Sách, đề xuất nhập EPUB/PDF gốc vào thư viện nội bộ.

## Bước 3: Đọc cá nhân
- `ebook_reader_start` sẽ trả URL đọc trên `127.0.0.1` của máy chạy MCP, không phải URL công khai.
- `ebook_import_local` chỉ đọc tệp trong thư mục nhập đã cấu hình; hướng dẫn người dùng đặt EPUB/PDF của mình vào đó.
- Không chấp nhận đường dẫn ngoài thư mục cho phép.
- `ebook_local_list` cho metadata; `ebook_save_progress` cập nhật tiến độ theo xác nhận người dùng.
- Đọc EPUB trong giao diện trình duyệt đã loại mã động và iframe nguy hiểm; PDF bằng trình đọc trình duyệt.

## Bước 4: Học tập bằng AI
- Chỉ tóm tắt phần văn bản người dùng cung cấp hoặc trích được từ tệp có quyền truy cập hợp lệ.
- Không tự nhận đã đọc toàn bộ ebook nếu mới có tiêu đề, ảnh bìa hay metadata.
- Luôn nêu rõ độ bao phủ và nguồn trích khi trả lời về nội dung sách.

## Khả năng và giới hạn
- MCP stdio chạy cục bộ, chưa phải cloud-hosted app. ChatGPT Web/mobile có thể chưa thực thi được tool này.
- Google OAuth cần `GOOGLE_OAUTH_CLIENT_ID` của dự án trên Google Cloud. Token giữ RAM đến lúc hết hạn, không tự lưu.
- Google Books API public có thể yêu cầu `GOOGLE_BOOKS_API_KEY`.
- Không phát sinh phí cố ý; quota và cấu hình Google Cloud do người dùng tự quản trị.
