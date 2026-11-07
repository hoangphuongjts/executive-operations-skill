# Báo cáo kiểm tra batch 03 — 2026-11-05

## Phạm vi
Đã xử lý tuần tự Cụm 1, hạng 7–8 theo registry. Commit ghim được dùng để kiểm tra; không chạy hay nhập mã upstream.

## Kết quả từng repo

| Hạng | Repo và commit | Giấy phép | Skill / trùng lặp | Script và phụ thuộc | Quyết định |
|---|---|---|---|---|---|
| 7 | [Rimagination/good-story](https://github.com/Rimagination/good-story/commit/978c44d977c6934f82923570ddfa0b7b0ef755c3), main, 2026-06-28 | MIT | Root `SKILL.md` là skill khoa học định hình mạch lập luận theo bằng chứng. Khác với thẩm định chất lượng nguồn, viết grant và báo cáo thống kê; không có kỹ năng trùng trong Cụm 1. Đã biên soạn thành `scientific-story-architecture-vn` | Không có manifest dependency. Hai script PowerShell là công cụ kiểm tra tài liệu cục bộ; rà soát tĩnh thấy đọc tệp/kiểm tra mẫu, không ghi tệp, mạng hay khởi tạo tiến trình. Không chạy/đưa vào plugin | Tích hợp một skill văn bản; giữ kèm giấy phép MIT |
| 8 | [aipoch/open-science](https://github.com/aipoch/open-science/commit/a1b8f402f7499c09dfbc055acee5c95306b9f327), main, 2026-11-05 | Apache-2.0; skill được chọn cũng khai báo Apache-2.0 | Repo là ứng dụng Electron lớn, chứa 26 tệp SKILL.md. Chọn `resources/skills/literature-review/SKILL.md`; chức năng tổng quan tài liệu khác với thẩm định nghiên cứu và tra cứu repo GitHub hiện có. Đã biên soạn thành `literature-review-vn` | Skill upstream kèm `kernel.py` gọi Crossref/OpenAlex qua mạng và đọc biến môi trường API key/email. Không sao chép, nhập hay chạy kernel. Ứng dụng dùng package-lock/npm dependencies; không đưa ứng dụng, mã, script hay dependency vào plugin | Tích hợp một skill văn bản với ranh giới riêng tư rõ ràng; giữ kèm giấy phép Apache-2.0. Kiểm toán toàn bộ mã repo còn mở |

## Những gì đã thay đổi trong plugin
- Thêm hai skill tiếng Việt vào Cụm 1: `scientific-story-architecture-vn` và `literature-review-vn`.
- Cập nhật bộ đếm Cụm 1 lên 9/24, tổng 37 skill chuyên môn trong 16 cụm.
- Registry 384 ứng viên: 4 repo đã đóng góp skill, 2 repo bị loại, 378 repo còn chờ. Mã upstream đã chạy/nhập: 0.
- Giữ nguyên 16 cụm, 128 hồ sơ agent, 108 mã học tập và tất cả tệp không có trong gói phủ thêm.

## Điều kiện xác minh
Đọc lại các tệp mới/sửa sau phát hành; chỉ tính hai repo này là host-verified nếu nội dung và phiên bản được xác nhận từ plugin.
