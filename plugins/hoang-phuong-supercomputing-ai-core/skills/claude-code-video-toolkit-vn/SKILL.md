---
name: claude-code-video-toolkit-vn
description: "Skill tham chiếu tiếng Việt cho wilwaldon/Claude-Code-Video-Toolkit; lập kế hoạch video Remotion/Manim, quay màn hình, phụ đề và FFmpeg. Chỉ tham chiếu nguồn và điều phối; không chứa engine hay cài phụ thuộc."
---

# Claude Code Video Toolkit VN — Adapter tham chiếu cho Hoang Phuong Supercomputing Core

## Trạng thái và nguồn
- **Đã đóng gói:** Skill hướng dẫn và danh mục nguồn (reference-only). **Không phải** mã nguồn của upstream đã được cài hay một engine tạo MP4 đang chạy.
- Trang nguồn: https://github.com/wilwaldon/Claude-Code-Video-Toolkit
- Commit nguồn đã kiểm tra: `a6e9e5225d85585472666598297f47d9584f9a97` (2026-02-26); chỉ có `README.md` ở root tại commit này.
- README ghi `MIT` nhưng trỏ đến `LICENSE` không có trong cây file tại thời điểm kiểm tra 2026-11-05. Vì vậy không sao chép README, code hoặc các gói bên thứ ba. Liên kết tới nguồn chỉ để nghiên cứu, không cấp phép cài hàng loạt.
- Các công cụ mà README liệt kê đều là **dự án/thành phần riêng** và cần tự kiểm tra commit, giấy phép, phần mềm phụ thuộc, rủi ro và chi phí trước khi cài.

## Khi nào sử dụng
Người dùng cần thiết kế pipeline sản xuất video giáo dục, quảng cáo, demo sản phẩm, mô phỏng toán/vật lý/khoa học, caption song ngữ hoặc xử lý FFmpeg; đặc biệt khi họ nói Claude Code Video Toolkit hoặc muốn so sánh video stack.

## Phân loại năng lực từ nguồn
1. **Remotion Agent Skills:** hướng dẫn viết video bằng React/Remotion; không nhầm các lệnh của Claude Code với lệnh trong ChatGPT. Nguồn chính https://www.remotion.dev/docs/ai/claude-code.
2. **digitalsamba/claude-code-video-toolkit:** project template gồm skills, commands, thiết kế giao diện chuyển động và thương hiệu. Nguồn https://github.com/digitalsamba/claude-code-video-toolkit.
3. **Yusuke710/manim-skill:** kỹ năng làm animation khoa học/toán; nguồn https://github.com/Yusuke710/manim-skill.
4. **HarleyCoops/Math-To-Manim:** pipeline tạo cảnh Manim từ mô tả/hình ảnh; nguồn https://github.com/HarleyCoops/Math-To-Manim.
5. **Manim MCP Server:** README trỏ tới bài viết về server, chưa xác nhận máy chủ hay quyền MCP; coi là ứng viên chưa kiểm toán.
6. **Playwright MCP `--save-video`:** tùy chọn ghi hình phiên trình duyệt; không có quyền điều khiển browser hoặc ghi hình nếu chưa cài và cấp quyền.
7. **op7418/Youtube-clipper-skill:** cắt/chia chương, phụ đề; nguồn https://github.com/op7418/Youtube-clipper-skill. Chỉ tải/sử dụng video khi có quyền hợp pháp; không vượt bảo vệ DRM.
8. **FFmpeg Skill:** nguyên tắc chuyển mã, chuẩn hóa khung hình, phụ đề, âm thanh; phần tham chiếu của bộ digitalsamba. FFmpeg engine phải được kiểm tra và cài trong runtime riêng.

## Quy trình vận hành — không phá hủy
1. Nhận brief: nội dung, đối tượng, thời lượng, 9:16 hoặc 16:9, ngôn ngữ, nguồn ảnh/nhạc/TTS và quyền sử dụng. Mặc định chỉ tạo bản nháp chờ duyệt.
2. Lập danh sách cảnh, storyboard, scripts, SRT/vị trí phụ đề và phân tuyến engine phù hợp. Với kênh giáo dục, kiểm chứng nội dung và nguồn độc lập.
3. So sánh với các Skill đang có: `sanxuatnoidung` (kịch bản), `explainer-studio-vn` (video giải thích), `adu-motion-video-vn` (đồ họa chuyển động), `cluster-skill-05-content-media` (điều phối). Không tự thay thế engine hay workflow hiện có.
4. Nếu cần thực thi: chuẩn bị đề xuất triển khai riêng. Trước khi tải một thành phần gốc, kiểm tra chính chủ, pinned commit, LICENSE thật, dependency lockfile, install hooks, quyền mạng, dữ liệu riêng tư, API key, TTS, assets, phí/credits và rollback. Không chạy `npx`, `pip`, `npm`, Claude CLI hoặc script từ README khi chưa qua kiểm toán.
5. Chỉ thực thi trong môi trường có công cụ và quyền thực tế. Kiểm tra phiên bản, build sandbox, kiểm tra output bằng ffprobe, nghe lời thoại, đối soát sync SRT, crop/safe zones, giấy phép và tính nguyên gốc.
6. Không đăng hoặc đưa media lên mạng xã hội trước khi được duyệt. Không tuyên bố đã render MP4, kích hoạt MCP, cài npm hoặc đã hoàn thành sản xuất nếu không có file/đầu ra kiểm thử.

## Ranh giới và tương thích
- Hệ thống ChatGPT chỉ nhìn thấy **Skill này** như hướng dẫn nếu plugin được cập nhật thành công. Không tự động có Claude Code CLI, Remotion, Manim, Playwright MCP, FFmpeg hoặc Youtube Clipper.
- Không tạo mới hay chiếm các lệnh `/video`, `/record-demo`, `/brand` hoặc bất kỳ lệnh `/` nào thuộc **108 mã học tập gốc**. Các lệnh trong README là lệnh riêng của công cụ upstream.
- Giữ nguyên 7 Skill gốc, 128 hồ sơ Agent, 16 cụm và mọi plugin khác, khóa/API, cấu hình/OAuth. Không chạy job nền, không tạo chi phí, không tự động upload hoặc phát hành.
- `source_audited` và `host_verified` chỉ được ghi nhận sau kiểm toán và xác minh riêng từng engine; tham khảo file `references/PROVENANCE.md`.
