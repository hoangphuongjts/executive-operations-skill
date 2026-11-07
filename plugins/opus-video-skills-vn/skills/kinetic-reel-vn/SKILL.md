---
name: kinetic-reel-vn
description: Thiết kế và hướng dẫn dựng video kinetic typography, motion graphics, WebGL và nhạc nền bằng mã từ opus-video-skills; hỗ trợ storyboard, render và QC.
---
# Kinetic Reel VN — adapter an toàn
Nguồn upstream: https://github.com/tuzhechen2005/opus-video-skills/tree/main/skills/kinetic-reel
Bản này là hướng dẫn workflow, không chứa engine hay bảo đảm xuất MP4 trực tiếp trong ChatGPT.

1. Nhận brief: mục tiêu, thông điệp, tệp khán giả, số liệu được xác minh, thời lượng, bố cục 9:16/16:9.
2. Lập STORYBOARD.md từng shot, cue/timing, hiệu ứng chữ, cơ chế trực quan, hiệu ứng chuyển cảnh và âm thanh.
3. Theo upstream, engine dùng Canvas 2D, three.js/WebGL, render.mjs và FFmpeg; âm nhạc tổng hợp theo cues timeline.
4. Khi runtime đã được cài và kiểm toán, kiểm tra contact sheets, font tiếng Việt, tiêu đề, HUD safe zones, subtitle, nhịp, âm thanh và encode.
5. Dữ liệu minh họa không có nguồn phải đánh dấu SCHEMATIC. Không dùng thương hiệu, nhạc, logo, font hoặc tư liệu bên thứ ba khi chưa có quyền.
6. Kiểm tra ffprobe và nghe/kiểm tra file MP4 trước khi bàn giao. Không tự đăng mạng xã hội.
7. Nếu muốn dùng source gốc, cần kiểm tra bản quyền, commit, dependencies, scripts và host runtime riêng. Không tự động thực thi trong ChatGPT.

Có thể phối hợp với Hoangphuong Supercomputing Core để thẩm định code, chất lượng sản phẩm và phương án tích hợp FFmpeg.
