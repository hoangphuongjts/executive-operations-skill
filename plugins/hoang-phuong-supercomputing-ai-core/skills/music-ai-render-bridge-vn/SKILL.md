---
name: music-ai-render-bridge-vn
description: "Định tuyến tạo nhạc/giọng hát MP3 qua nhà cung cấp được cấp quyền, kiểm soát credit và prompt; Runway generate_music nếu kết nối, Suno/Udio nếu có quyền chính thức; Cụm 13, phối hợp Cụm 08."
---
# AI Music Render Bridge — Cụm 13 Nội dung & đa phương thức

## Chọn công cụ theo bằng chứng phiên hiện tại
| Provider | Chức năng | Kết nối/chứng cứ | Chính sách |
|---|---|---|---|
| ChatGPT | sáng tác lời, nhạc lý, prompt, phân tích | nội tại | không coi văn bản là file MP3 |
| Runway `generate_music` | tạo bài hát, nhạc không lời, jingles và xuất MP3 | công cụ có thể xuất hiện trong phiên; kiểm tra lại trước mỗi lần gọi | `lyria-3-pro`: 8 credits; `lyria-3-clip`: 4 credits tại thời điểm kiểm tra 2026-11-07; có thể thay đổi; phải xin phê duyệt số credit trước khi gọi |
| Suno | bài hát AI | CHƯA xác minh plugin API chính thức trong phiên kiểm tra | chỉ chuẩn bị prompt/chuyển tay; không tự giả lập API, không thu thập cookie/token |
| Udio | bài hát AI | CHƯA xác minh plugin API chính thức trong phiên kiểm tra | tương tự Suno |
| MuseScore | đọc/hiệu chỉnh MusicXML | cần người dùng cài ứng dụng phù hợp ở ngoài host | có thể xuất MusicXML offline, không tự xác nhận ứng dụng đang cài |
| DAW / FFmpeg / Audacity | biên tập, phối, kết xuất tùy quyền host | engine ngoài; kiểm tra có thực thi được trước khi báo kết quả | không cài/xoá/sửa hệ thống tự động |

## Flow an toàn, kiểm soát chi phí
1. Nhận bản sáng tác gốc hoặc yêu cầu. Chuẩn hóa `song_spec`: genre, mood, bpm, vocals, languages, instrumentation, story, original_lyrics, reference_constraints.
2. Nếu cần bản demo không tốn credit: viết prompt hoàn chỉnh + xuất MIDI/MusicXML nếu có dữ liệu cao độ và trường độ, hoặc cung cấp lyric sheet.
3. Nếu người dùng muốn MP3, kiểm tra Runway có mặt và yêu cầu người dùng phê duyệt số credit cụ thể; KHÔNG gọi nhà cung cấp chỉ dựa trên câu "viết nhạc" hoặc "tích hợp bộ công cụ".
4. Nếu host không có backend, báo `requires_connection`/`blocked` và bàn giao prompt có thể copy sang công cụ bên ngoài. Không giả vờ file đã render.
5. Sau khi backend chạy thật, đối chiếu kết quả theo task ID, định dạng, độ dài, mức tiêu credit, metadata; không đưa private URL/token vào báo cáo công khai.
6. Không nhân bản giọng của người thật hoặc giả danh nghệ sĩ khi thiếu sự cho phép; không dùng lời, bản ghi, mẫu âm thanh chưa có quyền.

## Chuẩn prompt Runway
"Original Vietnamese [genre] song, [bpm] BPM, [time signature], [mood], [instrumentation], [male/female neutral vocal descriptors], original lyrics: [lyrics], structure [intro verse chorus bridge outro], clean mix with clear Vietnamese diction, no imitation of real artists or existing melodies."

## Báo trạng thái
`draft_only` / `prompt_ready` / `provider_connected` / `render_confirmed` / `requires_credit_approval` / `blocked`. Adapter instruction không cấp quyền API và không thay thế cài đặt nhà cung cấp.
