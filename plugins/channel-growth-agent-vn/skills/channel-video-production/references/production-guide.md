# Quy trình sản xuất video nhiều cảnh và xuất MP4

## A. Hai định dạng
- Short: 45–90 giây; 9:16; 1080×1920 nếu nhà cung cấp/tài khoản hỗ trợ; lời mở đầu thu hút trong 2 giây, giải thích có bằng chứng, CTA.
- Long-form: ưu tiên 3–15 phút; 16:9; Full HD 1920×1080 nếu nhà cung cấp/tài khoản hỗ trợ; 5–30+ cảnh tùy nhịp; hook, lời hứa, các chương nhỏ, chứng cứ, tổng kết. Không tự bịa dữ liệu. Dài hơn thì phân đoạn hợp lý, không bảo đảm giới hạn dịch vụ.

## B. Phân tuyến backend có thật
- HeyGen `create_video_from_studio`: ghép theo thứ tự 1–50 cảnh toàn khung `avatar_video`, `image`, `video`. Ảnh im lặng có `duration`; ảnh hoặc clip có narration dùng chính xác một trong `script+voice_id`, `audio_url` hoặc `audio_asset_id`; khi narration hiện diện, cảnh theo thời lượng audio. Clip video có thể giữ/điều chỉnh playback khi backend hỗ trợ. Input media phải là URL https công khai hoặc asset ID của HeyGen, không dùng đường dẫn local. `aspectRatio`: `9:16`/`16:9`; `resolution` `720p`/`1080p` theo gói; `caption:{file_format:"srt",style:"default"}` để có SRT và phụ đề burn-in. Sau khi tạo video_id, dùng `show_video` một lần, giao diện tự theo dõi. Tra `get_video` nếu user yêu cầu kiểm tra; chỉ dùng status thật.
- HeyGen Video Agent `video_agent_generate`: phù hợp video có giọng dẫn và hình minh họa, thời lượng >15s, đề bài mở và không bắt buộc lời đọc đúng từng chữ. Mô tả rõ 3D giáo dục hoặc phong cách cần thiết, không hứa tuân thủ chính xác.
- Runway/Higgsfield: có thể tạo clip minh họa động nhiều cảnh và âm thanh từ nguồn hợp lệ; cần xem thời lượng clip, giới hạn và cost trước khi sinh, không giả định clip đơn là video dài. Sau đó ghép trong công cụ có hỗ trợ hoặc trong môi trường render.
- Local/Work: dùng FFmpeg/ffprobe, Remotion hoặc NLE có thật khi được cấp quyền. Gộp `video`, `audio` (voiceover và nhạc nền) với mix/ducking; phụ đề burn-in từ SRT đồng bộ audio; xuất H.264/AAC MP4 + SRT + thumbnail nếu phù hợp. Nếu không có môi trường thực thi, chỉ cung cấp gói dự án/sản xuất có thể chạy, ghi rõ chưa render.

## C. Giọng Adam
Chỉ sử dụng nếu có voice_id đúng được cấp quyền hoặc bản audio người dùng sở hữu/có quyền thương mại. Một file MP3 29 giây không cho phép tạo giọng đọc 15 phút bằng cách ghép tùy ý, và không đủ đồng ý để clone voice người khác. Chỉ dùng voice clone khi có đầy đủ quyền/đồng ý; nếu chưa có, báo hạn chế và chọn giọng được cấp phép sau xác nhận. Kiểm tra audio cuối cùng nghe được.

## D. Âm thanh, phụ đề, bản quyền
Tạo nhạc gốc hoặc dùng bản được phép, giữ bảng chứng cứ giấy phép cho từng nguồn. Nhạc nền nhỏ so với lời thoại, duck khi có voice. Phụ đề khớp nội dung và timestamp của audio thật. Màu/hiệu ứng tuân thủ thương hiệu Tò Mò Lab, cảnh khoa học chính xác, không lặp footage vô lý.
HeyGen Studio có SRT và burn-in kiểu mặc định nhưng không hứa tự trộn nhạc nền nhiều lớp hoặc hiệu ứng phụ đề động theo lời nếu công cụ không có tham số đó. Với yêu cầu nâng cao, xuất qua hậu kỳ có runtime phù hợp.

## E. Chi phí, kiểm thử, bàn giao
Trước mỗi lượt sinh có chi phí: xác minh ước tính hoặc yêu cầu người dùng chấp thuận. Không tự đăng. Bàn giao gồm link MP4 đã hoàn thành, bản SRT và thumbnail nếu có, metadata 6 nền tảng, checklist và bảng nguồn. Lưu Google Drive đúng dự án khi có quyền. Trạng thái "đã lên kế hoạch / đã có tư liệu / đã render / đã QA / chờ duyệt / đã duyệt / đã đăng". Không gắn "đã render" khi video_id đang xử lý.
