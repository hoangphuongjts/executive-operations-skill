---
name: voice-selection
description: "Dùng khi cần chọn giữa VieNeu, VoxCPM2, Chatterbox, OpenVoice V2, Qwen3-TTS, F5-TTS hoặc so sánh file giọng đọc A/B để chọn bản phù hợp."
---
# Chọn và so sánh giọng đọc
Đọc [routing và A/B](references/ROUTING_AB.md); tra [registry](references/providers.json). Chọn theo ngôn ngữ, giấy phép, quyền người nói, phần cứng, chất lượng thực tế. Chỉ gọi engine có runtime thật; tên repo không phải MCP tool. Chỉ adapter VieNeu/VoxCPM có sẵn trong free-voiceover, bốn engine khác đi theo guide upstream.

Với video Tò Mò Lab, mặc định ưu tiên Adam - Dominant, Firm trong VidIQ (voice ID đã dùng: `pNInz6obpgDQGcFmaJgB`); đọc [cấu hình giọng Adam](../free-voiceover/references/TO_MO_LAB_ADAM.md), xác minh catalog/quota trước khi tạo. Không thay bằng preset Adam của VieNeu hoặc giọng khác.

Với Tò Mò Lab, dùng [bảng tương thích Adam](../free-voiceover/references/ADAM_PORTABILITY.md): chỉ vidIQ đang xác nhận exact voice ID `pNInz6obpgDQGcFmaJgB`; không tự ánh xạ sang voice trùng tên trên Runway, HeyGen, Higgsfield hoặc model local.

Với video thương mại, loại F5 official pretrained; khi chưa xác minh weights/preset không tự coi code license là đủ. Giữ giọng đã duyệt. Không dùng tên Adam để nhận đồng nhất hai giọng khác nhau.

Khi so tệp, dùng script voice_select.py để đo tệp và tổng hợp đánh giá người nghe; mọi điểm cảm nhận cần nghe thật, không bịa. Thiếu nghe hoặc chứng cứ thì báo chưa chọn. Đầu ra: bảng từng file/engine/version/quyền/metric/lỗi phát âm/điểm nghe/lý do chọn hoặc abstain. Cùng script và điều kiện so sánh, không mặc định bitrate/sample rate cao là hay hơn. Không chọn file gây lỗi khoa học chỉ vì giọng hay.

Với tác vụ A/B đã được giao, tạo tối đa hai ứng viên ban đầu khi runtime và quyền sẵn sàng; cho phép mở rộng có lý do trong ngân sách, không hỏi lại những quyền đã cấp. Sau chọn, chuyển file thật sang phụ đề/alignment và dựng. Báo rõ đã cấu hình/đã chạy test/đã tạo audio/đã nghe; không dùng các trạng thái thay nhau.
