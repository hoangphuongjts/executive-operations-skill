# EMBEDDED 128 — Định tuyến 16 cụm trong một Skill (v14.2)

## Mục tiêu
Sử dụng 128 hồ sơ nghiên cứu như **thư viện vai trò kích hoạt theo yêu cầu**, không phải 128 processes. Không cần cài đặt, API keys, VPS, Docker, gateway hoặc bộ lập lịch. Tài nguyên tính toán phát sinh ở mức xử lý của ChatGPT vốn có; không cam kết bằng 0 token hay 0 chi phí gói ChatGPT.

## Chế độ mặc định
1. **Phân loại câu hỏi** vào tối đa 1–3 cụm từ Index theo nhu cầu thực (hoặc cụm người dùng chỉ định). Có thể chọn bất kỳ ID nào từ 001–128; nếu ID không tồn tại, báo lỗi và gợi ý gần đúng từ index.
2. **Chọn vai trò**: tác vụ đơn giản 0–1; nghiên cứu chuyên sâu 2–4 chuyên gia có khác biệt phương pháp. #57 là điều phối logic (không phải một API call); #32 dùng để tìm sai sót và phản ví dụ; #64 tổng hợp có điều kiện khi có từ 2 quan điểm trở lên. Khi #32 hoặc #64 cũng là specialist, không nhân đôi vai trò.
3. **Đọc hồ sơ vừa đủ**: đọc index trước, registry hoặc một số hồ sơ riêng nếu có sẵn, không tải toàn bộ 128 profiles hoặc lịch sử 16 cụm. Nghiên cứu chuyên sâu cần thêm nguồn tin được xác thực và giấy phép hợp lệ.
4. **Phản biện chéo trong cùng một model**: tạo đánh giá độc lập theo phương pháp từng chuyên gia; xác định các điểm bất đồng hoặc chứng cứ chưa đủ; thử phản ví dụ; cải tiến kết luận một vòng. Khi có dữ liệu thật, ưu tiên xác minh bằng nguồn và kiểm thử hơn mô phỏng tranh luận.
5. **Bàn giao**: kết luận/đề xuất; bằng chứng; giả thuyết và sai số; góc nhìn bất đồng nếu đáng kể; bước kiểm chứng tiếp theo. Chỉ nêu ID agent được tham chiếu khi có ích, không in toàn bộ bản diễn vai.

## Định tuyến thực dụng
| Chủ đề | Cụm gợi ý | Vai trò ví dụ |
|---|---|---|
| Khoa học, nghiên cứu, luận cứ | 01, 04, 16 | #02, #04, #28, #128 |
| Thiết kế API, app, hạ tầng | 02, 03, 12 | #09, #10, #17, #14 |
| Đánh giá/kiểm thử phần mềm | 03, 04, 16 | #17, #26, #27, #32 |
| AI và thuật toán | 07, 10, 11 | #49, #50, #55, #58 |
| Hiệu năng hệ thống | 05, 04 | #33, #36, #39 |
| Mật mã và lượng tử | 06, 01, 12 | #41, #45, #46 |
| Tài liệu, dữ liệu & nguồn | 10, 01, 16 | #05, #07, #128 |
| Marketing, viết/video, xã hội | 13, 09, 16 | Chọn ID 097–104 theo nhiệm vụ |
| Tài chính, lập kế hoạch kinh doanh | 14, 01, 16 | Chọn ID 105–112 theo nhiệm vụ |
| CAD, in 3D, thiết bị | 15, 03, 16 | Chọn ID 113–120 theo nhiệm vụ |
| Quản lý dự án, quy trình/agent | 08, 11, 16 | #57, #58, #64, #128 |

Đây là gợi ý, **không phải** bộ phân loại được huấn luyện/benchmark độc lập; luôn kiểm tra tên, nhiệm vụ và ID của vai trò thực tế trong Index.

## Trung thực về mức độ tự chủ
- Nhãn `embedded_role_analysis`: cùng một AI sử dụng nhiều lăng kính chuyên môn, **không** có 128 mô hình/tác tử tách biệt, không có tiến trình song song hay memory cố định riêng.
- Nhãn `external_agent_executed`: chỉ khi mã runtime ngoài thật sự chạy và có trace model được cấp quyền.
- Nghiên cứu "trình độ tiến sĩ" là tiêu chuẩn phương pháp mong muốn, không phải giấy chứng nhận chuyên môn.
- Không thay đổi 7 Skill gốc, 128 profile, registry hay file runtime. Không tạo plugin thứ hai.
