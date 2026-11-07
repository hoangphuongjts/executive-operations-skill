# Định tuyến 108 mã học tập gốc + chidao (Hoàng Phương Core)

## Thứ tự ưu tiên và nguồn chân lý
- Nguồn dữ liệu DUY NHẤT cho tên, thứ tự, chức năng, ví dụ: `../hoangphuong-supercomputing-core/references/STUDY_108_BASELINE.json` (108 phần tử).
- Không đổi, thêm, xóa, alias hoặc cập nhật bất kỳ mục nào trong registry. `skills/chidao/SKILL.md` là Skill ĐIỀU PHỐI độc lập, tuyệt đối không ghi nó vào baseline 108.
- Khi Core được gọi (`@hoangphuong-supercomputing-core` hoặc chat plugin), kích hoạt hướng dẫn chidao qua `../core-chidao-auto-router/SKILL.md`; nếu nội dung bắt đầu với mã học tập hợp lệ, giải mã mã đó từ registry TRƯỚC, rồi áp dụng chidao như quy trình điều phối phù hợp, không thay thế chức năng gốc.

## Quy tắc phân giải lệnh
1. Lấy token đầu tiên sau khi trim khoảng trắng đầu dòng. Chỉ công nhận là mã đầy đủ khi token chính xác bằng `entry.code` trong registry; token theo sau bởi khoảng trắng hoặc hết chuỗi. Không khớp bằng tiền tố dài nhất mơ hồ.
2. Nếu người dùng gõ tiền tố chưa đủ như `/g` hay `/m`, gợi ý **chỉ** những mã đang có bắt đầu bằng tiền tố, giữ đúng tên và thứ tự, rồi để người dùng chọn. Nếu không khớp, nói không thấy mã trong 108 gốc; tuyệt đối không tự sáng tạo mã.
3. Nếu là mã đầy đủ kèm yêu cầu: thi hành đúng `function` nguyên bản. Khi yêu cầu là ảnh, dùng công cụ tạo ảnh thực sự nếu có; khi là game/app, ưu tiên UI tương tác thực thi được khi môi trường hỗ trợ; không ngụy tạo engine hoặc nút giả.
4. `/chidao` được bộ điều phối Core nhận riêng và không tính vào bộ mã học tập.
5. Không đánh tráo `/flashcards` với `/flashcardapp`, `/mindmap` với `/mindmapimage`, hay mã nào khác có cùng tiền tố. Khóa nhận diện theo token đầy đủ.

## Vai trò của chidao đối với 108 mã
- Chidao điều phối *phương pháp* phân loại độ phức tạp, chọn chuyên môn thích hợp, xác định điều kiện nghiệm thu, gọi công cụ được cho phép, kiểm chứng và báo cáo.
- 108 mã quyết định *kết quả* và hành vi cụ thể; chidao không được tự ghi đè `function`, mã hay ví dụ gốc, cũng không giả định Agent chạy thật.
- Hình ảnh: báo trạng thái công cụ image thực tế; game/app: UI chạy được hoặc thành thật nêu hạn chế; văn bản: tạo bài học đúng chức năng; kiểm tra thi cử: phân biệt mô phỏng đề với đề chính thức.
- Không tự phê duyệt các hành động nhạy cảm, mở quyền OAuth, sửa production, sinh phí hoặc chạy nền. Không khẳng định mô hình Gemini/subagent thực khi không có công cụ tương ứng.

## Giao diện tra cứu và kiểm thử
- Tệp `../hoangphuong-supercomputing-core/references/STUDY_108_DASHBOARD.html` là bản HTML offline tự chứa; trong chat chỉ có thể mở nếu môi trường host hiển thị/đính kèm nó, không mặc nhận đây là web app được host trên ChatGPT.
- Kiểm tra độc lập kết quả trong `../hoangphuong-supercomputing-core/references/STUDY_108_TEST_REPORT.json`. 108/108 route checks chỉ xác nhận khả năng nhận dạng/định tuyến, KHÔNG xác nhận 108 chức năng AI chạy end-to-end.
- Nếu host không nạp lại bản phát hành sau update, yêu cầu mở cuộc trò chuyện mới, xác minh hành vi thực tế rồi mới báo thành công trên @mention.
