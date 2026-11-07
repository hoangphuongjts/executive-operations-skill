# Thiết lập local — kiểm tra 04/11/2026

## Giọng thương hiệu Tò Mò Lab (vidIQ)
Mặc định Adam - Dominant, Firm, voice ID `pNInz6obpgDQGcFmaJgB` đã dùng trước đây; đây là preset tổng hợp của vidIQ, không phải giọng clone. Trước mỗi job, gọi `vidiq_voiceover_list_voices` để xác nhận tên/ID và kiểm tra quota; chỉ gửi một script đã chốt qua `vidiq_voiceover_generate`, rồi poll job và kiểm tra WAV/MP3 thật. Nếu quota hết hoặc tool không kết nối, dừng tại trạng thái chờ; không retry, chi dịch vụ khác hay tự đổi sang Adam VieNeu. Quyền thương mại cần xác minh theo điều khoản nhà cung cấp hiện hành.

## Nguồn chính quy
- VieNeu: https://github.com/pnnbao97/VieNeu-TTS/tree/04044e1b8f822f946bafb2c88b716459f4164152
- Model card và quyền preset: https://huggingface.co/pnnbao-ump/VieNeu-TTS-v3-Turbo (Apache-2.0; FAQ xác nhận quyền preset thương mại theo nhà phát hành). Card và README có danh sách preset khác nhau; `list_preset_voices()` của SDK đã cài là nguồn thực tế.
- VoxCPM: https://github.com/OpenBMB/VoxCPM/tree/cce58a5b59303c9bd63d12f23afe6a49a4a80c59 (Apache-2.0 code/weights theo repo, hỗ trợ tiếng Việt).
- Không chọn XTTS-v2 mặc định cho video kiếm tiền: https://huggingface.co/coqui/XTTS-v2/blob/v2.0.3/LICENSE.txt có giới hạn phi thương mại.

Miễn phí phần mềm/model không đồng nghĩa miễn tiền điện, GPU, lưu trữ hay hosting. VieNeu v4 dịch vụ proprietary không thuộc tuyến miễn phí v3 này. Chỉ đóng gói adapter mới viết, không đóng gói engine, weights hoặc preset; giữ notices khi phân phối lại thành phần bên thứ ba.

## Windows — chạy trên máy người dùng, không phải máy ChatGPT
Tạo môi trường riêng (Python 3.11 được khuyến nghị để tương thích):
```
py -3.11 -m venv .venv
.venv\Scripts\python.exe -m pip install vieneu==3.7.1
.venv\Scripts\python.exe scripts/free_voiceover.py --doctor
```
Sau khi kiểm tra gói đã cài và cho phép tải model, dùng preset đã chọn và thực sự có trong SDK:
```
.venv\Scripts\python.exe scripts/free_voiceover.py --engine vieneu --text script.txt --output narration.wav --voice "Mai Anh" --allow-model-download
```
Ví dụ preset không phải mặc định chọn giọng thay người dùng. Clone chỉ khi đồng ý thực sự đã được ghi nhận cho file tham chiếu:
```
.venv\Scripts\python.exe scripts/free_voiceover.py --engine vieneu --text script.txt --output clone.wav --reference my_voice.wav --consent --allow-model-download
```
VoxCPM2 dùng môi trường riêng Python 3.10–3.12, cài PyTorch phù hợp phần cứng theo docs chính thức rồi cài voxcpm và soundfile. Kiểm tra bản SDK hiện tại trước chạy; adapter API được đối chiếu commit repo ở trên, chưa pin wheel VoxCPM. Không tự mở server public.
```
python scripts/free_voiceover.py --engine voxcpm --text script.txt --output narration.wav --allow-model-download
```
Clone VoxCPM thêm --reference và --consent. Kiểm tra quyền sử dụng trước tạo. Nội dung file tiếng Việt phải UTF-8. Trước download weights kiểm tra model card/phiên bản và dung lượng, không chạy mã từ fork không rõ.

## Handoff video
Tạo narration.wav + narration.wav.json → nghe kiểm tra phát âm/thuật ngữ → ASR/alignment → SRT → mix nhạc → render MP4 → đo/giải mã/nghe duyệt. Lưu file trong thư mục dự án, giữ bản chưa có giọng là nháp. Không gọi phụ đề theo cảnh là phụ đề đồng bộ lời nói.

## Bằng chứng kiểm thử
Adapter đã qua 5 kiểm thử offline: từ chối clone chưa có đồng ý, từ chối chạy chưa cho phép tải model, bảo vệ file đầu ra, kịch bản hợp lệ, phát hiện preset sai engine. Doctor hiện chưa thấy vieneu/voxcpm/soundfile. CHƯA kiểm thử suy luận, chất lượng tiếng Việt/clone, latency, GPU, Windows hay end-to-end video. Khi dependency/API thay đổi phải kiểm tra lại; không lấy mock/unit test làm bằng chứng engine hoạt động.
