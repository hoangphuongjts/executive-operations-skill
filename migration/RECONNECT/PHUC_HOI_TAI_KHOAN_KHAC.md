# Quy trình nhập và rollback — KHÔNG nhập tự động

1. **Đối chiếu** SHA-256 và đọc `REPORTS/QA_RUN_REPORT.json`.
2. **Cài Core trước** qua Plugin Creator ở tài khoản đích khi có tính năng import. Nếu tính năng thiếu, dừng phần cài, giữ ZIP và quyền sở hữu nguyên bản.
3. **Đọc lại** plugin được cài bằng số Skill, ID mới và một lệnh thử đơn giản chỉ đọc; đừng coi người dùng đã được cấp quyền chỉ vì plugin hiển thị.
4. **Cài lần lượt** các plugin hướng dẫn không có backend riêng. Nango cần API key của tài khoản đích. Ebook local cần runtime Windows riêng. Site-bound App phải được chia sẻ hoặc tái triển khai bởi chủ sở hữu.
5. **Trùng Skill:** hai tên `voice-selection` và `free-voiceover` giữa 2 plugin; nếu host không phân biệt đúng, tạm thời không bật một trong hai trong tài khoản đích, không tự đổi ID gốc.
6. **Kiểm tra kết nối:** chỉ dùng hành động đọc, không cấp quyền ghi/đăng/xóa hoặc gọi dịch vụ trả phí trước phê duyệt.
7. **Rollback:** ở tài khoản đích, có thể ngắt kết nối hoặc gỡ plugin **mới đã cài thử** bằng thao tác có xác nhận; KHÔNG tác động plugin gốc. Dùng `ORIGINAL_BACKUP` để khôi phục nguồn bản cũ khi cần, không dùng bản vá staging ghi đè production.
8. **Bàn giao:** điền `RECONNECT/TARGET_ACCOUNT_ACCEPTANCE_TEMPLATE.json`; chỉ xác nhận thành công cho plugin nào đã thực sự đọc lại trên host.
