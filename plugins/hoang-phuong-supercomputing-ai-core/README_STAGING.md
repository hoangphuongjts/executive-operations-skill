# Kiểm thử Core v16.0.41 — Staging

Bản cập nhật giữ nguyên Core 16.0.40, chỉ bổ sung/điều chỉnh cầu nối và danh mục định tuyến.

- PASS: 216/216 kiểm thử tự động offline.
- Phân loại đề xuất thay đổi: 27 / 181. Các mapping còn lại vẫn cần kiểm chứng ngữ nghĩa khi sử dụng.
- 128 role / 16 workflow: pass về cấu trúc; kiểm thử gateway/host E2E: NOT TESTED.
- Zero cost: không có lệnh gọi model/tool/API thực.
- Kill switch mặc định bật; không sửa OAuth, không xóa plugin nguồn.
- Nếu phát hành: sử dụng update-plugin overlay với expected_release_id để tránh ghi đè chồng phiên bản, đọc lại manifest và các file mới.
