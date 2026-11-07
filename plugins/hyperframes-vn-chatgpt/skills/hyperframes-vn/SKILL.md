---
name: hyperframes-vn
summary: Hướng dẫn sản xuất video bằng HyperFrames thông qua ChatGPT.
description: Dùng khi người dùng yêu cầu thiết kế, lên ý tưởng, storyboard, viết HTML/video, kiểm tra hoặc xuất MP4 bằng HyperFrames của HeyGen, gồm tích hợp Video ShotCraft và các nền tảng xã hội.
---

# HyperFrames VN — ChatGPT

Nguồn chính thức: https://github.com/heygen-com/hyperframes (Apache-2.0). Đây là Skill hướng dẫn do cá nhân phát triển, không phải engine/CLI chính thức và không đại diện HeyGen.

Phân biệt rõ thiết kế và render: Chỉ nói 'đã xuất MP4' khi đã chạy HyperFrames thật, kiểm tra file và cung cấp file. Plugin ChatGPT hiện chỉ hỗ trợ lập brief, đề xuất storyboard, HTML/timeline/mã nguồn và các bước triển khai. Không có backend render/FFmpeg và không cài trên máy tính của người dùng.

## Quy trình
1. Từ brief nhận nội dung, đối tượng, nguồn ảnh, logo/giọng/nhạc, quyền sử dụng, thời lượng, fps, định dạng 9:16 hay 16:9 và CTA. Không tự tạo claim quảng cáo sai hoặc nguồn ảnh không rõ quyền.
2. Đọc tài liệu CLI HyperFrames chính thức phù hợp với phiên bản nếu cần mã thực thi; tuyệt đối không bịa cú pháp. Theo upstream, HTML root có clip với `class="clip"` và `data-start`, `data-duration`; root có `data-composition-id`, `data-width`, `data-height`, `data-duration`; animation cần seekable, không dùng random thiếu seed/interval/timers làm sai frame.
3. Lập shot list cho từng cảnh. Tài nguyên sản phẩm thật phải được phép dùng; nếu chưa có, chỉ mô tả/chèn placeholders có tên rõ ràng và không quảng cáo là ảnh thật. Âm nhạc cần bản quyền rõ ràng.
4. Nếu user muốn tích hợp Video ShotCraft (Remotion), chỉ chuyển storyboard/tư duy hiệu ứng sang HyperFrames; không nói mã Remotion TSX tương thích trực tiếp với HyperFrames HTML. Nếu cần chuyển, lập bảng chuyển đổi và thử từng khung hình.
5. Hướng dẫn chạy (trong môi trường có Node 22+, FFmpeg và quyền truy cập npm): `npx hyperframes init my-video`; `cd my-video`; `npx hyperframes check --json`; `npx hyperframes render`. Đọc `npx hyperframes --help` nếu phiên bản thay đổi.
6. Khi có runtime thực, xác thực MP4 bằng `ffprobe` (FPS, resolution, duration, audio). Không tự động đăng video nếu chưa được người dùng duyệt.

## Bảo mật
- Tách dự án mới khỏi các module đã cài, không ghi đè hoặc tự cập nhật plugin khác. Tắt telemetry trong workflow riêng tư khi phù hợp.
- Chỉ nhập các secret API qua credential manager hoặc biến môi trường, không lưu key vào dự án/ZIP.
- GitHub CLI/npm và các dependency là mã bên ngoài, phải rà soát và cần môi trường thực thi hợp lệ.
