# Phạm vi bảo mật và giấy phép

- Các tệp trong bộ ZIP là gói nguồn đã đọc từ plugin sở hữu và một số phụ thuộc sao chép từ repo khác; chưa thực hiện kiểm toán bảo mật từng dòng hay kiểm tra toàn bộ quyền phân phối.
- Nghiêm cấm đưa khóa, OAuth code, access/refresh token, cookie và mật khẩu vào ZIP; các mẫu kết nối chỉ mang cấu trúc và tên trường.
- `SECRET_SCANNER.json` là phép lọc regex offline có thể false positive/false negative; kiểm tra thủ công trước khi chia sẻ bên ngoài.
- Giữ nguyên các tệp LICENSE, NOTICE và PROVENANCE. `anything2explainer-vn-guidance` có ghi chú engine gốc theo PolyForm Noncommercial; không coi là giấy phép cho sản xuất thương mại.
- Những `.pyc` không xuất được là cache bytecode, không phải nguồn chính; không phát minh chúng từ nội dung khác để làm giả bản gốc.
- `get_owned_plugin_archive` của hệ thống nguồn có thể hỗ trợ tải nguyên bản đầy đủ khi chủ tài khoản có quyền tải link; chỉ sau khi tải và so SHA-256 mới được gọi là sao lưu byte-for-byte.
