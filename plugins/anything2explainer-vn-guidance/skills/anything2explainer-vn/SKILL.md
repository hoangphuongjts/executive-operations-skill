---
name: anything2explainer-vn
description: "Bộ hướng dẫn tiếng Việt cho quy trình video thuyết minh dựa trên dự án anything2explainer của Vincentwei1021: nghiên cứu, kịch bản, TTS, storyboard, Remotion, kiểm tra chất lượng; bắt buộc kiểm tra giấy phép trước khi dùng engine gốc."
---

# Anything2Explainer VN — Optional, guidance-only

## Nguồn, giấy phép và phạm vi
- Upstream: https://github.com/Vincentwei1021/anything2explainer
- License upstream: PolyForm Noncommercial 1.0.0; copyright notice (c) 2026 Vincent Wei.
- **Không** sao chép hoặc nhúng mã upstream ở đây. Gói này là Skill hướng dẫn viết độc lập, không chứa executable/Remotion template, không tự cài thư viện hoặc chạy render.
- Các video tạo ra thuộc về người tạo theo tuyên bố README, nhưng sử dụng toolkit trong bối cảnh thương mại phải xin phép chủ sở hữu trước. Việc dùng để sản xuất nội dung cho kênh có kiếm tiền/quảng cáo không mặc nhiên được cấp phép.
- Font và Remotion có các điều khoản riêng. Kiểm tra license và quyền dùng thương mại, và lưu bằng chứng trước khi triển khai.

## Cách kích hoạt
Khi người dùng yêu cầu làm video explainer hoặc đưa bài viết, dữ liệu, chủ đề vào video, hỗ trợ các giai đoạn:
1. Xác định chủ đề, người xem, độ dài, ngôn ngữ, mục đích thương mại hay phi thương mại.
2. Kiểm chứng nguồn chính quy và trích dẫn; phân biệt dữ kiện xác minh với sơ đồ minh họa.
3. Viết script thuyết minh và bố cục, xin duyệt nội dung trước các thao tác có chi phí hoặc việc đăng tải.
4. Thiết kế storyboard khớp lời đọc; quy định rõ thời gian từng cảnh, nhịp chuyển và safe area.
5. Đề xuất TTS có giấy phép rõ ràng, sử dụng giọng tham chiếu chỉ khi có quyền hợp lệ; không mặc định tái tạo giọng cá nhân.
6. Lập đặc tả giao diện Remotion React + TypeScript, phụ đề đồng bộ, thanh tiến độ, HUD và đồ họa nguyên bản.
7. Đề xuất kiểm thử preview ngắn, QC hình/âm/thời gian và xuất MP4 tại máy hoặc môi trường được cấp phép.
8. Lưu manifest nguồn/giấy phép, report kiểm thử và các yêu cầu phê duyệt. Không đăng lên mạng xã hội khi chưa được duyệt.

## Cấu hình upstream tham khảo (không phải năng lực đã cài)
- Video 16:9, 1280x720, 30 fps; H.264; 2–8 phút; tiếng Anh/Trung.
- Node >=18, FFmpeg, Python3, Remotion4, React, TTS. Upstream shell zsh/macOS; Windows chưa được xác nhận bởi tác giả.
- Chuyển sang tiếng Việt hoặc 9:16 đòi chỉnh sửa engine và kiểm thử độc lập; không hứa hỗ trợ sẵn.
- Render bằng Remotion/FFmpeg chỉ khi đã xác nhận giấy phép và runtime thực sự sẵn sàng.

## Tích hợp an toàn với Hoangphuong Core
- Chỉ routing sang Skill này khi nội dung đòi video giải thích bằng đồ họa chuyển động; không sửa 7 Skill gốc, 128 hồ sơ Agent, 16 cụm, 108 mã học tập, catalog 500 repo hoặc các module đang cài.
- Trường hợp nội dung thương mại hoặc chưa rõ: chỉ tư vấn, phác thảo quy trình và đề xuất triển khai clean-room dựa trên Remotion theo giấy phép riêng, không sao chép template/scene upstream.
- Trạng thái chuẩn: guidance skill installed, upstream engine NOT installed, no service deployed, no validated MP4.
- Không thực thi lệnh có tải/install, truy cập bí mật, đăng bài hoặc thanh toán mà không có quyền hợp lệ và kiểm soát rủi ro.
