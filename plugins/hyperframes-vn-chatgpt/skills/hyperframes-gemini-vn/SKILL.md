---
name: hyperframes-gemini-vn
description: Dùng khi cần thiết lập HyperFrames cho Gemini CLI, kiểm tra bản clone riêng Gemini và hướng dẫn tạo video từ Gemini mà không thay đổi plugin của ChatGPT.
---

# HyperFrames Gemini Bridge

Bản HyperFrames chính thức **đã hỗ trợ Gemini CLI**, có file `gemini-extension.json` và các Agent Skills. Sử dụng đường cài chính thức:

`gemini extensions install https://github.com/heygen-com/hyperframes --auto-update`

`gemini extensions list`

Dùng `gemini extensions update hyperframes` khi người dùng muốn cập nhật. Không dùng đường cài chính thức trên một bản clone đã sửa nếu dễ bị ghi đè. Cách giữ hai bản độc lập: clone upstream vào một thư mục riêng, clone thứ hai từ upstream vào thư mục khác, chỉ thêm GEMINI.md và skill tiếng Việt vào bản thứ hai, sau đó `gemini extensions install <absolute-local-clone-path>`, kiểm tra trước để không thay thế extension hyperframes đã cài.

Gemini CLI chạy ngoài ChatGPT và cần Node.js 22+, Git, FFmpeg, kết nối mạng, tài khoản và môi trường phù hợp. Người dùng có thể dùng bộ cài Windows đã tạo riêng trong cuộc trò chuyện. Đừng nói đã cài/đã render trên máy người dùng khi chưa có bằng chứng kiểm tra trực tiếp.

Bản plugin này chỉ cung cấp kiến thức, không kết nối hay điều khiển Gemini CLI từ ChatGPT.
