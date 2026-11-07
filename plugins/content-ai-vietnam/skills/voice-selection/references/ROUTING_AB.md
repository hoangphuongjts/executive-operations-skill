# Chọn engine và thử A/B — 04/11/2026

Đây là cấu hình tích hợp workflow, không phải sáu engine đã chạy trong ChatGPT. Adapter free_voiceover.py hiện thực thi VieNeu/VoxCPM; bốn repo bổ sung dùng runtime và ví dụ upstream bên dưới. Chỉ báo runtime_ready sau doctor và một lần inference thật của engine đó. Không gọi tên engine chưa được adapter hỗ trợ bằng CLI free_voiceover.py.

## Routing
- Tò Mò Lab: ưu tiên preset vidIQ `Adam - Dominant, Firm` đã dùng trước đây (ID `pNInz6obpgDQGcFmaJgB`), nếu catalog còn liệt kê và quota khả dụng; đọc cấu hình `free-voiceover/references/TO_MO_LAB_ADAM.md`. Đây là preset vidIQ, không phải clone và không đồng nhất với preset Adam của VieNeu.
- Tiếng Việt / máy CPU: VieNeu trước; VoxCPM khi muốn giọng mới hoặc đã có phần cứng phù hợp. Chatterbox Multilingual là ứng viên thử thêm, không coi hỗ trợ ngôn ngữ là bằng chứng đọc chuẩn.
- Tiếng Anh: so Qwen3-TTS Base/VoiceDesign phù hợp mục tiêu với Chatterbox/VoxCPM. Qwen3-TTS chưa công bố tiếng Việt trong 10 ngôn ngữ, không route vi vào bản gốc.
- Đã có bản đọc đúng, muốn chuyển màu giọng: OpenVoice V2; cần source audio, source speaker embedding và target reference có quyền. Chất lượng tiếng Việt phụ thuộc base TTS và thử nghiệm; không coi conversion là tự tạo phát âm đúng.
- F5-TTS: code MIT khác weights CC-BY-NC. Video kiếm tiền loại official pretrained khỏi shortlist. Model fine-tune khác chỉ được vào khi xác minh quyền toàn chuỗi weights/data; không tự cho rằng đổi fine-tune là hết ràng buộc.
- Không thay giọng Adam cũ chỉ vì trùng tên preset. Giữ lựa chọn giọng đã được duyệt; so sánh giọng khác là đề xuất để người dùng chọn, không tự đổi identity.
- Adam Tò Mò Lab: chỉ route đến vidIQ khi catalog trả đúng `Adam - Dominant, Firm` / ID `pNInz6obpgDQGcFmaJgB`. Runway/HeyGen/Higgsfield có voice khác tên Adam nhưng không cùng ID; model local không nhập được preset provider này. Nếu người dùng chỉ định tool không hỗ trợ exact ID, dừng và trình bày lựa chọn khác để họ duyệt.
- Mỗi tác vụ chọn 1 engine, hoặc 2 ứng viên khi thực sự cần A/B; không chạy cả sáu mặc định. Khi yêu cầu hiện tại đã cho phép tạo/so sánh thì tiếp tục trong phạm vi đó; chỉ hỏi thêm nếu thiếu quyền giọng hoặc chi phí mới.

## Tích hợp bốn runtime bổ sung
Cài mỗi repo vào môi trường riêng, pin commit/package + model revision, lưu giấy phép và phiên bản vào manifest của lần chạy. Không cài chồng vào venv VieNeu, không chạy installer từ fork. Các liên kết sau là API/ví dụ chính thức cần đọc phiên bản thực tế trước chạy:
- Chatterbox: https://github.com/resemble-ai/chatterbox — dùng Multilingual cho tiếng Việt, bản English/Turbo/Nano theo ngôn ngữ công bố. Ví dụ chính thức trong README và multilingual_app.py, truyền file reference theo API của bản đã pin; giữ watermark mặc định, không gỡ nhận diện tổng hợp.
- OpenVoice V2: https://github.com/myshell-ai/OpenVoice/blob/main/demo_part2.ipynb — cấu hình checkpoint converter, source embedding của base TTS và target embedding từ reference. Chỉ chuyển màu giọng khi cả base và target có quyền; không lấy embedding nguồn không tương ứng. Output WAV rồi đối chiếu transcript.
- Qwen3-TTS: https://github.com/QwenLM/Qwen3-TTS — Base dùng voice clone, VoiceDesign dùng giọng mô tả, CustomVoice dùng preset theo docs. Không lẫn checkpoint các chế độ. Xem mục Voice Clone và generate_voice_clone của SDK qwen-tts; ref transcript đúng hoặc chế độ x-vector theo API thực tế.
- F5-TTS: https://github.com/SWivid/F5-TTS/blob/main/src/f5_tts/api.py — dùng F5TTS/infer theo signature phiên bản đã pin, reference audio và transcript chính xác; weights official chỉ thử phi thương mại. Không dùng demo public cho file riêng nếu chưa được phép gửi.

Các model cần tải, RAM/VRAM, thời gian chạy và phụ thuộc riêng. Miễn phần mềm không đồng nghĩa miễn hosting/GPU. Chưa cài/kiểm thử suy luận bốn runtime trong bản nâng cấp này.

## A/B cùng điều kiện
1. Cùng văn bản UTF-8, ngôn ngữ, cùng reference được phép nếu so clone; khác reference hoặc thiết kế giọng mới phải ghi rõ không phải so mức giống cùng người nói. Cùng cách đọc thuật ngữ/số và tốc độ mục tiêu tự nhiên. Không ép time-stretch.
2. Lưu WAV gốc. Tạo bản nghe so sánh có loudness tương đương bằng FFmpeg loudnorm, không ghi đè gốc và không suy ra chất lượng từ độ lớn. Với script voice_select.py dùng bản PCM16 không đổi tốc độ; đồng thời giữ log clipping của bản gốc vì normalize có thể che dấu clipping.
3. Gán A/B không lộ tên engine khi nghe. Nghe hết, so script để đánh dấu bỏ/thêm/lặp/sai từ, tên riêng, dấu tiếng Việt. ASR chỉ hỗ trợ, không là sự thật tuyệt đối. Ghi reviewer và thời gian thực tế. Không có khả năng nghe thì abstain, không tự bịa điểm.
4. Điểm 1–5 do người nghe cung cấp: đúng nội dung 35%, tự nhiên 25%, đúng identity/phù hợp giọng thương hiệu 20%, ngữ điệu 15%, sạch tạp âm 5%. Cột identity phải ghi tiêu chí (clone similarity hay brand fit); không so lẫn hai tiêu chí. Đây là rubric nội bộ, không phải MOS được kiểm định.
5. Chặn file sai script, thiếu quyền, sai trọng yếu hoặc clipping đáng kể. Không có reviewer/điểm đầy đủ thì chưa chọn. Hai bản chênh dưới 2/100 trả tie; khi đủ điều kiện script gợi ý file điểm cao hơn, không tự ghi đã được người dùng duyệt.
6. Chỉ ghép vào video file được chọn/phê duyệt theo ủy quyền hiện có. ASR/alignment theo audio cuối. Giữ bản khác để rollback trong phạm vi lưu trữ người dùng, không đăng tự động.

## Dùng công cụ so tệp
```
python scripts/voice_select.py candidates.json --output comparison.json
```
Manifest mẫu trong references/candidates.example.json. Điền script_sha256 từ chính kịch bản, file, quyền, is_clone/consent, reviewer, full_listen, critical_errors và 5 điểm thật. Dùng đường dẫn file tương đối với manifest. Công cụ chỉ nhận WAV PCM16; nhiều tệp khác cần chuyển bằng FFmpeg. Đo duration/rate/channels/RMS/sample-peak/near-full-scale; không tính SNR hoặc true peak, không đo tự nhiên/đúng giọng. Một engine ghi âm 48kHz không tự tốt hơn 24kHz. Ngưỡng gần im lặng/clipping là heuristic.

## Kiểm chứng
5 unit tests selection dùng tín hiệu tổng hợp để kiểm tra logic (không phải mẫu TTS): thiếu nghe → abstain; clipping → loại; sai script → loại; clone thiếu đồng ý → loại; hòa → abstain. Không suy ra chất lượng engine từ các test này. 5 test adapter VieNeu/VoxCPM trước vẫn giữ nguyên. Trạng thái: registry/workflow/scripts packaged và offline-tested; cả sáu engine chưa có kiểm chứng end-to-end tại máy người dùng.
