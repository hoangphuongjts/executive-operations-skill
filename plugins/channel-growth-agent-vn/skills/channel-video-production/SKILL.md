---
name: channel-video-production
description: "Kích hoạt khi người dùng yêu cầu Xây Kênh hoặc Tò Mò Lab dựng/xuất MP4 hoàn chỉnh, video dài 3–15 phút, video Shorts/Reels 45–90 giây, lồng giọng đọc Adam có quyền sử dụng, nhạc nền, phụ đề SRT, đồng bộ hoặc kiểm tra chất lượng video."
---
# Xây Kênh — Sản Xuất Video Hoàn Chỉnh

## Ưu tiên
Trách nhiệm của agent là **xuất video thật** khi có backend và quyền truy cập, không chỉ tạo kịch bản hoặc tuyên bố tạo xong. Đọc `references/production-guide.md` và `references/qa-checklist.md`. Thực hiện cùng `channel-growth-agent` (giữ nghiên cứu, SEO, lịch xuất bản, analytics).

## Nhận brief và quyết định định dạng
Mặc định Tò Mò Lab giáo dục khoa học; giữ yêu cầu lịch sử liên quan bản quyền, phê duyệt và giọng Adam. Video ngắn 45–90 giây / 9:16 / 1080×1920 (khi gói hỗ trợ). Video dài 3–15 phút / 16:9 / 1920×1080 (khi gói hỗ trợ). Có thể làm 90 giây–3 phút nếu mục tiêu yêu cầu; không giới hạn giả. Quyết định theo yêu cầu cụ thể, nội dung và chi phí, không tự chọn nâng cấp lên 4K.

## Tuyến sản xuất
1. Kiểm tra nội dung, nguồn tài liệu, hình ảnh/clip đã có, quyền, mức độ chính xác khoa học.
2. Viết kịch bản có nhịp cảnh và bản thời gian; lời đọc; danh sách tài nguyên; chú giải kỹ thuật và SEO.
3. Lập media manifest: nguồn, giấy phép, id file/video/voice, tỉ lệ, từng đoạn thời gian; kiểm tra tài nguyên đã tồn tại.
4. Ưu tiên backend có thể xuất MP4: công cụ HeyGen Studio đã xác minh; nếu có nguồn riêng và phần mềm thực thi thì FFmpeg/Remotion. HeyGen Video Agent dùng khi mong muốn dàn dựng mở; có thể thay lời, không chọn nếu bắt buộc phát đúng bản thu.
5. Trước phát sinh chi phí, kiểm tra gói/hạn mức có sẵn và quy tắc đồng ý. Không phát lệnh tiêu credits chưa được cho phép. Không nhân bản giọng của người khác nếu chưa được người nói đồng ý rõ.
6. Kết hợp cảnh, âm thanh, phụ đề, xuất file thật; nếu thiếu khả năng mix nhạc hoặc đồng bộ, dùng hậu kỳ FFmpeg trong môi trường được phép thay vì tự nhận đã làm.
7. Chỉ báo "Đã xuất MP4 hoàn chỉnh" sau khi có kết quả render đã hoàn tất, có video URL/tệp thực và kiểm tra âm thanh, thời lượng, khung hình, phụ đề. Nếu máy chủ đang xử lý, báo "Đang dựng" (không hứa giao sau); nếu lỗi, báo lỗi.
8. Không tự đăng. Chỉ tải Drive đúng thư mục khi được yêu cầu và có kết nối có quyền.

## Tránh hiểu nhầm khả năng
Plugin chỉ chứa workflow và không tích hợp một engine render mới. HeyGen/Runway/Higgsfield và những tool khác chỉ dùng khi thật sự đang kết nối. Sự hiện diện của công cụ không chứng minh đã hoàn thành render hoặc đã thanh toán. Xuất dữ liệu dạng JSON, script, ZIP, storyboard không được coi là video.

## Tương thích nhiều dự án

Yêu cầu định dạng, thương hiệu và giọng đọc trong brief hiện tại được ưu tiên hơn cấu hình gợi ý Tò Mò Lab/Adam. Các giới hạn dịch vụ trong tài liệu là tham khảo cần xác minh bằng tool/schema hiện tại. Đọc [trạng thái và tài sản](../../references/channel-workflow.md) để phân biệt render, QA, duyệt và đăng. Không thêm khâu phê duyệt nếu ủy quyền hiện có đã đủ cho hành động; vẫn tuân thủ yêu cầu cụ thể của công cụ.

## Giọng đọc local miễn phí
Với video Tò Mò Lab, mặc định dùng preset Adam vidIQ đã cấu hình trong [free-voiceover](../free-voiceover/SKILL.md) và [hướng dẫn Adam](../free-voiceover/references/TO_MO_LAB_ADAM.md); kiểm tra voice ID/quota trước khi tạo. Nếu dùng tool khác, kiểm tra [khả năng ánh xạ cùng Adam](../free-voiceover/references/ADAM_PORTABILITY.md); không thay bằng voice chỉ trùng tên. Khi exact voice không khả dụng, để voiceover chờ và báo rõ; chỉ dùng giọng local khác nếu người dùng đồng ý và runtime sẵn sàng.
