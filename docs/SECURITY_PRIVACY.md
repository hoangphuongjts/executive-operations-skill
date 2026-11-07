# SECURITY / PRIVACY

- **Repository phải PRIVATE.** Các gói có thể bao gồm hướng dẫn nội bộ, cấu hình kỹ thuật, tác giả, và bản sao mã mà người dùng sở hữu.
- Không mở repository cho public/fork/Pages trước khi có kiểm toán license, secrets và quyền tác giả.
- `.gitignore` ngăn file nhạy cảm mới, **không** tự bảo vệ file đã được commit. Trước mỗi push, chạy `python scripts/VERIFY_REPO.py` và xem diff.
- Không lưu access/refresh token OAuth, Google `client_secret`, GitHub PAT, Nango API key, cookie, file `.env` thực tế, private key, dữ liệu khách hàng.
- Mọi kết nối ChatGPT/GitHub/Google/Nango phải được cấp quyền riêng ở tài khoản đích.
- Không tự động chạy source từ repository, không bật workflow có chi phí/credential trên GitHub Actions.
- Nếu phát hiện secret sau khi đẩy: thu hồi/rotate ngay; sau đó xử lý lịch sử Git theo chính sách bảo mật, không chỉ xóa ở commit mới.
- Quét regex chỉ kiểm tra mẫu; không thể chứng minh toàn bộ dữ liệu chắc chắn không có bí mật. Cần người có quyền kiểm tra trước khi chia sẻ.
