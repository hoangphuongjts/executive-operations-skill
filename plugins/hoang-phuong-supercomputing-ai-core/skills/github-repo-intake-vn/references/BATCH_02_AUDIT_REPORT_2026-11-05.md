# Báo cáo kiểm tra batch 02 — 2026-11-05

## Phạm vi
Đã xử lý tiếp theo thứ tự registry các mục Cụm 1, hạng 5–6. Nguồn dữ liệu là GitHub API và tệp tại commit ghim; không thực thi mã nguồn thượng nguồn.

## Kết quả từng repo

| Hạng | Repo và commit | Giấy phép | Skill / trùng lặp | Script và phụ thuộc | Quyết định |
|---|---|---|---|---|---|
| 5 | [InternScience/Awesome-Scientific-Skills](https://github.com/InternScience/Awesome-Scientific-Skills/commit/e67760e2081508773a59398f72bf808f3ac3217c), main, 2026-08-13 | MIT cho nội dung của catalog; submodule liên kết có giấy phép riêng | Thư mục `skills/` gồm 29 gitlink tới repo ngoài, không có một skill riêng của catalog để ánh xạ. Các nội dung được trỏ tới cần rà soát license và trùng lặp riêng; catalog có các nguồn đã nằm trong danh sách ứng viên | Không có manifest dependency ở root. Không tải hay chạy submodule/script | Loại khỏi chỉ tiêu skill: đây là catalog tổng hợp, không phải gói skill đơn nhất |
| 6 | [Boom5426/Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills/commit/00ecc183dddc5aba23462c1d547d250836122962), main, 2026-11-03 | Repo gốc MIT; skill `stats-reporting-audit` khai báo Apache-2.0 và NOTICE xác nhận nguồn Apache | So với các skill cụm 1 đang có, đây là kiểm toán cách báo cáo thống kê ở bản thảo; khác với thiết kế thí nghiệm, thẩm định nguồn trích dẫn, đánh giá bằng chứng tổng quát và viết đề xuất grant. Đã chọn một skill, biên soạn thành `statistical-reporting-audit-vn` | Thư mục skill được chọn chỉ có SKILL.md và 5 tài liệu tham khảo; không có script hoặc dependency manifest. Repo còn có installer Bash tải nguồn/ghi tệp đích, trình quản lý cài đặt thay thế và sao lưu skill, cùng script tải nội dung bài báo/ghi kết quả; chỉ triage tĩnh, không chạy/nhập. Không đưa mã, installer hay dependencies vào plugin | Tích hợp một skill văn bản tiếng Việt; giấy phép Apache 2.0 và NOTICE được giữ kèm. Kiểm toán toàn bộ mã của repo vẫn chưa hoàn tất |

## Những gì đã thay đổi trong plugin
- Thêm `skills/statistical-reporting-audit-vn/SKILL.md` và tài liệu nguồn/giấy phép.
- Cập nhật registry 16 cụm và trạng thái Cụm 1: 7/24 skill hiện có.
- Cập nhật registry 384 ứng viên: 2 repo đã đóng góp skill, 2 repo bị loại, 380 repo còn chờ; toàn bộ mã thượng nguồn đã chạy/nhập: 0.
- Giữ nguyên 16 cụm, 128 hồ sơ agent, 108 mã học tập và tất cả tệp không nằm trong gói phủ thêm.

## Điều kiện xác minh
Sau khi phát hành, đọc lại các tệp vừa thêm/sửa từ plugin. Chỉ báo là `host_verified` nếu readback xác nhận đúng nội dung và phiên bản.
