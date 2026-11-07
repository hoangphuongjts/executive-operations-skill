---
name: moneyprinter-ai-video-vn
description: Điều phối nội dung video AI bằng tiếng Việt dùng MoneyPrinter hoặc MoneyPrinterTurbo kết hợp HyperFrames, Herk Edit Kit, Video ShotCraft, Gemini CLI và n8n; bảo đảm không ghi đè module và không đăng trước khi duyệt.
---

# Điều phối MoneyPrinter với hệ sinh thái VIDEO AI

## Vai trò từng thành phần

- MoneyPrinter / MoneyPrinterTurbo: tự động tạo phần nội dung/kịch bản, thu thập/chuẩn bị footage (quyền sử dụng phải kiểm tra), lồng tiếng/phụ đề và dựng thô.
- Video ShotCraft VN: lựa chọn bố cục, hiệu ứng, storyboard, shotlist và phương án Remotion.
- HyperFrames + Herk Edit Kit: tinh chỉnh video HTML/motion, kiểm tra lời thoại, cắt cảnh, dựng MP4.
- Gemini CLI: đọc SKILL và cộng tác dựng trên môi trường người dùng có quyền thực thi.
- n8n (nếu có): nhận brief, tạo job, chờ render, chuyển bản xem trước để duyệt, chỉ xuất bản sau hành động duyệt xác thực.

## Mẫu job để sao chép vào pipeline

```json
{
  "language": "vi",
  "platforms": ["youtube_shorts", "tiktok", "facebook_reels"],
  "aspect_ratio": "9:16",
  "resolution": "1080x1920",
  "fps": 30,
  "duration_sec": 30,
  "topic": "CHU_DE",
  "voice": "licensed_voice_or_user_asset",
  "asset_policy": "original_or_verified_commercial_license",
  "publication_approval": "required",
  "auto_publish": false
}
```

Job mẫu là hợp đồng nội bộ gợi ý, KHÔNG phải schema API được xác minh của MoneyPrinterTurbo. Khi triển khai API thật phải đọc swagger/openapi và kiểm tra các endpoint/fields trước.

## An toàn và tách biệt

- Tạo thư mục `C:\AI-VIDEO\moneyprinter` hoặc `C:\AI-VIDEO\moneyprinterturbo` chỉ khi đường dẫn cho phép, không ghi đè.
- LLM tạo script không tự cấp quyền dùng nhạc, hình, footage. Kiểm tra giấy phép thương mại từng tài nguyên; không lấy logo/nhạc có bảo hộ ngoài phạm vi cho phép.
- Không thu thập mật khẩu/cookies/tokens trong chat, không tự cung cấp quyền publish, không tạo nguồn cảnh trích từ thương hiệu không được phép.
- Chỉ báo thành công `mp4` sau khi file tồn tại, ffprobe xác nhận kích thước/độ dài/FPS và nghe xem kiểm tra âm thanh.
