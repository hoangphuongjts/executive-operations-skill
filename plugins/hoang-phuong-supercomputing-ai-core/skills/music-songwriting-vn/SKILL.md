---
name: music-songwriting-vn
description: "Sáng tác ca khúc, viết lời nguyên bản, cấu trúc verse/chorus/bridge, hợp âm, giai điệu bằng nốt và xây bản thông số sản xuất âm nhạc tiếng Việt; Cụm 13 Hoàng Phương Core."
---
# Music Songwriting VN — Cụm 13 Nội dung & đa phương thức

## Triggers
Viết nhạc, sáng tác bài hát, lời nhạc, melody, hợp âm, bolero, ballad, pop, rap, EDM, nhạc nền, nhạc khoa học, jingle.

## Hợp đồng đầu vào
- Chủ đề, người nghe, phong cách, cảm xúc, ngôn ngữ, thời lượng, hình thức; hỏi một câu ngắn nếu thiếu thông tin thật sự thiết yếu.
- Bản mẫu nếu có: dùng làm tham khảo đặc điểm tổng quát, không sao chép ca từ/giai điệu hoặc bắt chước giọng một ca sĩ có thật khi không có quyền.
- Đầu ra mặc định gồm: tên, concept, BPM, nhịp, giọng/tonality, tiến trình hợp âm, cấu trúc, lời nguyên bản và mô tả giai điệu. Đầu ra kỹ thuật mở rộng: nốt dạng MIDI pitch + độ dài beat, MusicXML/MIDI offline nếu cần.

## Quy trình
1. Xác định chủ đề, thông điệp, nhạc tính; tránh biến một bài hát có bản quyền thành bản phỏng theo gần giống.
2. Chọn nhịp 4/4 hoặc 6/8, khóa nhạc, BPM và phong cách phối khí. Không bịa bằng chứng đã nghe nhạc hoặc đã render âm thanh.
3. Lên cấu trúc Intro → Verse → Pre-chorus (tuỳ chọn) → Chorus → Verse → Bridge → Final Chorus → Outro; không áp cấu trúc cứng nếu thể loại không phù hợp.
4. Viết lời tiếng Việt có nhịp âm tiết, dấu thanh và điểm nhấn hát được; rà soát lỗi lặp vần/độ dài dòng và từ khó phát âm.
5. Tạo bảng hợp âm theo ô nhịp, melody bằng ký hiệu có kiểm tra phạm vi âm; tránh tự tuyên bố giai điệu MIDI được sinh từ lời khi chưa có bước chuyển đổi.
6. Chuyển cho `music-midi-arrangement-vn` nếu cần tạo MIDI/MusicXML, `music-ai-render-bridge-vn` nếu cần đầu ra nghe được, `music-quality-audit-vn` khi phát hành.

## Đầu ra & chuẩn chất lượng
- Lyrics, lead sheet/hợp âm, sonic brief, lyric syllable review, prompt chuyên dụng theo nhà cung cấp; xuất từng tệp đúng ngữ nghĩa.
- Ghi rõ: `draft_written`, `musicxml_generated_offline`, `midi_generated_offline`, `audio_generated_provider` hoặc `blocked`, không gom vào "đã hoàn thành".
- Giữ quyền riêng tư, bản quyền lời/tư liệu, quyền sử dụng giọng hát, quyền phát hành theo điều khoản nguồn âm thanh.
