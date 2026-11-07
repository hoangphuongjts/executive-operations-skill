---
name: architecture-documentation-arc42-vn
description: "Lập hồ sơ kiến trúc phần mềm có cấu trúc cho hệ thống mới hoặc hiện hữu; tổ chức bằng chứng, quyết định, luồng chạy, triển khai, chất lượng và rủi ro theo arc42."
license: Apache-2.0
---

# Lập hồ sơ kiến trúc phần mềm theo arc42

Dùng kỹ năng này khi Hoàng Phương cần một tài liệu kiến trúc có thể bàn giao, cập nhật và đối chiếu với bằng chứng. Kỹ năng tổ chức tài liệu; bản nháp không xác nhận hệ thống đã được triển khai hoặc kiểm thử.

## Quy trình

1. **Chọn phạm vi và người đọc.** Xác nhận hệ thống, phiên bản, môi trường, đối tượng đọc và mục đích tài liệu. Nếu đang thiết kế phương án mới, dùng thêm system-design-planning-vn; nếu cần mô tả codebase hiện hữu, thu thập bằng chứng theo github500-architecture-blueprint trước.
2. **Lập sổ bằng chứng.** Tách dữ kiện đã đọc hoặc được người dùng cung cấp, suy luận, giả định và đề xuất. Ghi đường dẫn/tên nguồn hoặc trích dẫn cho các chi tiết kiến trúc quan trọng. Không xem tên file hay thư mục là bằng chứng về chức năng.
3. **Tạo bản đồ tài liệu.** Tổ chức nội dung theo 12 phần:
   1. Mục tiêu và yêu cầu
   2. Ràng buộc kiến trúc
   3. Phạm vi hệ thống và bối cảnh
   4. Chiến lược giải pháp
   5. Các khối xây dựng
   6. Luồng chạy chính
   7. Mô hình triển khai
   8. Khái niệm xuyên suốt
   9. Quyết định kiến trúc
   10. Yêu cầu chất lượng
   11. Rủi ro và nợ kỹ thuật
   12. Thuật ngữ
4. **Mô tả các ranh giới.** Với từng thành phần, ghi trách nhiệm, dữ liệu sở hữu, giao diện, giao thức, phụ thuộc, người gọi và ranh giới lỗi. Phân biệt sơ đồ bối cảnh, khối thành phần, luồng thời gian và triển khai; dùng Mermaid khi sơ đồ giúp người đọc kiểm tra được luồng.
5. **Ghi quyết định có lý do.** Mỗi ADR nêu bối cảnh, ràng buộc, các lựa chọn thực tế, quyết định, lý do, hệ quả thuận lợi/bất lợi và điều kiện xem xét lại. Gắn nhãn dự thảo cho đến khi người có thẩm quyền chấp thuận; không suy diễn quyết định đã được thông qua.
6. **Viết yêu cầu chất lượng có thể đánh giá.** Nêu tác nhân, điều kiện kích hoạt, môi trường, kết quả mong đợi, phép đo và ngưỡng do Hoàng Phương cung cấp hoặc xác nhận. Đánh dấu ngưỡng minh họa là giả định; không gọi chúng là benchmark.
7. **Ghi rõ điều chưa biết.** Dùng trạng thái “chưa có bằng chứng”, “giả định” hoặc “đề xuất” thay vì tự điền. Nếu một phần không áp dụng, ghi lý do ngắn gọn; không bỏ phần để che khoảng trống.
8. **Rà soát tính nhất quán.** Đối chiếu quyết định với sơ đồ, luồng chạy với giao diện, yêu cầu chất lượng với kế hoạch kiểm chứng, và rủi ro với biện pháp xử lý. Đánh dấu nội dung cũ, mâu thuẫn và câu hỏi cần người phụ trách quyết định.
9. **Bàn giao.** Xuất bản Markdown theo 12 phần, kèm sổ nguồn, sơ đồ cần thiết, danh sách giả định, quyết định còn mở và việc cần xác minh tiếp theo.

## Định dạng đầu ra

- Tóm tắt mục đích, phạm vi, phiên bản và trạng thái tài liệu.
- 12 phần kiến trúc, chỉ nêu chi tiết có ích cho người đọc.
- Sơ đồ và bảng cho ranh giới, luồng, quyết định, yêu cầu chất lượng và rủi ro.
- Bằng chứng/nguồn bên cạnh các khẳng định trọng yếu.
- Danh sách giả định, khoảng trống, mâu thuẫn và người cần xác nhận.

## Giới hạn

- Không khẳng định một thiết kế là hiện trạng nếu chưa có bằng chứng.
- Không tự chọn nhà cung cấp hoặc công nghệ thay cho người dùng.
- Không tuyên bố kiểm thử, triển khai, bảo mật hoặc tuân thủ đã được xác minh nếu chưa có kết quả tương ứng.
- Không chạy script hay cài dependencies chỉ để tạo tài liệu.
- Với yêu cầu pháp lý, tiêu chuẩn hoặc thông số sản phẩm có thể thay đổi, xác minh nguồn chính thức và phiên bản trước khi ghi vào tài liệu.

