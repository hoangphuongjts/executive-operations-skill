---
name: statistical-reporting-audit-vn
description: "Dùng khi cần soát, biên tập hoặc soạn phần phương pháp thống kê, kết quả, chú thích hình, cỡ mẫu, p-value, khoảng tin cậy, đơn vị thực nghiệm, phép thử, mô hình, hiệu chỉnh nhiều phép so sánh hoặc phản hồi nhận xét về thống kê trong bản thảo khoa học."
license: Apache-2.0
---

# Kiểm tra báo cáo thống kê khoa học

Dùng skill này để làm cho phần thống kê trong bản thảo minh bạch, có thể hiểu và đối chiếu với thiết kế nghiên cứu. Đây là hướng dẫn báo cáo và rà soát. Không thay thế chuyên gia thống kê hoặc việc phân tích lại dữ liệu thô, trừ khi Hoàng Phương cung cấp dữ liệu và yêu cầu rõ việc phân tích.

## Nguyên tắc

- Xác định điều gì được đo, đơn vị nào được phân tích và kết luận nào được đưa ra.
- Lấy đơn vị thực nghiệm độc lập làm cơ sở xác định cỡ mẫu n. Không tự coi tế bào, ảnh, trường nhìn, giếng kỹ thuật, lần đọc lặp, phổ, hạt dữ liệu hay nhiều lần chạy trên cùng một mẫu là các mẫu độc lập.
- Báo cáo cỡ ảnh hưởng, độ bất định, cỡ mẫu và định nghĩa phép kiểm định; không để p-value hoặc dấu sao gánh toàn bộ kết luận.
- Ghi thông tin còn thiếu thành `CẦN TÁC GIẢ XÁC NHẬN`. Không tự điền cỡ mẫu, phép kiểm định, phần mềm, hiệu chỉnh, tiêu chí loại mẫu, ngẫu nhiên hóa, làm mù hay cách xử lý dữ liệu thiếu.
- Khi chỉ dẫn của tạp chí, quy trình đã đăng ký trước hoặc chuẩn chuyên ngành khác với gợi ý chung, ưu tiên nguồn cụ thể đó và nêu rõ nguồn đã áp dụng.

## Đầu vào phù hợp

- Phần Phân tích thống kê, Phương pháp hoặc Kết quả.
- Chú thích hình, bảng, dữ liệu nguồn hoặc nhận xét của phản biện về thống kê.
- Thiết kế nghiên cứu, đề cương, kế hoạch phân tích hoặc bảng các phép so sánh.
- Dữ liệu thô hay dữ liệu tóm tắt chỉ khi người dùng yêu cầu phân tích lại hoặc kiểm tra số liệu cụ thể.

Nếu chỉ có một phần bản thảo, hãy giới hạn phạm vi rà soát và ghi rõ phần nào chưa thể đánh giá.

## Quy trình

1. **Phân loại yêu cầu.** Xác định người dùng muốn kiểm tra, viết lại, soạn mới, trả lời phản biện, đối chiếu chú thích hình hay phân tích dữ liệu.
2. **Tái dựng thiết kế từ tài liệu được cung cấp.** Ghi nhóm, điều kiện, thời điểm, kết cục, yếu tố chặn, đo lặp, ngẫu nhiên hóa, làm mù, tiêu chí loại mẫu và cách xử lý thiếu dữ liệu.
3. **Xác định n và cấu trúc lặp.** Phân biệt đơn vị độc lập, lặp sinh học, lặp kỹ thuật, đo lặp, mẫu phụ, tế bào/ảnh, mô phỏng và dữ liệu gộp.
4. **Đối chiếu hai chiều giữa kết luận và phân tích.** Với mỗi kết luận, ghi phép so sánh hoặc mô hình, giả định, chiến lược hiệu chỉnh, ước lượng hiệu quả, khoảng bất định và cách báo cáo p-value. Sau đó kiểm tra ngược: mỗi phép thử được khai báo trong Phương pháp có xuất hiện trong Kết quả và phù hợp với câu hỏi nghiên cứu không. Loại nội dung khai báo nhưng không sử dụng thay vì tự thêm kết quả.
5. **Kiểm tra nguy cơ thường gặp.** Soát giả lặp, nhiều phép so sánh, suy luận tương tác sai, phân tích bỏ qua ghép cặp/phân tầng/lồng nhau, cỡ mẫu nhỏ, ngoại lệ và kết luận chỉ dựa vào ngưỡng ý nghĩa.
6. **Kiểm tra đủ thông tin.** Nếu phù hợp, nêu biến kết cục, đơn vị n, số nhóm, tiêu chí loại mẫu, xử lý thiếu dữ liệu, phép thử/mô hình, giả định hoặc lý do dùng phương pháp bền vững/phi tham số, hiệu chỉnh, ước lượng, khoảng bất định, p-value và phần mềm/phiên bản.
7. **Đối chiếu hình và kết quả.** Với từng ô dữ liệu định lượng, kiểm tra ý nghĩa của điểm/thanh/hộp/đường, định nghĩa n, loại thanh sai số, phép thử, cặp hay không cặp, hiệu chỉnh nhiều so sánh và dữ liệu nguồn. Với chuỗi thời gian, kiểm tra có theo dõi cùng đơn vị hay không. Với tương quan/hồi quy, phân biệt mô tả với suy luận và kiểm tra tính độc lập của các điểm.
8. **Kiểm tra nguồn hiện hành.** Ưu tiên tài liệu người dùng cung cấp và hướng dẫn chính thức mới nhất của tạp chí đích. Dùng hướng dẫn theo loại nghiên cứu như CONSORT, STROBE, PRISMA hoặc ARRIVE khi nghiên cứu thực sự thuộc phạm vi đó. Không khẳng định tạp chí bắt buộc một phép thử cụ thể nếu nguồn chính thức không nói vậy.
9. **Soạn bản sửa và kiểm tra cuối.** Viết phần có thể dán vào bản thảo, chỉ dùng thông tin đã có. Không đổi tương quan thành nhân quả, không tăng độ mạnh của kết luận và không lặp một quy tắc báo cáo ở nhiều nơi.

## Định dạng kết quả mặc định

### Phạm vi rà soát
- Tài liệu đã xem:
- Giới hạn và phần còn thiếu:
- Thiết kế nghiên cứu:
- Đơn vị độc lập và cấu trúc lặp:

### Vấn đề cần sửa
Với mỗi điểm, ghi mức độ, bằng chứng trong tài liệu, vì sao quan trọng và cách sửa:
- **P0:** Có thể làm sai kết luận trung tâm, chẳng hạn dùng sai đơn vị độc lập hoặc bỏ qua cấu trúc đo lặp.
- **P1:** Thiếu thông tin quan trọng để diễn giải hay tái lập kết quả.
- **P2:** Cách trình bày chưa nhất quán hoặc khó đọc.

### Bản sửa đề xuất
Viết đoạn Phương pháp/Kết quả/chú thích hình có thể sử dụng sau khi tác giả xác nhận dữ kiện còn thiếu.

### CẦN TÁC GIẢ XÁC NHẬN
Chỉ liệt kê câu hỏi thực tế, ngắn gọn.

### Rủi ro phản biện còn lại
Nêu điểm chuyên gia thống kê có thể tiếp tục chất vấn. Phần này dành cho tác giả, không đưa vào nội dung bản thảo.

Với yêu cầu soạn mới đã có đủ dữ kiện, có thể dùng đầu ra rút gọn: bản Phân tích thống kê, định nghĩa n, phép thử/mô hình, hiệu chỉnh, phần mềm/phiên bản và các trường chưa được xác nhận.

## Giới hạn

- Không bịa p-value, cỡ mẫu, bậc tự do, khoảng tin cậy, phiên bản phần mềm, cách hiệu chỉnh, đăng ký trước, loại mẫu hay tính toán lực thống kê.
- Không kết luận phép kiểm định cuối cùng khi chưa rõ đơn vị phân tích hoặc thiết kế. Có thể nêu phương án sơ bộ, kèm dữ kiện còn thiếu và yêu cầu chuyên gia phù hợp xem xét.
- Không chấp nhận `n = số tế bào/ảnh/lần đo` làm số lần lặp độc lập nếu chưa kiểm tra cấu trúc thí nghiệm.
- Không dùng “có ý nghĩa thống kê” đồng nghĩa với quan trọng, ảnh hưởng lớn, có quan hệ nhân quả hay có ý nghĩa sinh học/thực tiễn.
- Không che kết quả yếu hoặc không có ý nghĩa bằng cách viết lại theo hướng mạnh hơn.
- Không đưa lời khuyên thống kê lâm sàng, y tế hoặc pháp quy vượt quá việc rà soát cách báo cáo nếu không có đề cương liên quan và yêu cầu giới hạn rõ ràng.

## Thứ tự ưu tiên nguồn

1. Tài liệu, dữ liệu, đề cương, kế hoạch phân tích, nhận xét phản biện và hướng dẫn tạp chí do người dùng cung cấp.
2. Hướng dẫn tác giả và biểu mẫu báo cáo hiện hành của tạp chí đích.
3. Hướng dẫn thống kê/chuyên ngành chính thức phù hợp với lĩnh vực và loại nghiên cứu.
4. Nguyên tắc báo cáo thống kê thận trọng, có thể kiểm tra lại.

Khi chưa đủ dữ kiện để đưa ra nhận xét vững chắc, hãy hỏi thông tin còn thiếu hoặc đưa ra phương án câu chữ có giới hạn; không đoán.
