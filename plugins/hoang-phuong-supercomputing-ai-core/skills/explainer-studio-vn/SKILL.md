---
name: explainer-studio-vn
description: "Hướng dẫn tiếng Việt dùng reedodev/explainer-studio để lập storyboard có nguồn, chọn 8 phong cách đồ họa vẽ tay, dựng MP4/SRT bằng Node.js và FFmpeg; chỉ sử dụng engine khi có môi trường thực thi được phép."
---

# Explainer Studio VN — Hoangphuong Supercomputing Core adapter

Nguồn gốc: https://github.com/reedodev/explainer-studio (MIT, copyright 2026 Reedo). Đây là adapter hướng dẫn riêng, không chứa engine gốc, không phải chứng cứ rằng engine được cài hoặc đang chạy. Upstream skill: `skills/explainer-studio/SKILL.md`.

## Chế độ vận hành
- Mặc định `skills_only`: hỗ trợ nghiên cứu, kịch bản, storyboard JSON, nguồn, styleframes, lệnh dựng, QC; không nhận là đã render trừ khi có tệp MP4 thực tế và ffprobe.
- Không tự thực thi script từ GitHub hoặc cài Node/npm/FFmpeg trên máy người dùng; chỉ trong môi trường thực thi được cấp phép, theo phiên bản commit đã kiểm tra, và sau khi soát dependency/install hooks.
- Không sửa hoặc thay thế Core, 7 Skill gốc, 128 hồ sơ, 16 cụm, 108 slash code, HBG, Adu Motion, Spec Kit hay OAuth. Không tự đăng video.
- Giấy phép: engine MIT, nhưng thư viện, font, TTS và tài sản người dùng có điều kiện riêng. Giữ LICENSE/attribution theo yêu cầu; kiểm tra quyền thương mại của âm thanh, font, dữ liệu, hình ảnh và giọng nói.

## Năng lực thực tế theo upstream
- 8 style: `whiteboard`, `swiss-motion`, `blueprint`, `ink-wash`, `urban-sketch`, `spy-titles`, `shadow-puppet`, `ascii-crt`.
- Đầu vào: chủ đề, câu hỏi, nguồn tri thức; soạn storyboard JSON. Đầu ra khi engine chạy: 1920x1080, 30 fps, H.264/AAC MP4, phụ đề SRT, contact sheet, báo cáo xác thực.
- Phù hợp: video giải thích 45–60 giây, bảng so sánh, sơ đồ khoa học, kiến thức lớp 6–12. Không hứa hỗ trợ native 9:16, nhân vật chuyển động toàn thân, 3D hoặc quay màn hình.
- Phụ thuộc: Node >=20, npm, FFmpeg/ffprobe; `npm ci` khi đã soát file khóa, `@napi-rs/canvas`, `roughjs`, `zod`, `msedge-tts`. Chế độ `edge` qua endpoint không chính thức có thể lỗi HTTP 403; `sapi` trên Windows hoặc `cmd` là phương án thay thế; `silent` để kiểm thử không tiếng.

## Quy trình 8 bước
1. Xác định chủ đề và khán giả; rà soát nguy cơ sai lệch, lựa chọn định dạng landscape nếu dùng engine nguyên gốc.
2. Kiểm chứng các tuyên bố và số liệu; đưa URL/cấp phép vào `research/sources.json`; không tạo số liệu minh họa mà không chú thích.
3. Lập narration và storyboard 6–8 cảnh; ưu tiên mở đầu cho thấy kết quả, quan hệ nhân quả, 4–9 yếu tố trực quan cho mỗi cảnh; dùng `reference/storyboard-recipes.md` từ repo gốc.
4. Khóa storyboard và style. Chọn một trong 8 style; có thể thử `styleframes --styles all` để so sánh.
5. Kiểm tra môi trường và phụ thuộc trước khi chạy, chỉ dùng mã đã soát. Không gọi API trả phí hoặc cung cấp khóa bí mật khi không có thỏa thuận quyền hạn.
6. Dựng preview silent, kiểm tra bố cục, vùng an toàn, subtitle, tốc độ vẽ, giá trị số; sửa warning/error rồi mới xuất.
7. Nếu cần lời đọc, chọn nhà cung cấp/giọng được phép, tạo TTS, đối chiếu transcript và kiểm tra nhạc nền thấp hơn lời đọc. SRT theo timeline thực tế hoặc nêu giới hạn căn chỉnh tỉ lệ.
8. `ffprobe` thành phẩm để xác minh fps, duration, audio/video codec; phát/kiểm tra hình âm thanh thực tế trước bàn giao. Không tuyên bố xuất MP4 nếu chưa có file.

## Lệnh tham khảo trong repo (KHÔNG có tác dụng trong ChatGPT nếu chưa triển khai runtime)
```bash
git clone https://github.com/reedodev/explainer-studio.git
cd explainer-studio
npm ci
npm run es -- build examples/fiber-optics --tts silent --style blueprint
npm run es -- styleframes examples/fiber-optics --styles all
npm run es -- init "Why do cats purr?" --slug cats
```
Đầu ra ví dụ: `examples/fiber-optics/variants/blueprint/final.mp4`; storyboard đang dùng có thể bị cập nhật đo thời lượng bởi lệnh build, vì vậy sao lưu đầu vào nếu cần giữ nguyên.

## Điều phối cùng Core
- Với video giáo dục: chọn `sanxuatnoidung` cho nội dung, `github500-citation-verification` hoặc `github500-research` để kiểm chứng, `github500-agent-supply-chain` để đánh giá tích hợp; dùng `explainer-studio-vn` cho thiết kế/kỹ thuật vẽ.
- Cần Shorts 9:16: thiết kế lại bố cục và engine riêng, hoặc chuyển sang công cụ đã xác minh hỗ trợ portrait; không coi crop là hỗ trợ gốc.
- Xuất bản: bắt buộc duyệt nội dung, nguồn, giấy phép và bản dựng trước khi đăng.

## Chứng cứ tích hợp
Plugin version 16.0.4 bao gồm Skill adapter này. Không được đồng nhất `HOST_VISIBLE` với engine cài trên máy, runtime backend, hay video MP4 thực tế. Kiểm toán upstream mới nhất/giấy phép lại trước mỗi lần chạy production.
