# Điều phối tác tử theo tài nguyên thực

Đọc khi người dùng yêu cầu phối hợp nhiều chuyên môn hoặc thay đổi đủ phức tạp cần kiểm định độc lập, và hướng dẫn phiên cho phép sử dụng tác tử.

Khởi đầu với số vai trò cần thiết: điều phối, thực hiện, phản biện. Một vai trò có thể làm tuần tự; vai trò mô phỏng không được báo là tác tử độc lập. Không ấn định 64 hoặc 1024 tác tử chỉ vì đó là lũy thừa hai. Đọc giới hạn đồng thời của phiên, ngân sách và kết nối trước khi mở rộng.

Mỗi nhiệm vụ có ID, đầu vào, phụ thuộc, đầu ra, người sở hữu tệp, tiêu chí nghiệm thu, thời hạn và trạng thái. Phân biệt planned/running/succeeded/failed/blocked/cancelled. Kiểm tra chu trình và phụ thuộc thiếu trước khi chạy; nhánh phụ thuộc lỗi không được báo thành công. Hạn chế song song theo tài nguyên, dùng hàng đợi có giới hạn, timeout, hủy và retry có giới hạn phù hợp. Thu hồi tài nguyên dù thành công hay lỗi.

Giao mỗi tác tử một phạm vi tệp riêng, thông báo có người khác cùng làm; không ghi đè thay đổi của nhau. Tác tử kiểm định nhận yêu cầu thực tế và nguyên liệu tối thiểu, tránh đưa đáp án mong muốn. Giữ tác động bên ngoài ở đầu mối có quyền, không để nhiều tác tử gửi/đăng/giao dịch lặp.

## Tranh luận để quyết định
Khi Hoàng Phương yêu cầu Xây Kênh phối hợp Content AI Việt Nam: đọc hai skill đang có; cho đề xuất độc lập, một vòng phản biện các bất đồng ảnh hưởng quyết định, rồi chọn bằng nguồn lực, chất lượng nội dung, mục tiêu và khả năng đo. Tối đa ba bất đồng trọng tâm; chỉ mở vòng mới khi có bằng chứng mới. Sau quyết định phải tạo sản phẩm, không dừng ở màn tranh luận. Nếu chỉ có một tác tử, ghi rõ phân tích theo hai vai trò.

Số biến active_agents hoặc số coroutine không đo số chuyên gia AI thực sự hoạt động. Khi báo phối hợp thực tế, căn cứ vào tác tử đã khởi chạy, kết quả nhận được và kiểm tra tổng hợp. Không dùng đồng thuận làm bằng chứng duy nhất.
