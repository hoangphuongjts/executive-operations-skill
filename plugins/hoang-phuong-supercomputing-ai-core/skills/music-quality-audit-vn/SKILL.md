---
name: music-quality-audit-vn
description: "Rà soát bản quyền, phát âm tiếng Việt, quyền giọng hát, cấu trúc, metadata và tiêu chuẩn kiểm tra file MP3/Audio sáng tác; Cụm 13 + kiểm định Cụm 16."
---
# Music Quality Audit VN — Cụm 13, kiểm tra chéo Cụm 16

## Checklist kiểm định
1. Lời nguyên bản, không sao chép giai điệu/bản ghi, không tuyên bố độc quyền tuyệt đối chỉ dựa vào mô hình tự đánh giá.
2. Kiểm tra vần, nhịp, thanh điệu tiếng Việt, rõ lời, cường độ cảm xúc, cấu trúc lặp; nhận xét các câu có rủi ro khó hát.
3. Kiểm tra hợp âm, tonal center, dải nốt với thông số thật của file nếu có.
4. Chỉ khi MP3 đã sinh thật mới kiểm tra bằng file/tool: codec, thời lượng, sample rate, peak/clipping, silence, loudness nếu có FFmpeg/ffprobe hoặc công cụ tương ứng.
5. So sánh cấu trúc file MusicXML/MIDI với bản score đầu vào; nếu không có file audio, ghi `audio_qa_not_performed`.
6. Trước phát hành: nguồn giọng hát, consent, giấy phép thương mại, quyền bản phối, watermark và chính sách nền tảng; giữ bằng chứng quyền sử dụng.

## Xuất báo cáo
Bảng `criterion`, `evidence`, `status` (pass/fail/not_tested), `next_action`; phân biệt QA văn bản, QA MIDI, QA audio và kiểm toán pháp lý. Không tuyên bố chuẩn broadcast nếu không có đo âm thanh thật.
