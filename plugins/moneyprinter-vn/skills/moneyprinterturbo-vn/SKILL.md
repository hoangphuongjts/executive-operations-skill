---
name: moneyprinterturbo-vn
description: Dùng khi cần chuẩn bị, cài đặt, cấu hình, khắc phục lỗi hoặc lập kịch bản vận hành MoneyPrinterTurbo của harry0703 cho video ngắn 9:16 tiếng Việt qua WebUI/API/CLI hay AI Agent.
---

# MoneyPrinterTurbo — Hướng dẫn tiếng Việt

Nguồn chính thức: https://github.com/harry0703/MoneyPrinterTurbo; license MIT. Skill gốc của dự án: https://github.com/harry0703/MoneyPrinterTurbo/blob/main/docs/skill/SKILL.md. Đây là bản hướng dẫn Việt hóa độc lập, KHÔNG cung cấp CLI/backend trong ChatGPT.

## Năng lực từ dự án

MoneyPrinterTurbo có thể tạo script, chọn/tạo hình, thoại, phụ đề, nhạc và xuất MP4 qua WebUI/API/CLI. Có nhà cung cấp LLM Gemini, OpenAI v.v., tiếng Việt tùy chọn; đừng sử dụng mặc định tiếng Trung của Skill upstream. Tùy dịch vụ, cần API keys, credits, công cụ và giấy phép riêng.

## Triển khai riêng trên Windows (chỉ khi được người dùng giao quyền thực thi)

Cách chính thức đơn giản nhất: https://github.com/harry0703/MoneyPrinterTurbo/releases/latest, chọn file `.7z` đóng gói Windows (không nhầm Source code ZIP), kiểm tra scripts trước khi chạy `start.bat`; không tự chạy update và thay mã khi chưa phê duyệt.

Cách cài Python 3.11+: tạo môi trường ảo tách biệt, `python -m pip install mpt`, sau đó `mpt webui`; dữ liệu mặc định dưới `%LOCALAPPDATA%\MoneyPrinterTurbo`, có thể chọn root khác bằng `MPT_HOME`. Dùng riêng thư mục bên cạnh `C:\AI-VIDEO` chứ không đè lên HyperFrames, Herk, ShotCraft hoặc Gemini. Trên Windows PowerShell nếu chặn `.ps1`, có thể sử dụng cmd.exe/launcher hợp lệ, không tắt chính sách bảo mật toàn hệ thống.

AI Agent skill upstream kèm `mpt_agent.py` cần môi trường terminal, network, filesystem và long-running process; một plugin chỉ lưu SKILL.md không tạo được những quyền đó. Nếu chạy trong môi trường đủ quyền, tham khảo và kiểm duyệt code helper trước khi thực thi. Không chạy mã tải từ mạng theo cách `irm | iex` mà không rà soát.

## Preset tiếng Việt cho hệ thống VIDEO AI

- Vertical 9:16, 1080 × 1920, 30fps; mặc định 30 giây trừ khi yêu cầu khác.
- Kịch bản gốc tiếng Việt, nguồn kiểm chứng được; không bịa tính năng sản phẩm.
- Lồng giọng Adam nếu có bản thu/licence được cung cấp hoặc có quyền tạo; nếu không có, hỏi nguồn giọng hoặc đề xuất giọng hợp pháp tương đương (không tự khẳng định giọng Adam đã tạo).
- Phụ đề đồng bộ chính xác lời đọc; nhạc nhỏ; cảnh có bối cảnh Việt Nam khi phù hợp.
- Luồng xuất: brief → script → kiểm nguồn/license → tài nguyên → voice/subtitle → render → ffprobe → bản xem trước → duyệt → (chỉ đăng sau duyệt).
- Khi dùng ảnh thương hiệu/sản phẩm thật, xác minh quyền quảng cáo; không đăng tự động.
- Nếu nhà cung cấp phát sinh phí, báo chi phí và xin chấp thuận trước.

## Kết nối ChatGPT đúng sự thật

Hỗ trợ viết brief, cấu hình/mẫu payload API, kế hoạch chạy và khắc phục lỗi. Không thể gọi máy Windows hoặc render bằng plugin skills-only khi chưa có runtime/MCP tương ứng. Nếu người dùng cần tạo MP4, kiểm tra các tool hiện có và không tự giả định API đang kết nối.
