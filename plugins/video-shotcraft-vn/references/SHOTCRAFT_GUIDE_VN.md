# Video ShotCraft — chỉ mục thực hành tiếng Việt

## Nguồn chính thức
- Repo: https://github.com/Vincentwei1021/video-shotcraft
- Trang Gallery: https://vincentwei1021.github.io/video-shotcraft/
- Tài liệu gốc: https://github.com/Vincentwei1021/video-shotcraft/blob/main/SKILL.md
- Quy trình: https://github.com/Vincentwei1021/video-shotcraft/blob/main/references/pipeline.md
- Quy trình chung sáng tạo: https://github.com/Vincentwei1021/video-shotcraft/blob/main/references/guided-free-creation.md
- Template mẫu: https://github.com/Vincentwei1021/video-shotcraft/blob/main/template/TEMPLATE.md
- Workbench: https://github.com/Vincentwei1021/video-shotcraft/blob/main/workbench/README.md

## Hiệu ứng xuất hiện trong README/TEMPLATE (ví dụ, không phải danh sách đầy đủ)
| Tên tham khảo | Mục tiêu |
|---|---|
| brand-ink-open | Mở đầu thương hiệu |
| spotlight-hero-card | Nhấn sản phẩm/điểm chính bằng spotlight |
| deck-deal-flyin | Các thẻ phân phát và bay vào bố cục |
| row-embed | Chi tiết tính năng hoặc hàng dữ liệu |
| list-stack-press | Danh sách/đối tượng xếp chồng |
| document-typewriter-reveal | Nội dung hiện theo hiệu ứng đánh máy |
| outro-group-photo-launch | Gom các thành phần, kết thúc thương hiệu |
| flying-words | Chữ bay, giới thiệu từ khóa |
| paper-title-card | Chuyển đoạn bằng chữ |
| text-as-mask | Tiêu đề dạng mặt nạ |

Xác nhận category/tên chính xác qua Gallery hoặc `gallery/api/library.json` trước khi trích dẫn đường dẫn card cụ thể. Không suy luận tên biến thể từ mô tả.

## Quy trình gợi ý 30 giây cho video sản phẩm
- 0–3s: Hook / nêu lợi ích chính
- 3–8s: Chi tiết sản phẩm bằng cảnh hero và camera
- 8–19s: 2–3 điểm nổi bật có chứng cứ ảnh thực
- 19–25s: Lợi ích/so sánh dựa trên dữ liệu có nguồn
- 25–30s: CTA và logo

Không công bố video, nhạc và bản quyền người khác khi chưa có quyền. Xóa/ẩn dữ liệu người dùng khỏi screenshot.

## Windows (theo repo gốc)
Điều kiện cơ bản: Node.js + npm; FFmpeg/ffprobe để kiểm tra video. Có thể cần uv để phân tích nhịp, Puppeteer để chụp ảnh web. Tác giả kiểm thử chủ yếu trên macOS; Windows có rủi ro symbolic-link.

Lệnh mẫu (tại root repo):
```powershell
cd template
npm ci
npm run dev
# chạy ở terminal khác, trong template:
npm run render
```

```powershell
cd workbench
npm ci
npm run dev
# http://localhost:5198 trên máy tính đang chạy dev server
```

Để mở một Remotion project đã chuẩn bị bằng công cụ:
`node workbench/scripts/open.mjs <duong-dan-du-an>`

## Phân định các lớp tính năng
1. **Skill plugin ChatGPT**: nhận yêu cầu, tạo storyboard, shot list, đề xuất mã Remotion, hướng dẫn kiểm thử.
2. **Remotion + Motion Workbench**: sử dụng máy chủ có Node.js, browser và FFmpeg để preview/render.
3. **Video API được cấp phép (ví dụ Runway)**: một con đường khác để tạo video bên trong ChatGPT, không có nghĩa đang dùng code Video ShotCraft.
4. **n8n/Upload-Post**: tự động xuất bản chỉ khi có API, giấy phép và người dùng phê duyệt.

Không nói video đã tạo/xuất/đăng nếu không có artifact và bằng chứng thành công.
