# Quy tắc xuất và đồng bộ hướng dẫn Gemini — dùng mặc định từ phiên bản này

Áp dụng cho mọi yêu cầu **xuất/chuyển/đóng gói kỹ năng sang Gemini** của bộ kỹ năng này ở các phiên tiếp theo. Đây là tài liệu hướng dẫn trong plugin, không phải cơ chế tự đồng bộ nền.

## Cam kết khi đóng gói
1. Không thay thế hoặc xóa chức năng hiện có của bộ kỹ năng ChatGPT. Lấy phiên bản nguồn hiện hành của đúng plugin, kiểm kê tệp trước khi xuất.
2. Mỗi bản xuất Gemini Web phải **đính kèm sẵn** `Gem-Instructions/GEM_INSTRUCTIONS.txt` để người dùng dán vào Instructions của Gem; kèm `README-GEMINI.md` và các tài liệu Knowledge phù hợp. Nếu có yêu cầu phối hợp hai bộ, kèm `Gem-Instructions/GEM_PHOI_HOP.txt`.
3. Mỗi bản xuất Gemini CLI phải chứa `.gemini/skills/<tên-skill>/SKILL.md`, các tệp references/scripts được phép liên quan, và `GEMINI.md` định tuyến skill ở thư mục gốc. Giữ các tên skill gốc, không đổi chức năng.
4. Trong bản xuất hợp nhất, giữ bản sao nguồn riêng biệt ở `source-plugins/<plugin-name>/`; chỉ gộp các thư mục skill trùng tên khi nội dung đồng nhất. Nếu khác nhau, dừng và báo xung đột; không ghi đè im lặng.
5. Luôn đưa tài liệu này, lời hướng dẫn thiết lập Gemini Web/CLI, cảnh báo kết nối và quyền, cùng manifest kiểm tra SHA-256 vào tệp bàn giao để không cần ghép thủ công sau này.
6. Kiểm tra file ZIP, số tệp nguồn, kỹ năng, cú pháp JSON/YAML nơi có thể, liên kết nội bộ, danh sách tệp và hash; báo rõ phần chưa kiểm thử trên Gemini thật.
7. Nếu người dùng chỉ yêu cầu sửa bản ChatGPT, không tự cài/sửa trên Gemini. Nếu yêu cầu xuất, tạo bản cho Gemini nhưng **không nói đã cài hoặc kích hoạt trên tài khoản Google** khi chưa kiểm chứng.
8. Khi sau này cập nhật nội dung các skill, duy trì và chỉnh lại hướng dẫn Gemini đi kèm để phản ánh thay đổi thực tế. Không hứa Gemini tự cập nhật nếu chỉ mới cập nhật plugin ở ChatGPT.

## Giới hạn bắt buộc
- Plugin/Skill ChatGPT không phải plug-in tự cài được trên Gemini Web. Tài liệu Knowledge & Gem Instructions không cấp kết nối MCP, OAuth, quyền Analytics hay quyền đăng bài.
- Quy tắc dành cho Gemini CLI là hướng dẫn tổ chức project; tên các lệnh dạng `/channel-growth-agent ...` trong skill gốc là **trigger hội thoại**, không tự trở thành slash command Gemini CLI.
- Tôn trọng bản quyền tài nguyên và giọng nói (bao gồm giọng Adam), xác minh quyền thương mại trước khi dùng; không tự clone giọng khi chưa có phép.
- Không đăng bài, thay đổi tài khoản, chi tiền/credits, chạy script chưa được cho phép. Không tuyên bố render MP4 nếu chưa có file và QA.
- Mặc định tiếng Việt, xưng "mình" hoặc "em". Brief người dùng là ưu tiên khi không xung đột quy tắc an toàn.

## Tệp kèm sẵn
- `gemini/GEM_INSTRUCTIONS.txt`: hướng dẫn riêng cho Gem của plugin này.
- `gemini/GEM_PHOI_HOP.txt`: hướng dẫn khi phối hợp với plugin còn lại.
- `gemini/GEMINI.md`: chỉ dẫn Gemini CLI riêng cho plugin này.
- `gemini/README.md`: hướng dẫn sử dụng và giới hạn.
