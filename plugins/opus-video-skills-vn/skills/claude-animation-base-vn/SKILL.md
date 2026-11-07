---
name: claude-animation-base-vn
description: "Hướng dẫn dùng repo JohnHeibel/ClaudeAnimationBase trên máy được phép cài đặt: thiết kế storyboard hoạt hình 2D vẽ tay, dựng mã p5.js + p5.brush, kiểm tra và xuất MP4; phối hợp với Hoangphuong Core và Opus Video Skills VN."
---

# ClaudeAnimationBase VN — Adapter an toàn

**Upstream**: https://github.com/JohnHeibel/ClaudeAnimationBase (John Heibel, MIT, copyright 2026). Bản này chỉ là hướng dẫn, **không** chứa engine hoặc dịch vụ dựng video và **không** tự cấp quyền thực thi shell. Đọc `ANIMATION_GUIDE.md` từ clone upstream trước khi lập trình, không đoán API khi không có nguồn.

## Điều phối
- Chạy trong vai trò hỗ trợ của Hoangphuong Core, không thay thế Core; không thay đổi 7 Skills, 128 hồ sơ vai trò, 16 cụm hay 108 lệnh học tập.
- Repo là starter kit nền tảng; `painted-animation` trong Opus Video Skills kế thừa và mở rộng ý tưởng này. Tránh sao chép và cài gói phụ thuộc trùng vào chung thư mục dự án.
- Yêu cầu bản quyền: tự tạo nhân vật/cốt truyện/âm thanh; tránh dùng lại nhân vật hoặc tài nguyên có quyền hạn chưa được xác minh để thương mại; giữ thông báo MIT khi phân phối mã.

## Workflow
1. Xác định nội dung, thời lượng, tỷ lệ 16:9 hay 9:16, nguồn giọng, quyền sử dụng, mục tiêu.
2. Xây `STORYBOARD.md`: chủ đề, nhân vật, góc máy, nhịp chuyển, mục tiêu học tập và từng shot.
3. Kiểm tra hệ thống có Node.js, npm, Git, Chrome và FFmpeg; tải đúng upstream qua `git clone` hoặc cập nhật có kiểm soát. Không tự chạy mã repo trong ChatGPT.
4. Đọc `ANIMATION_GUIDE.md`, tùy chỉnh `src/config.js`, tạo scene JS trong `src/scenes/`, đăng ký trong `studio.html` và giữ thứ tự chuyển cảnh.
5. Dùng `node render.mjs --sheet=0,1,2 --out=out/sheet.jpg` để xem mẫu; đánh giá hình, chuyển động, chữ, viền, tương phản.
6. Chạy `node render.mjs --clip --out=out/video.mp4` khi đã kiểm tra và không có xung đột; nếu thiếu GPU cân nhắc `--soft-gl` với giới hạn hiệu năng.
7. Dùng `ffprobe` xác nhận codec, độ phân giải, FPS, thời lượng, audio; không khẳng định xuất thành công nếu chưa quan sát file thực tế.

## Tính tương thích
- Repo upstream `package.json`: p5 ^2.3.3, p5.brush ^2.2.3, puppeteer-core ^25.11.0; khóa phiên bản thực tế qua lockfile sau khi cài, kiểm tra npm audit.
- Node.js + Chrome + FFmpeg là yêu cầu upstream; Python không cần cho demo thông thường.
- Cấu hình Windows ưu tiên thư mục `D:\AI-VIDEO\ClaudeAnimationBase`, không xóa/cập nhật thư mục có sẵn khi chưa đối chiếu.
- Render có thể chậm nhiều giây mỗi frame nếu GPU tích hợp; không bảo đảm hiệu năng hay chất lượng dựa trên README.

## Trạng thái
- `[PACKAGED]` chỉ khi adapter được upload vào plugin; `[HOST_VISIBLE]` chỉ sau khi đọc lại host; `[DEPLOYED]` chỉ khi engine được chạy thử thật bên ngoài.
- Không đăng, tải lên mạng xã hội, tiêu hao credits hay thay đổi project/khóa API khi chưa được người dùng cho phép.
