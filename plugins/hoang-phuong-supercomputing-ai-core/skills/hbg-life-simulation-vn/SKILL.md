---
name: hbg-life-simulation-vn
summary: Vietnamese planning and safety adapter for the MIT-licensed Mr-funny/hbg-life-simulation, with consent-gated video production.
description: Hướng dẫn dựng video kể chuyện cuộc đời theo HBG Life Simulation; quản lý IP nhân vật, storyboard, Edge TTS, HyperFrames, QA và bản quyền. Không tự khởi động local API, OAuth hay sử dụng tài khoản.
---

# HBG Life Simulation — Hoangphuong Core Adapter

Nguồn: https://github.com/Mr-funny/hbg-life-simulation (MIT, copyright Mr-funny 2026). Không tự nhận đây là upstream skill nguyên bản hoặc renderer đã cài trên máy.

## Khi nào kích hoạt
Khi người dùng muốn làm video kể chuyện đời người, truyện tranh nhân vật xuyên suốt, clip zoom/pan kết hợp lời kể và phụ đề. Giữ nguyên Hoangphuong Core và 108 mã lệnh, 128 role records, 16 clusters; Skill này là hướng dẫn tích hợp tùy chọn, không có hệ thống tự chạy.

## Chuỗi công việc
1. Nhận văn bản câu chuyện; lưu nguyên bản trong SCRIPT_SOURCE.md. Chỉ chỉnh lỗi chính tả được chấp nhận, không đổi nội dung trọng yếu.
2. Chọn hướng video theo yêu cầu: ngang 1920×1080 mặc định; chỉ dùng 1080×1920 nếu yêu cầu rõ. Chốt tình trạng quyền sử dụng nội dung, nhân vật, nhạc, ảnh.
3. Phát triển CHARACTERS.md để khóa nhân vật (gương mặt, dáng, trang phục) và sinh thử ảnh neo; phê duyệt trước khi sản xuất hàng loạt.
4. Viết PROJECT_SPEC.json, SCRIPT.md, STORYBOARD_BASE.json. Dựng TTS + thời gian thực VTT rồi tạo STORYBOARD.json; không suy đoán độ dài từ văn bản sau khi có giọng thật.
5. Dùng công cụ tạo ảnh được cấp quyền để tạo ảnh truyện tranh gốc. Kiểm tra giải phẫu tay, điện thoại, công cụ; không sao chép IP/nhãn hiệu được bảo hộ.
6. Render HyperFrames/FFmpeg nếu công cụ thực thi thật sự có mặt; chuyển động xen kẽ zoom/pan có kiểm tra toàn bộ cảnh. Duy trì phụ đề nằm trong vùng an toàn và nhạc nền thấp hơn giọng.
7. Kiểm tra MP4 đã mã hóa: số khung hình, thời lượng, tiếng, điểm im lặng, khung đen, sai khác phụ đề, cấp phép từng asset. Không nhận HTML preview là video thành phẩm.
8. Giao storyboard + bản nháp cho người dùng duyệt trước khi đăng. Không tự đăng video hay tải lên tài khoản mạng xã hội.

## Bảo mật, OAuth và tài nguyên
- Nghiêm cấm tự động chạy `curl | sh`, `install.sh`, `--with-local-proxy`, `bootstrap`, `login`, `--accept-oauth-risk`, hoặc khởi động CLIProxyAPI trong ChatGPT.
- CLIProxyAPI là proxy OAuth bên thứ ba, KHÔNG phải API chính thức. Không tự cài hoặc dùng tài khoản, kể cả khi người dùng nói 'cài repo'. Muốn thiết lập cần lần đồng ý riêng minh thị với điều khoản, quyền và số lượng ảnh thử, người dùng tự đăng nhập, bind 127.0.0.1 và hạn mức kiểm soát.
- Không đọc, in hoặc upload API keys, .env, cookie, auths, client.env, session logs hay nội dung dự án riêng tư.
- Mặc định sử dụng built-in ImageGen trên host khi có sự cho phép cho tác vụ ảnh, KHÔNG giả định có quyền chạy tool trên máy Windows hay GPU server.
- Edge TTS, HyperFrames, FFmpeg, nội dung nguồn, nhạc và mô hình hình ảnh được cấp phép độc lập. Kiểm tra quyền thương mại trước xuất bản.
- Nếu không có runtime, kết quả chỉ là SPEC/STORYBOARD/INSTALL PLAN; đừng khai báo [DEPLOYED], video render hay cài thành công trên PC.

## Phương án triển khai PC sau kiểm toán
Clone repo bằng Git trong sandbox hoặc máy người dùng, pin commit, kiểm tra LICENSE và `scripts/` rồi cài các phụ thuộc Node 22+, Python, Edge-TTS, FFmpeg. Các lệnh cài phải được kiểm tra trước, KHÔNG dùng tùy chọn proxy/OAuth. Vì upstream ưu tiên bash, Windows nên dùng WSL2 nếu cần shell. Không ghi đè project cũ. Có thể kiểm tra Node scripts bằng `node --check` và Bash bằng `bash -n`, không thay thế kiểm thử end-to-end.

## Tình trạng bản adapter
Bản hướng dẫn đã đóng gói trong plugin; engine HBG gốc và local CLIProxyAPI chưa được chạy trên máy người dùng. Repo MIT; thành phần phụ thuộc có thể có giấy phép khác.
