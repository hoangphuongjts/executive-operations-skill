---
name: ai-promo-video-maker-vn
description: Điều phối video quảng bá sản phẩm, website, ứng dụng, khóa học qua kịch bản, kiểm chứng nguồn, storyboard, ảnh chụp giao diện thật, Remotion, giọng đọc, phụ đề, QC và video 4K/9:16. Skill hướng dẫn không tự render.
---

# AI Promo Video Maker VN — adapter an toàn cho Hoangphuong Core

## Nguồn gốc và phạm vi
- Upstream: https://github.com/liyupi/ai-promo-video-maker
- Maintainer: liyupi. README và AGENTS.md được đối chiếu ngày 2026-11-05; giấy phép kho gốc MIT, phải giữ thông báo copyright/giấy phép nếu tái phân phối mã gốc.
- Đây là adapter hướng dẫn được viết mới, KHÔNG chép mã engine gốc, không có FFmpeg, Remotion hay ElevenLabs runtime trong ChatGPT.
- Hướng tới workflow `Hoangphuong` (đặc tả/kiểm toán), `sanxuatnoidung` (kịch bản) và `phattrienungdung` (dựng engine khi được cấp quyền). Không giả vờ liên kết API runtime giữa plugin.

## Điều kiện pháp lý và an toàn
- Remotion có điều khoản giấy phép riêng (https://www.remotion.dev/license); xác minh điều kiện theo quy mô nhóm và mục đích sử dụng.
- ElevenLabs có chi phí/quyền khai thác thương mại tùy gói; KHÔNG tự gọi dịch vụ, đăng ký gói, thu phí, hay dùng khóa API chưa được cấp quyền. Nếu thiếu, dùng phương án âm thanh gốc được phép hoặc để người dùng cung cấp.
- Ảnh, logo, màn hình, nhạc, video, giọng nói phải thuộc quyền sở hữu hoặc được cấp phép thương mại. Không tự nhận Mixkit/stock là mặc nhiên an toàn; kiểm chứng từng tài nguyên và lưu giấy phép vào MANIFEST.
- Không upload, public, đăng kênh xã hội, thu thập tài khoản hoặc đăng nhập hộ nếu chưa được phê duyệt.
- Không chạy script từ GitHub vô điều kiện. Pin commit; kiểm tra `AGENTS.md`, `template/package.json`, requirements, dependency lock/install scripts, paths, outputs, secrets; chạy cách ly.

## Quy trình
1. Xác định sản phẩm, đối tượng, thời lượng, 16:9 / 9:16, thông điệp, các nguồn hợp lệ; dùng giá trị đã biết, chỉ hỏi khi thực sự thiếu.
2. Phân tích sản phẩm và dữ kiện từ trang chính thức. Không bịa thông số, lượt dùng, lời chứng thực.
3. Đưa ra 3–4 hướng phong cách độc lập và một storyboard mẫu, phê duyệt hướng trước render.
4. Lập kịch bản với hook trong 3 giây; chia các cảnh theo thời gian, thông điệp, chuyển cảnh, nguồn minh họa; không biến quy tắc gốc thành khẳng định hiệu quả chắc chắn.
5. Lập danh mục ảnh chụp giao diện thật; chỉ dùng ảnh/chụp có quyền; bảo vệ PII, account và credential.
6. Tạo project Remotion khi có runtime hợp lệ: Node.js >=18, Python >=3.9, FFmpeg, Playwright Chromium; xét phụ thuộc từng phiên bản; không tự cài global.
7. Âm thanh: giọng đọc do người dùng cấp quyền (giọng Adam nếu có tệp/nhà cung cấp hợp lệ); âm nhạc thấp hơn lời đọc, phụ đề đồng bộ, có transcript QA.
8. QC trước và sau render: frame size, 30 fps, không đen/trắng lỗi, font tiếng Việt, render log, clipping, âm lượng lời thoại, phụ đề, giấy phép và fact-check.
9. Bàn giao MP4 + project + storyboard + nguồn + MANIFEST + báo cáo QC; chờ duyệt trước đăng.

## Cài upstream trên Windows khi được phép
- Tải về `D:\AI-VIDEO\ai-promo-video-maker` bằng `git clone`, không xóa hoặc cập nhật repo cũ tự động.
- Dùng venv riêng, cài requirements và `playwright install chromium`, chạy `python template/scripts/doctor.py`.
- Windows không phải nền tảng được tác giả thử đầy đủ, có thể cần điều chỉnh lệnh bash và dấu `/` trong scripts.
- Repo gốc là skill + template, không phải dịch vụ video đã deploy; ChatGPT skill không chạy lệnh `npm`, không tự xuất MP4.

## Phối hợp với các plugin đã có
- Opus Video Skills VN / ClaudeAnimationBase: tùy phong cách vẽ tay. Không thay engine hoặc ép dùng ví dụ gốc.
- Content AI Việt Nam / Xây Kênh: kịch bản, nhận diện, kế hoạch đăng; quyền đăng bài chỉ sau duyệt.
- Hoangphuong Core: điều phối kiến trúc, bảo mật, ghi rõ trạng thái DESIGNED/PACKAGED/TESTED/DEPLOYED.

## Quy tắc bảo toàn
Không sửa 7 Skill gốc, 128 role, 16 cụm, 108 mã slash học tập, hoặc plugin khác. Mọi kết quả cần phân biệt skill guidance và engine executable.
