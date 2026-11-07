---
name: voxcpm-authorized-cloning-vn
description: Dùng khi người dùng muốn nhân bản giọng của chính họ hoặc một người đã cho phép bằng VoxCPM2, tạo voiceover từ file WAV tham chiếu, điều chỉnh cảm xúc và kiểm chứng nguồn âm thanh cho VIDEO AI.
---

# VoxCPM2 — Nhân bản giọng có sự cho phép

## Quyền và an toàn
Chỉ nhân bản giọng của chính người dùng hoặc khi đã xác nhận chủ giọng cho phép sử dụng với phạm vi phù hợp. Không phục vụ giả mạo, lừa đảo, thao túng, tạo phát ngôn sai hoặc tuyên bố chứng thực giả. Không yêu cầu gửi mật khẩu, cookie phiên, khoá API, dữ liệu nhạy cảm. Nhãn AI-generated cho audio phát hành công khai.

## Hai cách tạo
- **Controllable Voice Cloning:** âm thanh mẫu qua `reference_wav_path` / `--reference-audio`, có thể điều chỉnh phong cách bằng phần mô tả trong text.
- **Ultimate Cloning:** thêm `prompt_wav_path` và bản transcript chính xác `prompt_text`, hữu ích cho độ giống và nhịp đọc; không suy diễn transcript nếu chưa kiểm tra.

## Quy trình
1. Hỏi quyền sử dụng mẫu khi chưa rõ; nhận WAV/MP3 người dùng có quyền, tốt nhất giọng sạch không nhạc/ồn.
2. Kiểm tra audio: ngôn ngữ, mức ồn, clip/đỉnh, thời lượng và transcription thật.
3. Lập kịch bản và thông số giọng đọc; ưu tiên tập tin WAV tham chiếu lưu local, không công khai.
4. Chỉ khi có VoxCPM runtime và tệp mẫu sẵn có, dùng lệnh chính thức như bên dưới; xác minh output tồn tại bằng file và nghe thử.
5. Kiểm tra nội dung không tự thêm cam kết/y tế/pháp lý không có căn cứ; lưu nguồn quyền và phiên bản kịch bản.
6. Chỉ bàn giao audio cho video sau khi người dùng chấp thuận nếu đây là dự án VIDEO AI.

## Lệnh CLI VoxCPM2
```powershell
# Ví dụ: dùng mẫu giọng mà chủ giọng đã cho phép, chạy trên máy đã cài VoxCPM2
voxcpm clone --text "Xin chào, đây là bản thuyết minh AI đã được cho phép." --reference-audio "C:\AI-VIDEO\voxcpm2\input\reference.wav" --output "C:\AI-VIDEO\voxcpm2\output\voiceover.wav"
```

## Không được khẳng định
Không gọi việc gửi một đoạn âm thanh vào ChatGPT là đã tạo bản sao giọng nếu chưa có model backend; không viện dẫn Google Drive hay Windows như đã đọc nếu chưa có quyền truy cập thực tế. Không gọi một giọng preset của công cụ khác là VoxCPM2.

Nguồn: https://github.com/OpenBMB/VoxCPM ; https://openbmb.cn/docs/en/guides/voxcpm
