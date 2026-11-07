# Khả năng dùng cùng giọng Adam trên các công cụ

**Danh tính chuẩn:** vidIQ public voice `Adam - Dominant, Firm`, ID `pNInz6obpgDQGcFmaJgB`. Giữ ID này làm nguồn sự thật; không khớp giọng chỉ bằng tên “Adam”.

## Kết quả kiểm tra catalog — 04/11/2026

| Công cụ | Kết quả | Cách xử lý |
|---|---|---|
| vidIQ Voiceover | Có đúng tên và ID trên trong catalog | Dùng ID trả về từ `vidiq_voiceover_list_voices`; kiểm tra quota trước mỗi job. |
| Runway | Tìm đúng ID không có kết quả. Có nhiều voice tên Adam nhưng ID, mô tả và ngôn ngữ khác | Không gán các voice Adam của Runway là giọng Tò Mò Lab; chỉ dùng khi người dùng chọn một voice khác. |
| HeyGen | Có một số voice tên Adam bằng tiếng Anh, ID riêng; truy vấn Adam tiếng Việt không có kết quả | Không coi là cùng Adam và không route tiếng Việt sang voice tiếng Anh. |
| Higgsfield | Không thấy Adam trong 114 preset đã đọc | Không tạo voice element hay clone từ preview của vidIQ. |
| VieNeu, VoxCPM2, Chatterbox, OpenVoice, Qwen3-TTS, F5-TTS | Mỗi engine có catalog/reference và ID riêng; không nhận dạng vidIQ ID như cùng voice | Không gọi preset Adam tương đồng hoặc clone. Dùng chỉ khi người dùng chấp thuận một voice khác và runtime/rights đã sẵn sàng. |

Catalog có thể thay đổi; kiểm tra lại trước khi dùng. Kết quả trên xác nhận khả năng ánh xạ ở thời điểm kiểm tra, không phải so sánh nghe A/B. Voice Adam cùng tên ở một dịch vụ khác không chứng minh cùng người nói, cùng âm sắc hoặc cùng quyền sử dụng.

## Quy tắc routing

1. Brief Tò Mò Lab yêu cầu Adam → ưu tiên vidIQ đúng ID. Kiểm tra catalog, quota, quyền nội dung và độ dài script trước khi synthesize.
2. Người dùng chỉ định công cụ khác → tìm exact voice ID trong catalog của chính công cụ đó. Nếu không có, báo “chưa hỗ trợ đúng Adam”; không tự chọn một voice trùng tên.
3. Nếu user muốn dùng voice khác tương tự trên một công cụ → đưa tên, ID, ngôn ngữ và preview để user duyệt trước khi đổi. Không gọi synthesize thử vì mỗi tool có quota/credits riêng.
4. Không tải preview/public sample của voice Adam từ vidIQ sang công cụ clone hoặc voice-conversion. Chỉ clone voice do user sở hữu/được ủy quyền bằng reference hợp lệ và có đồng ý rõ; việc voice hiện trong catalog không cấp quyền clone.
5. Giữ stem Adam và version trong manifest video. Nếu exact provider không có quota hoặc không kết nối, để audio chờ thay vì thay identity.
