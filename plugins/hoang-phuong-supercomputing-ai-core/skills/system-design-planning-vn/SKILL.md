---
name: system-design-planning-vn
description: "Lập phương án thiết kế hệ thống mới hoặc thiết kế lại từ yêu cầu, tải dự kiến, thuộc tính chất lượng và rủi ro; dùng trước khi chọn công nghệ hoặc triển khai. Với phân tích codebase hiện có, định tuyến sang github500-architecture-blueprint."
license: Apache-2.0
---

# Lập kế hoạch thiết kế hệ thống

Dùng kỹ năng này cho hệ thống mới hoặc thay đổi kiến trúc ở mức giải pháp. Mục tiêu là làm rõ yêu cầu, tải, trade-off và rủi ro trước khi chọn stack; đây không phải khẳng định rằng thiết kế đã được triển khai hay kiểm chứng.

## Quy trình

1. **Đóng khung vấn đề.** Ghi người dùng/đối tượng, hành trình chính, phạm vi, giai đoạn sản phẩm, ranh giới hệ thống, điều đã biết và điều chưa biết. Tách yêu cầu chức năng khỏi yêu cầu vận hành.
2. **Mô tả tải và dữ liệu.** Ước lượng số người dùng và yêu cầu theo thời gian, khu vực, giờ cao điểm, tỷ lệ đọc/ghi, kích thước yêu cầu, tần suất cập nhật, loại dữ liệu và thời gian lưu. Dùng khoảng giá trị khi chưa có số đo.
3. **Tính nháp công suất.** Ghi đơn vị và giả định cho mọi phép tính. Có thể dùng:
   - yêu cầu/giây ≈ yêu cầu/ngày ÷ 86.400 × hệ số cao điểm;
   - băng thông nháp ≈ yêu cầu/giây × kích thước trung bình yêu cầu;
   - dung lượng nháp ≈ bản ghi/ngày × byte/bản ghi × số ngày lưu × hệ số bản sao/chi phí phụ trợ.
   Nêu riêng dữ liệu sao lưu, chỉ mục, nén, bản sao và tăng trưởng nếu chúng ảnh hưởng quyết định. Không trình bày ước lượng thô như số đo thực tế.
4. **Xếp ưu tiên thuộc tính chất lượng.** Ghi mục tiêu và ràng buộc cho hiệu năng, khả năng mở rộng, độ tin cậy, tính sẵn sàng, nhất quán dữ liệu, bảo mật, quyền riêng tư, khả năng quan sát, khả năng bảo trì và chi phí. Nêu trade-off quan trọng theo bối cảnh thay vì tối ưu mọi thứ cùng lúc.
5. **Chia hệ thống thành phần/lớp.** Chỉ đưa vào các thành phần cần thiết, chẳng hạn client, API/edge, dịch vụ nghiệp vụ, lưu trữ, cache, hàng đợi hoặc pipeline xử lý, quan sát và vận hành. Ghi trách nhiệm, luồng dữ liệu, điểm tin cậy và ranh giới lỗi; không chọn sản phẩm chỉ vì tên phổ biến.
6. **So sánh phương án.** Nêu 2–3 kiến trúc khả thi khi còn lựa chọn đáng kể. So sánh mức đáp ứng yêu cầu, độ phức tạp, chi phí, rủi ro vận hành, khả năng thay đổi và điều kiện khiến lựa chọn không còn phù hợp. Ghi quyết định cùng lý do và hệ quả.
7. **Rà soát lỗi và an toàn.** Tìm điểm lỗi đơn, giới hạn tải, lỗi mạng/dịch vụ/dữ liệu, hành vi suy giảm, phục hồi, xác thực/ủy quyền, dữ liệu nhạy cảm, logging và giám sát. Nối mỗi kiểm soát với yêu cầu hoặc rủi ro cụ thể.
8. **Lập kế hoạch kiểm chứng.** Xác định phép thử, số liệu quan sát, mô hình tải, kịch bản lỗi, nguồn tiêu chí và điều kiện chấp nhận. Đây là kế hoạch cần thực hiện; không gọi thiết kế là “đã kiểm thử” nếu chưa có bằng chứng.
9. **Bàn giao.** Cung cấp sơ đồ ngữ cảnh hoặc sơ đồ thành phần, bảng tải/giả định, phương án được chọn, trade-off, rủi ro, câu hỏi mở và các bước tiếp theo. Nếu cần phân tích codebase hiện có, dùng github500-architecture-blueprint.

## Quy tắc độ tin cậy

- Không bịa số người dùng, lưu lượng, SLO, ngân sách, tiêu chuẩn, dữ liệu hoặc giới hạn pháp lý.
- Phân biệt số đo, giả định, mục tiêu đề xuất và dữ kiện cần xác minh.
- Không rút mọi quyết định hệ thống phân tán thành một khẩu hiệu hoặc quy tắc hai lựa chọn; nêu giả định về lỗi, mạng, dữ liệu và cách hệ thống được phép suy giảm.
- Với sản phẩm, phiên bản, benchmark, giá hoặc tiêu chuẩn hiện hành, kiểm tra tài liệu chính thức trước khi đưa ra quyết định phụ thuộc vào thông tin đó.
- Không tự cài package, chạy repo, dựng hạ tầng, gọi API trả phí hay gửi dữ liệu ra dịch vụ ngoài phạm vi yêu cầu.

## Nguồn và giấy phép

Bản hướng dẫn tiếng Việt được chuyển thể từ checklist thiết kế hệ thống của [evelyne24/system-design-checklist](https://github.com/evelyne24/system-design-checklist), commit be1624e32e65de3fc2a65f830018e14ffb6b0331. Bản này được điều chỉnh thành quy trình lập phương án trước triển khai, làm rõ giả định/kiểm chứng và lược bỏ nội dung site Jekyll; không sao chép mã hay cài dependency. Giấy phép Apache 2.0 được giữ tại [UPSTREAM_LICENSE_APACHE-2.0.txt](references/UPSTREAM_LICENSE_APACHE-2.0.txt). Mô tả nguồn trong repo có một cách diễn đạt đơn giản hóa về trade-off nhất quán/phân vùng; bản chuyển thể không lặp lại cách rút gọn đó.
