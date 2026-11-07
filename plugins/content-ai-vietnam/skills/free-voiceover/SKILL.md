---
name: free-voiceover
description: "Dùng khi cần giọng đọc miễn phí chạy tại máy, tạo tiếng Việt từ văn bản, clone giọng từ file được phép, hoặc nhà cung cấp trả phí hết credits."
---
# Giọng đọc miễn phí cho quy trình nội dung/video

Đọc [triển khai và nguồn](references/SETUP.md). Có adapter Python đóng gói, không có engine hay máy chủ suy luận được nhúng sẵn. Chỉ đánh dấu đã tạo giọng sau khi có WAV thật và kiểm tra. Không tự tuyên bố miễn phí cloud/GPU hoặc clone giống tuyệt đối.

Với video Tò Mò Lab, xem [cấu hình giọng Adam đã dùng](references/TO_MO_LAB_ADAM.md): ưu tiên đúng preset vidIQ Adam đã dùng trước đây; kiểm tra voice ID và quota mỗi lần. Không thay bằng preset cùng tên của engine khác.
Khi cần chuyển Adam sang công cụ TTS khác, đọc [bảng tương thích theo catalog](references/ADAM_PORTABILITY.md); chỉ ánh xạ exact voice ID, không coi voice cùng tên là cùng identity.

1. Dùng VieNeu-TTS v3 Turbo cho tiếng Việt trên CPU; VoxCPM2 là lựa chọn đa ngôn ngữ khi tài nguyên phù hợp. Không thay tuyến đang chạy tốt ngoài phạm vi người dùng giao. Khi dịch vụ hết credits, đề xuất hoặc dùng tuyến local nếu đã được ủy quyền và môi trường sẵn sàng, không tự chi tiền hay tạo bản nhạc thay lời đọc mà gọi là video đầy đủ.
2. Trước clone, xác định file, người nói và bằng chứng đồng ý. Chỉ clone giọng của người dùng hoặc người cho phép. Upload hoặc yêu cầu chung không tự chứng minh quyền người nói. Không dùng file Adam thương mại để clone khi chưa xác minh quyền; preset Adam của VieNeu là danh tính khác Adam vidIQ/ElevenLabs, không gắn nhãn thay thế tương đương.
3. Chốt kịch bản, giọng/preset và quyền thương mại. Giọng mặc định mới hoặc preset khác chỉ thay giọng đã chọn khi người dùng đồng ý. Có thể tạo giọng mới không clone bằng VoxCPM2. Dùng file gốc một người nói, không nhạc; VieNeu v3 khuyến nghị đoạn ngắn 3–8 giây. Không tự tải file riêng sang demo công cộng.
4. Kiểm tra runtime với `python scripts/free_voiceover.py --doctor`. Nếu không có SDK/model, ghi đúng thiếu thành phần; có quyền triển khai thì dùng môi trường ảo riêng và hướng dẫn SETUP, không cài vào hệ thống chung. Không mặc định ChatGPT đọc được ổ C hoặc localhost trên máy người dùng.
5. Tạo WAV bằng adapter khi có runtime được phép; engine chạy 1x. Cờ --allow-model-download chỉ cho phép SDK tải model ở máy đang chạy; không mở phí dịch vụ. Lưu metadata về engine/giọng/quyền/thời lượng. Khi người dùng yêu cầu so sánh giọng, dùng voice-selection, chọn hai ứng viên phù hợp thay vì tạo hàng loạt mặc định.
6. Đo audio thật; sau đó ASR/forced alignment để tạo SRT và phụ đề khớp. Không chia đều từ để giả đồng bộ, không tăng tốc để ép thời lượng. Giữ stem giọng/nhạc riêng, nhạc nhỏ hơn giọng, kiểm tra clipping, nghe trọn đoạn hoặc ghi listening_review=not_performed.
7. Bàn giao WAV, metadata và kịch bản vào bộ dựng. Trạng thái: packaged → runtime_ready → synthesized → aligned → reviewed. Chỉ nói DEPLOYED khi có health/inference thật. Không tự đăng video.

Mã kiểm tra quyền chỉ là chốt vận hành, không tự xác minh pháp lý người nói. Không lưu transcript hoặc file mẫu vào log công khai. Quyền model, preset, reference và bản nhạc là những thứ riêng biệt.

## Bổ sung bốn nguồn và chọn chất lượng
Khi cần Chatterbox, OpenVoice V2, Qwen3-TTS, F5-TTS hoặc so sánh đầu ra, đọc [voice-selection](../voice-selection/SKILL.md). Phân biệt adapter local sẵn có với runtime upstream chưa cài. Không lấy sample rate làm điểm chất lượng.
