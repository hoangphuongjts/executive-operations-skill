---
name: voxcpm-voice-design-vn
description: Dùng khi người dùng muốn tạo giọng đọc AI tiếng Việt mới bằng VoxCPM2, chỉnh biểu cảm, tốc độ, kịch bản và lời thoại cho quảng cáo, Shorts, Reels, TikTok, YouTube hoặc VIDEO AI.
---

# VoxCPM2 — Voice Design tiếng Việt

## Mục đích
Hỗ trợ người dùng chọn phong cách giọng mới **không sao chép danh tính giọng của người khác**, thiết kế nội dung tiếng Việt, và chuẩn bị lệnh chạy bằng mô hình VoxCPM2 của OpenBMB.

## Dữ kiện kỹ thuật đã xác minh
- Repo chính thức: https://github.com/OpenBMB/VoxCPM
- Tài liệu: https://voxcpm.readthedocs.io/en/latest/quickstart.html
- VoxCPM2: 2B tham số; hỗ trợ tiếng Việt trong 30 ngôn ngữ, WAV 48 kHz (theo trang dự án); Python >=3.10,<3.13, PyTorch >=2.5, CUDA >=12 cho đường chạy GPU phổ biến.
- Mã và trọng số được công bố Apache-2.0. Kiểm tra tiếp giấy phép của audio/nhạc/voice tham chiếu.
- Plugin này là **skills-only**: KHÔNG có runtime PyTorch, backend TTS, MCP, API endpoint hay quyền truy cập GPU/máy Windows. Không báo đã tạo giọng khi chưa có tệp audio thật.

## Quy trình
1. Nhận bối cảnh: kênh, đối tượng, thời lượng, giọng nam/nữ, chất giọng, nhịp, sắc thái.
2. Viết văn bản đọc tự nhiên tiếng Việt, tránh từ quá dài và chuẩn hoá dấu, con số, tên riêng.
3. Nếu muốn giọng mới, dùng Voice Design; tránh giả giọng người thật không được phép.
4. Sau khi backend VoxCPM2 thực sự cài xong, hướng dẫn chạy và kiểm tra WAV; nếu không có backend, chỉ cung cấp cấu hình/lệnh.
5. Nghe kiểm tra phát âm tiếng Việt, tiếng Anh xen kẽ, ngữ điệu, âm lượng, nhiễu và độ lệch thời gian; cắt/ghép bằng FFmpeg khi được yêu cầu.
6. Nếu dùng cho công chúng, gắn nhãn AI voice khi phù hợp và ghi nhận nguồn/giấy phép.

## Ví dụ chính thức
```powershell
# Chạy sau khi đã cài VoxCPM và kích hoạt đúng môi trường Python
voxcpm design --text "(Giọng nữ trẻ trung, ấm áp, nhịp rõ ràng)Xin chào, chào mừng bạn đến với Tò Mò Lab!" --output giọng-thử.wav
```

## Ràng buộc khi phối hợp VIDEO AI
- Không đăng mạng xã hội trước khi người dùng duyệt.
- Không tự mua credit hay dùng dịch vụ trả phí.
- Mỗi file âm thanh ghi rõ trạng thái preview/final, tập nào, ngôn ngữ, sample rate và quyền sử dụng.
