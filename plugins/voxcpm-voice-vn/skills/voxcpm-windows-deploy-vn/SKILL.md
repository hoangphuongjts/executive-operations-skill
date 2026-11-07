---
name: voxcpm-windows-deploy-vn
description: Dùng khi người dùng muốn cài và chạy VoxCPM2 thật trên Windows, kiểm tra GPU/Python/CUDA, tích hợp đầu ra WAV với HyperFrames, Herk Edit Kit, Video ShotCraft, Gemini CLI hoặc ChatGPT qua backend có xác thực.
---

# VoxCPM2 — Triển khai Windows và ghép AUDIO AI

## Nguyên tắc
VoxCPM2 không chạy trong plugin kỹ năng ChatGPT này. Muốn tạo WAV cần cài mô hình vào Windows có Python và đủ tài nguyên, hoặc kết nối tới backend TTS có xác thực. Không mặc định mở local HTTP ra Internet hay tạo tunnel công khai. Không để lộ API key, giọng mẫu và dữ liệu cá nhân. Giữ module độc lập với các module VIDEO AI khác.

## Môi trường mục tiêu
- Thư mục riêng: `C:\AI-VIDEO\voxcpm2` (không ghi đè).
- Node.js 26/FFmpeg/Chrome đã có trong hệ thống VIDEO AI theo báo cáo trước đây, nhưng **VoxCPM cần Python** riêng.
- Ưu tiên Python 3.11 (repo yêu cầu >=3.10,<3.13), môi trường ảo riêng, kiểm tra card NVIDIA/driver CUDA, RAM/VRAM, trống đĩa trước khi tải weights; model VoxCPM2 2B có thể cần tài nguyên GPU đáng kể, đường CPU có thể rất chậm.
- Repo chính thức https://github.com/OpenBMB/VoxCPM ; tài liệu chính thức https://voxcpm.readthedocs.io/en/latest/quickstart.html

## Lệnh khởi tạo tham khảo (chỉ chạy trong terminal được cấp quyền)
```powershell
$base = 'C:\AI-VIDEO\voxcpm2'
if (Test-Path "$base\.venv") { throw 'Da co .venv, khong ghi de tu dong.' }
New-Item -ItemType Directory -Force -Path $base | Out-Null
py -3.11 -m venv "$base\.venv"
& "$base\.venv\Scripts\python.exe" -m pip install --upgrade pip
& "$base\.venv\Scripts\python.exe" -m pip install voxcpm
& "$base\.venv\Scripts\voxcpm.exe" --help
```
`pip install voxcpm` có thể kéo nhiều package và trọng số sẽ được tải ở lần chạy đầu: cần kiểm tra dung lượng/nguồn/điều khoản trước. Chạy thử lệnh synth (không clone giọng khác):
```powershell
& 'C:\AI-VIDEO\voxcpm2\.venv\Scripts\voxcpm.exe' design --text 'Xin chào, đây là giọng AI thử nghiệm.' --output 'C:\AI-VIDEO\voxcpm2\demo.wav'
```
Kiểm tra WAV bằng `ffprobe`. Thiếu GPU thì không báo thành công giả; kiểm tra phương án CPU hoặc dùng máy chủ của chính người dùng sau khi xác minh quyền.

## ChatGPT API/MCP
Cài package Python cục bộ KHÔNG cài model vào ChatGPT. Để gọi trực tiếp từ ChatGPT cần máy chủ suy luận VoxCPM2 thật có API/MCP HTTPS bảo mật, quyền tải và sử dụng giọng mẫu, giới hạn kích thước audio, rate limit, auth, che log nhạy cảm, giám sát phí, xác nhận gửi dữ liệu ra ngoài. Chỉ thêm `mcp.json` khi endpoint được cung cấp và kiểm chứng; không bịa endpoint hoặc tự mở port 8808.

## Chuỗi VIDEO AI
AI Agent xây script -> VoxCPM2 sinh WAV đã kiểm tra -> FFmpeg căn chỉnh âm thanh -> HyperFrames/ShotCraft/Herk render MP4 -> duyệt thủ công -> đăng sau phê duyệt. Giữ thư mục output và project riêng, không làm hỏng Remotion/Node packages hiện có.
