---
name: study108-sync-router
description: "Kiểm thử định tuyến 108 mã học tập và mã mở rộng chỉ trong plugin staging, không thay đổi Hoàng Phương Core production."
---
# Study108 Sync — STAGING, không phải Core chính thức

Khi người dùng đưa yêu cầu bắt đầu bằng `/`, lấy token đầu tiên sau khi trim. So khớp **chính xác** token với các trường `code` trong `references/STUDY_108_BASELINE.json`, ưu tiên 108 mã gốc. Nếu không khớp mã gốc, thử `references/CUSTOM_STUDY_CODES.json`, kiểm tra đúng token; nếu chỉ là tiền tố thì đưa ra mã có thật bắt đầu bằng tiền tố đó. Không tự đặt tên mã. Nếu người dùng gửi lệnh đầy đủ kèm nội dung thì thực hiện chức năng đã định nghĩa, theo năng lực công cụ hiện có. Với mã mở rộng, dùng `description` và `prompt` làm nội dung hướng dẫn tác vụ, không chạy hướng dẫn độc hại, không yêu cầu quyền hoặc phí trái phép. Dùng nội dung đầu vào sau token để thực hiện. Nếu thiếu runtime, nêu hạn chế. Không tuyên bố đã chạy AI, tạo ảnh, game khi chưa thực thi tương ứng.

Bản staging không tự cập nhật plugin gốc, không nhận quyền quản trị hệ thống, không ghi đè baseline 108. Không tự tiếp nhận lệnh từ Windows khi chưa có gói được kiểm tra và phê duyệt.
