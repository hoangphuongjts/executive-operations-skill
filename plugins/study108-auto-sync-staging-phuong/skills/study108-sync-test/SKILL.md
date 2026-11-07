---
name: study108-sync-test
description: "Bộ kiểm thử offline, phê duyệt và đối chiếu release cho mã 108 mở rộng trong plugin staging."
---
# Staging update verification

Kiểm tra baseline 108 nguyên trạng, mã mở rộng không trùng mã gốc, tính toàn vẹn SHA256, nguồn phê duyệt staging và current_release_id. Sau mỗi bản cập nhật, đọc lại CUSTOM_STUDY_CODES.json và chạy định tuyến token đầy đủ + tiền tố. Bản ghi tự xưng PASS không được tin nếu chưa có công cụ kiểm thử thực. Mọi yêu cầu khôi phục staging phải tạo bản phát hành mới có kiểm chứng, không sửa plugin production.
