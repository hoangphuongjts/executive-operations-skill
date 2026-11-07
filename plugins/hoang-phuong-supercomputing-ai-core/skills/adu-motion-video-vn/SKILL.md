---
name: adu-motion-video-vn
description: Hướng dẫn tiếng Việt dùng adunext/adu-motion-video và định dạng MotionGit .motion để tạo video đồ họa chuyển động có lời đọc, phụ đề, xuất MP4 và dự án có thể chỉnh sửa; chỉ triển khai runtime khi có quyền thực thi và đã kiểm tra giấy phép từng template.
---
# Adu Motion Video VN — Skill adapter dành cho Hoangphuong Supercomputing Core

## Xuất xứ và phạm vi
- Nguồn: https://github.com/adunext/adu-motion-video (GitHub). LICENSE của mã nguồn repo: MIT; tôn trọng thông báo bản quyền và THIRD_PARTY.md.
- Repo hướng người dùng đến https://motiongit.com/@adunext để tải các gói `.motion` mới nhất. **Không mặc định** một template `.motion` có giấy phép MIT chỉ vì repository cũ là MIT. Kiểm tra điều kiện riêng mỗi gói.
- Skill này là hướng dẫn và điều phối, KHÔNG chứa bản sao nguồn upstream, template `.motion`, plugin thực thi, server, quyền đăng nhập, hoặc trình render chạy sẵn.
- Bảo toàn toàn bộ 7 Skill gốc, 128 hồ sơ Agent, 16 cụm, 108 mã học tập, tất cả Skill khác và các kết nối của Core. Không thay đổi registry hay slash codes.

## Khi nào chọn
Video ngắn hoặc dài, infographic động, kinetic typography, video giải thích, bài học, lời thuyết minh có chuyển cảnh; muốn tái sử dụng template `.motion`, video ngang 16:9 hoặc dọc 9:16. Không dùng để sao chép trái phép video, logo, nhạc, hình người hoặc nội dung từ bên thứ ba.

## Quy trình hoạt động an toàn
1. Xác định mục tiêu, nội dung gốc, thời lượng, ngôn ngữ, khung hình, nguồn audio/nhạc/ảnh, giấy phép thương mại và nơi xuất; mặc định chỉ tạo bản nháp để người dùng duyệt.
2. Nguồn mới: người dùng cung cấp `.motion` từ trang chính thức. Kiểm tra file, manifest, cấu trúc, version, script thực thi, quyền và điều khoản trước khi mở/chạy. Xem hướng dẫn https://motiongit.com/use và https://motiongit.com/spec. Không giả định file `.motion` đã có trong môi trường hoặc có engine host.
3. Nguồn cũ: tham khảo GitHub `SKILL.md`, `AGENTS.md`, `references/` và trình pipeline Python; đọc `references/tooling.md` và `references/compatibility.md`. Với Windows, Python `scripts/pipeline.py` là đường được mô tả trong upstream; tránh sao chép nguyên lệnh Bash sang PowerShell nếu chưa tương thích.
4. Lên shot list: cue cụ thể từ lời nói, timecode thực, nội dung và tài sản tương ứng; style nhất quán; lựa chọn template không phỏng đoán ID/version. Tạo ảnh/nhạc riêng khi cần, không lấy tài nguyên không rõ quyền sử dụng.
5. Sau khi có quyền và môi trường thực thi, kiểm tra doctor, versions, dependencies, ffmpeg/chrome, font fallback. Chạy thử preview trước, xác minh chuyển cảnh/phụ đề/âm thanh; xuất MP4 và project editable dưới thư mục mới, không đè nguồn.
6. QA file cuối: ffprobe codec, fps, dimensions, length, black frames, silent spans, subtitle safe zones, clip seams, audio intelligibility, licensing log. Báo path/hash có bằng chứng; chưa test thì ghi chưa test.
7. Yêu cầu phê duyệt trước xuất bản, đăng tải, chi tiêu credits, sử dụng tài khoản hoặc thay đổi plugin/host. Không tự ý bật networking, OAuth hoặc thực thi mã ngoài.

## Phân biệt trạng thái
- Skill trong ChatGPT: hướng dẫn vận hành, không có engine render.
- Repo GitHub: mã nguồn và hướng dẫn; checkout và `npm install` trên máy riêng không mặc nhiên đồng nghĩa plugin ChatGPT đang chạy.
- MotionGit `.motion`: tài sản tải riêng, license riêng, cần người dùng cung cấp/ủy quyền tải và kiểm toán.
- Không nhận production-ready chỉ vì có demo hay test unit; chỉ xác nhận khi MP4 đã kiểm thử thật.

## Liên kết
- Repo: https://github.com/adunext/adu-motion-video
- README: https://github.com/adunext/adu-motion-video/blob/main/README.md
- Giấy phép repo: https://github.com/adunext/adu-motion-video/blob/main/LICENSE
- THIRD_PARTY: https://github.com/adunext/adu-motion-video/blob/main/THIRD_PARTY.md
- Thư viện mới: https://motiongit.com/@adunext
