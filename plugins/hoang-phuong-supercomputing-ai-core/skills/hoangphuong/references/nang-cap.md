# Nâng cấp skill có đối chiếu và phục hồi

Đọc khi được giao tạo, audit hoặc cập nhật skill/plugin. Dùng skill-creator và quy trình quản lý plugin tương ứng nếu khả dụng.

1. Đọc phiên bản sở hữu thay đổi, kiểm kê định danh, hành vi, tham chiếu và cấu hình. Ghi yêu cầu → khoảng trống → thay đổi → phép thử. Bảo toàn phần cũ hữu ích, prompts, giấy phép và quyền. Không sửa cache plugin để giả là đã phát hành.
2. Chọn phạm vi cụ thể; giữ entrypoint gọn và tài liệu chuyên biệt theo nhu cầu. Chỉ thêm helper cho công việc lặp lại cần tính xác định, không thêm danh mục kỹ năng để tạo cảm giác mạnh hơn.
3. Đặt tiêu chí và sao lưu riêng theo lượt; dựng bản ứng viên. Audit năm mặt: kích hoạt đúng, tải ngữ cảnh, logic/ngoại lệ, an toàn và định dạng. Đánh giá prompt dương tính, gần đúng nhưng ngoài phạm vi, thiếu dữ liệu và ca lỗi thật; không gọi kiểm tra YAML là kiểm thử hành vi.
4. Chạy kiểm tra tương ứng; với nâng cấp lớn, nhờ tác tử độc lập xử lý tình huống thực tế khi được phép. Nếu có baseline, so trước/sau cùng điều kiện; chưa có thì ghi mốc đầu. Hai lần sửa cùng lỗi chưa đạt thì lưu chướng ngại, không tiếp tục vòng vô hạn.
5. Lưu qua nơi sở hữu (tệp local hoặc API plugin), bảo vệ khỏi thay đổi đồng thời bằng version/hash/release guard. Đọc lại sau lưu. Nếu thất bại, giữ bằng chứng và khôi phục riêng phần của mình khi cần; không phá thay đổi của người khác.

Báo đúng phiên bản gói đã lưu, khác với tên kiến trúc trong tài liệu. Bản v13.0 kể trong chat không tự trở thành phiên bản plugin. Báo 'đã lưu lên tài khoản' riêng với 'ứng dụng đã nạp bản mới'. Không bịa nút duyệt, lỗi quyền hoặc thao tác bẻ khóa khi công cụ không cho thấy.

## Rà soát định kỳ
Lịch bốn giờ do ứng dụng quản lý, skill không tự lập lịch. Lượt cải tiến được kích hoạt đọc trạng thái dở/nhật ký, chọn một lỗi có chứng cứ, cập nhật chính thức, khoảng trống hoặc tình huống mới; khoảng 20 phút chủ động, tối đa hai lần sửa cùng lỗi. Nếu có core cục bộ và quy trình đã ủy quyền, đọc quy trình đó; không tự lan cập nhật ra tài khoản hoặc skill khác. Lưu tiêu chí, sản phẩm, kết quả và việc tiếp theo. Chỉ thông báo kết quả mới đáng kể, lỗi hoặc quyết định cần người dùng; không đổi model, quyền, lịch hoặc tự huấn luyện.
