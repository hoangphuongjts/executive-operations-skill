# Quy tắc xử lý giao thoa ba Skill — 2026-11-07

Phạm vi: chỉ điều phối và kiểm chứng `ultra-thinking`, `thammuutruong`, `sieunangluc` với Core v16, `chidao` và các Skill sẵn có. Không sửa Skill gốc, không tự kích hoạt API/subagent, không tạo mã thuộc danh mục 108.

## Thứ tự ưu tiên
1. Chính sách nền tảng, quyền thực có thể quan sát, bảo mật và phê duyệt rõ ràng của người dùng luôn đứng đầu.
2. `hoangphuong-v16-active` giữ trách nhiệm kiểm chứng, bảo toàn 16 cụm, 128 vai trò và 108 mã học tập. `chidao` chỉ điều phối theo các giới hạn này.
3. Khi gọi đích danh một trong ba Skill mới, dùng đúng Skill chuyên môn đó; không tự gọi các Skill khác nếu không cần thiết. `/ultrathink` là bí danh của `ultra-thinking`, không phải một Skill mới.
4. Lệnh học tập được nhận diện duy nhất bằng đối sánh chính xác `STUDY_108_BASELINE.json`; ba lệnh Skill mới và `/chidao` không được thêm vào 108 mã gốc.

## Ma trận xung đột & cách xử lý
| Thành phần | Khả năng giao thoa | Cách xử lý | Mức kiểm chứng |
| --- | --- | --- | --- |
| ultra-thinking và First Principles/Socratic của Core | Trùng phương pháp suy luận | Chỉ kích hoạt `ultra-thinking` khi gọi rõ; không ép tất cả nhiệm vụ chạy chuỗi 5 tầng | Tĩnh + Host read; behavior E2E chưa kiểm thử |
| thammuutruong và chidao | Đều phân phối công việc, đòi subagent/duy trì Wiki | Core làm tổng điều phối; `thammuutruong` hỗ trợ chiến lược; chỉ gọi subagent và ghi Wiki nếu thực sự có công cụ, quyền, đường dẫn; tuyệt đối không tự nhận có memory hay worker chạy nền | Tĩnh + Host read; agent runtime E2E chưa kiểm thử |
| sieunangluc và các skill superpowers / AI Coding Kit | Trùng TDD, review, debug | Khi gọi đích danh `sieunangluc`, ưu tiên quy trình đó, tránh nạp nhiều skill trùng phạm vi; mọi yêu cầu xóa/ghi đè mã cũ chỉ được thực hiện khi đã có quyền và bản sao an toàn | Tĩnh + Host read; code E2E chưa kiểm thử |
| Các khẳng định '100%', tiết kiệm quota, Gemini/Flash | Không có bằng chứng năng lực hoặc model | Coi là nội dung hướng dẫn không xác nhận; không hứa bảo đảm, không tự phân công model hay chạy ngầm | Đã rà soát tĩnh |

## Trạng thái và bằng chứng
- Cả ba Skill đã xuất hiện qua `skills__list` và đọc bằng `skills__read` trong phiên 2026-11-07.
- Registry chính đã thêm 3 bản ghi `core_skill_overlay`, mỗi Skill chỉ có **một cụm chính** và các cụm liên quan là metadata; không nhân đôi Skill.
- Không có bằng chứng gọi runtime Agent độc lập, lưu Wiki lâu dài, lập trình bằng một model khác, hay E2E phát sinh chi phí.
- Không được đánh dấu `runtime_e2e_verified=true` chỉ từ việc Skill hiển thị trong danh mục.
