---
name: music-midi-arrangement-vn
description: "Tạo MIDI Standard MIDI File và bản nhạc MusicXML không cần API/trả phí từ dữ liệu nốt/hợp âm do người dùng cung cấp hoặc được sáng tác; tương thích nhập vào DAW/MuseScore. Cụm 13."
---
# Music MIDI & Arrangement VN — Cụm 13 Nội dung & đa phương thức

## Phạm vi
- Dùng `scripts/score_export.py` (Python stdlib) sinh bản MIDI giai điệu đơn âm và MusicXML part một dòng từ JSON cao độ và trường độ.
- Đây là bản nhạc dữ liệu máy đọc được, KHÔNG phải bản ghi MP3/giọng hát/nhạc cụ thật. Phối khí nhiều track, VST, mix/master phải thực hiện trong phần mềm âm thanh chuyên dụng hoặc backend đã được kết nối.
- Input JSON ở `examples/melody.json`; lệnh minh họa sau chỉ chạy trong môi trường được người dùng cho phép:

```bash
python scripts/score_export.py --input examples/melody.json --midi output.mid --musicxml output.musicxml
python -m unittest discover -s tests -v
```

## Bảo đảm
- Không cần pip, không tải thư viện, không tự gọi mạng, không thu thập secret, không phát sinh credit.
- Kiểm tra BPM từ 40–240, pitch 0–127, duration thuộc {0.25, 0.5, 1, 2, 4}, giới hạn số nốt; fail closed với dữ liệu bất hợp lệ.
- MusicXML version 4.0, ký hiệu đơn giản khóa G và 4/4; xem bảng điều kiện dùng trước khi xuất bản nhạc phức tạp, không quảng cáo khả năng hỗ trợ polyphony/điều hòa nhiều track.
- Nếu không được thực thi script hoặc chưa đọc được kết quả, trạng thái `packaged_only`, không phải `verified_audio`.
