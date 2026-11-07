# Cài đặt trên tài khoản ChatGPT khác

## Đối chiếu & chuẩn bị

1. Tải repository **Private**, giải nén hoặc `git clone` vào máy được phép sử dụng.
2. Chạy `python scripts/VERIFY_REPO.py` và `python migration/TESTS/QA_OFFLINE.py` (bài QA migration cần chạy từ đúng đường dẫn, dùng symlink/working-directory theo hướng dẫn trong script `scripts/CHECK_PACKAGES.py`; báo cáo gốc tại `migration/REPORTS/QA_RUN_REPORT.json` chỉ là bằng chứng cũ).
3. Chọn **một** ZIP trong thư mục `packages/` tại mỗi lần nhập plugin qua tính năng Plugin Creator, nếu tài khoản đích có tính năng này.
4. Ưu tiên Core, sau đó theo `migration/MANIFESTS/INSTALL_SEQUENCE.csv`. Các tệp trong `plugins/` là nguồn dễ so sánh diff, **không phải toàn bộ repository gộp lại thành 1 plugin**.
5. Ghi `plugin_id` và `release_id` mới cho mỗi lần nhập. Không dùng ID tài khoản nguồn để đăng nhập ở tài khoản đích.
6. Sau khi nhập, dùng danh mục Skill trên tài khoản đích để xác minh từng Skill đã hiện diện. Kiểm thử hành vi có kiểm soát; cấu trúc YAML chỉ là kiểm thử tĩnh.
7. Thiết lập OAuth/MCP lại **bằng giao diện chính thức** của từng dịch vụ. Không copy token, OAuth refresh token, private key hay mật khẩu.

## Trạng thái được kiểm chứng

- 16 package có thể đem thử nhập, không bảo đảm tất cả được host chấp nhận.
- 17 plugin cá nhân được ghi danh mục. Plugin Google AI Tools dạng Site/App phụ thuộc quyền Site/backend, không có package riêng tự import được.
- 128 hồ sơ Agent là khai báo vai trò; không chứng minh 128 process/LLM độc lập đang chạy.
- 7 tệp `.pyc` không được xuất theo bản nguồn; chúng có thể được tạo lại trong Python từ `.py` tương ứng. Việc thiếu cache không chứng minh runtime đã chạy.
- 108 mã học tập gốc giữ nguyên. Mã slash custom không phải mặc nhiên là lệnh host cấp hệ thống.
- Xem `migration/REPORTS/RESOURCE_GAPS.json` và `migration/RECONNECT/OAUTH_MCP_MATRIX.json`.
