---
name: moneyprinter-local-vn
description: Dùng khi người dùng muốn hiểu, so sánh, cài hoặc vận hành repository FujiwaraChoki/MoneyPrinter chạy Ollama cục bộ, Python/uv, Docker/Postgres, worker và frontend; hỗ trợ tiếng Việt.
---

# MoneyPrinter Local — Hướng dẫn tiếng Việt

Nguồn: https://github.com/FujiwaraChoki/MoneyPrinter. Giấy phép MIT; giữ nguyên thông báo bản quyền khi sao chép/mở rộng mã. Repo chính này KHÁC MoneyPrinterTurbo của harry0703.

## Khả năng chính

Từ chủ đề tạo YouTube Shorts, Ollama xử lý kịch bản và metadata. Phiên bản hiện tại dùng hàng đợi có API + worker + Postgres khi chạy Docker. Không suy diễn rằng ChatGPT plugin này có quyền điều khiển Ollama hoặc Windows.

## Cài đặt riêng khi người dùng thực sự yêu cầu chạy trên máy (cần terminal được cấp quyền)

- Repo gốc: `git clone https://github.com/FujiwaraChoki/MoneyPrinter.git` vào thư mục con mới, tránh ghi đè dữ liệu.
- Cần Python 3.11+, uv, FFmpeg, ImageMagick, Ollama; Docker/Postgres nếu chọn Docker Compose.
- Đọc `docs/quickstart.md`, `docs/docker.md`, `docs/configuration.md`, `docs/testing.md` và scripts trước khi chạy.
- Lệnh chỉ để tham khảo sau khi đã kiểm tra và phê duyệt: `uv sync`, `uv run pytest`, `uv run python Backend/main.py`, `uv run python Backend/worker.py`. Frontend có thể dùng port 3000 khi chạy riêng. Docker Compose dùng backend/API/worker/DB; không tự triển khai/cấp cổng công khai.
- Không cài trực tiếp repo Python/Docker vào ChatGPT cloud bằng cách chỉ thêm Skill: phải có runtime và MCP server có endpoint đã xác minh mới được gọi hành động từ ChatGPT.

## Bảo mật và nội dung

- Không yêu cầu người dùng dán `TIKTOK_SESSION_ID` hoặc cookie đăng nhập vào chat. Nếu dùng, nhập trực tiếp trong ứng dụng/môi trường bí mật của người dùng; ưu tiên API chính thức và không tự đăng.
- Không tự kéo model Ollama nặng hoặc thực thi mã chưa rà soát, không xóa/thay đổi các module HyperFrames/Herk/ShotCraft/Gemini đang có.
- Không đăng video tự động. Phải có phê duyệt sau khi xem bản cuối và quyền sử dụng video, hình ảnh, nhạc, giọng và logo.
- Đối với nguồn web, phải xác minh bản quyền thương mại và điều khoản các dịch vụ, không tin giả định mọi video stock đều tự do dùng.

## Cách phục vụ trong ChatGPT

Chuẩn hóa brief tiếng Việt (chủ đề, khán giả, tỉ lệ, thời lượng, CTA), kịch bản, shotlist và checklist triển khai. Nếu có công cụ máy tính/runtime đủ quyền, kiểm tra trạng thái trước, yêu cầu xác nhận cài đặt rủi ro/chi phí, kiểm thử trả kết quả thực tế. Không tuyên bố đã tạo MP4 nếu chỉ có mã hoặc storyboard.
