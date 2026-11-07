---
name: revidapi-reup-video-vn
description: "Adapter an toàn cho RevidAPI Reup Video: phân tích nội dung được cấp quyền và dựng MP4 offline qua FFmpeg; tích hợp HoangPhuong Core Cụm 05, không tự phát sinh credit."
---
# RevidAPI Reup Video VN — staging

## Định tuyến
- Core: HoangPhuong Supercomputing Core
- Cụm chính: 05 — Content & Media
- Cụm liên quan: 06 — Social Growth (tham chiếu, không đếm skill lần hai)
- Upstream: https://github.com/Revidapi-com/revidapi-reup-video
- Upstream commit tham chiếu: 9e2cc61e58fdad71194ce0f1e1b5452b777c4853
- Chế độ: Skill hướng dẫn trong host, engine upstream chưa được cài và chưa được xác minh; sandbox/offline only.

## Luồng hoạt động
1. Chỉ sử dụng video/ảnh/nhạc do chủ sở hữu cho phép.
2. Phân tích local file (nếu đã có upstream được kiểm toán và môi trường tương ứng).
3. Viết kịch bản gốc, kiểm duyệt người dùng.
4. Render offline bằng `adapter/render_offline.py` với tài sản tự tạo; không gọi endpoint.
5. Kiểm tra codec/hình/kích thước/fps/audio bằng ffprobe.
6. Chờ phê duyệt riêng trước khi bật mạng, plugin hay xuất bản.

## Quyền mặc định
- API RevidAPI / bất kỳ API tạo AI có phí: DENY
- Download URL / network egress: DENY
- Cài gói, git clone, hiệu ứng phụ thuộc bên ngoài: DENY
- FFmpeg xử lý file local trong sandbox: ALLOW
- Đăng video: DENY

## Bằng chứng
Xem `references/AUDIT.md`, `references/TEST_REPORT.json`, `references/INTEGRATION_PLAN.md`.
Không đồng nhất adapter đã đóng gói với upstream đã cài hoặc plugin đã kích hoạt.

## Sử dụng trong Core
- Khi người dùng yêu cầu phân tích mẫu hoặc dựng video bằng RevidAPI, cung cấp workflow, checklist và hướng dẫn thực thi offline có kiểm soát.
- Không giả định có quyền chạy FFmpeg trên máy người dùng hoặc runtime upstream đã cài.
- `adapter/offline_guard.py`, `adapter/render_offline.py`, `adapter/patch_upstream.py` thuộc gói staging độc lập, **không được kích hoạt từ Skill host**.
- Chỉ chuyển qua `runtime_installed` và `render_verified_upstream` nếu có bản checkout pinned, kết quả test offline thực và kiểm chứng egress.
- Chỉ sử dụng video tham khảo có quyền, không tự sao chép âm thanh, hình ảnh, nhân vật hoặc logo của tác giả khác.
