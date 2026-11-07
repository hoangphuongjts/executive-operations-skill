# Kiểm thử trên tài khoản ChatGPT đích (phải thao tác tại đích)

- [ ] Plugin Core xuất hiện, bản phát hành, Skill và permission được đọc lại.
- [ ] Nhập `/mindmap Chủ đề: Chu trình nước` và kiểm tra có tạo mindmap theo chức năng gốc; đây là kiểm thử định tuyến ở host.
- [ ] Nhập `/g` và kiểm tra trả về danh sách mã học tập hợp lệ bắt đầu bằng `/g`, không bịa tên.
- [ ] Nhập `/m` và kiểm tra danh sách tiền tố hợp lệ.
- [ ] Gọi Skill `chidao` với nhiệm vụ phân tích kỹ thuật, kiểm tra nó chỉ điều phối theo quyền hiện tại.
- [ ] Yêu cầu Core dùng hồ sơ `agent-082` để kiểm toán định tuyến Skill; xác nhận có dùng hồ sơ/định danh, không đánh đồng với process Agent độc lập.
- [ ] Xem plugin độc lập `content-ai-vietnam` / `channel-growth-agent-vn`; thử `voice-selection` và `free-voiceover` dưới chỉ rõ plugin, phát hiện xung đột.
- [ ] Duyệt đủ các Skill tại host; đối chiếu 197 bản ghi trong `TESTS/SKILL_ACTIVATION_STATIC_MATRIX.json`.
- [ ] Ebook local: chỉ thử khi có Windows runtime được phép; không kỳ vọng ChatGPT cloud tự chạy Python của máy.
- [ ] Nango: kết nối lại bằng thông tin xác thực của đích; thử thao tác đọc, không xuất giá trị API key.
- [ ] Google AI Tools: Site/App phải được chia sẻ hoặc tái triển khai riêng; không đánh dấu import thành công chỉ vì có 2 manifest.
- [ ] Sau từng bước ghi plugin ID mới, số Skill host nhìn thấy, lỗi, phiên bản vào `TARGET_ACCOUNT_ACCEPTANCE_TEMPLATE.json`.

**Chưa có tài khoản đích kết nối trong phiên kiểm thử này. Tất cả mục trên chờ xác nhận thực tế.**
