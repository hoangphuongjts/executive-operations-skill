# Tò Mò Lab — giọng đọc Adam đã dùng

## Mặc định giọng

Khi brief là video Tò Mò Lab và người dùng không yêu cầu đổi giọng, ưu tiên preset công khai **Adam - Dominant, Firm** trong vidIQ Voiceover. Voice ID đã dùng trước đây: `pNInz6obpgDQGcFmaJgB`. Đây là preset tổng hợp của nhà cung cấp, không phải bản clone giọng của một người thật.

Trước mỗi lần tạo, gọi danh sách voice vidIQ và xác nhận đúng tên/ID còn khả dụng; dùng nguyên `voiceId` do danh sách trả về với `vidiq_voiceover_generate`. Chỉ tạo một bản từ kịch bản cuối đã thống nhất. Chờ job hoàn tất rồi kiểm tra file âm thanh thực, thời lượng và phát âm trước khi mix.

## Khi không dùng được Adam

- Kiểm tra quota/tình trạng công cụ trước khi gọi tạo. Nếu hết credits, công cụ không kết nối hoặc voice ID không còn trong danh sách, không gọi lặp, không tiêu khoản phí khác và không tự đổi sang giọng gần giống.
- Có thể đề xuất VieNeu-TTS hoặc engine local khác nếu runtime đã sẵn sàng, nhưng preset Adam của VieNeu là một giọng khác, không tương đương Adam vidIQ. Chỉ đổi khi người dùng đồng ý.
- Không lấy audio Adam đã phát hành làm mẫu để clone. Đây là preset tổng hợp; không cần clone. Chỉ clone một người nói khi đã có quyền và đồng ý rõ.
- Trước nội dung thương mại, xác minh điều khoản hiện hành của dịch vụ/voice. Việc voice xuất hiện trong danh sách không tự chứng minh quyền thương mại.

## Handoff dựng video

Giữ file voice gốc riêng, đo thời lượng audio thật, căn SRT theo audio (ASR/forced alignment hoặc rà soát nghe), rồi mix giọng trên nhạc nền. Không kéo giãn lời để vừa thời lượng dự kiến; chỉnh script hoặc nhịp dựng. Nếu không tạo được WAV thì trạng thái là bản hình/phụ đề chưa có lời đọc.
