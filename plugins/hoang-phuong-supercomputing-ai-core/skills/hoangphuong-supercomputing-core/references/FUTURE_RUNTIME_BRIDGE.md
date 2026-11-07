# Future Runtime Bridge — Giữ lõi, nâng cấp khi có thiết bị

**Mặc định v14.2 = Skill nội bộ.** Những tệp hiện có trong `profiles/`, `scripts/`, `runtime/`, `references/AGENTS_128.json`, các Skill cũ vẫn được giữ nguyên. Không có server, Docker, API, VPS hay tác tử chạy nền nào được tự động bật.

## Nguyên tắc giữ tương thích
- ID 001–128 và 16 nhóm ổn định; không đổi tên file `agent-NNN.json`, không đổi `mission`, metadata hoặc contract của registry khi chưa có migration và kiểm thử.
- `EMBEDDED_128_MODE.json` cung cấp **ý định vận hành mặc định** cho lớp Skill. Nó không điều khiển, chặn hoặc tự khởi động executable Python/Docker cũ. Không có mã chạy nền mặc định.
- Mọi hồ sơ/sơ đồ/chương trình rèn luyện (curriculum) vẫn dùng lại được, không cần tái tạo 128 agents. Chỉ tạo adapter và cấu hình cụ thể cho môi trường mới.

## Lộ trình khi có VPS/server/VM
1. Xác nhận người dùng chủ động yêu cầu kích hoạt thực, hệ điều hành, CPU/RAM/GPU, mức sẵn sàng và ngân sách.
2. Tạo bản sao/backup, chạy validate 128 registry/profiles cùng bài test hiện có trên runtime; không sửa production trực tiếp.
3. Chọn một provider/model được phép; có thể dùng model tại máy hoặc API tương thích. Test 1 agent, rồi nhóm tối đa 8; không cần 128 processes. Lấy khóa từ secret manager/env và kiểm tra license dữ liệu.
4. Cấp quyền theo nguyên tắc tối thiểu, chặn expose cổng HTTP, bật rate limits/timeout/metrics/backup; tuyệt đối không lưu secret trong plugin.
5. Đo chuẩn chất lượng: tác vụ ngành, ground truth độc lập, tỷ lệ trích dẫn đúng, rủi ro, chi phí, độ trễ và lỗi; compare chế độ Skill với runtime thực.
6. Chỉ khi kiểm thử đạt và người dùng phê duyệt mới bật endpoint/agent runner. Khi chuyển từ Skill sang runtime, giữ ID và policy; không hứa tăng năng lực model nếu không có bằng chứng.

## Tình trạng
`skill_embedded` = có sẵn trong plugin; `agent_profile_defined` = 128 hồ sơ; `runtime_source_preserved` = mã nguồn được lưu; `runtime_deployed` = **chưa xác minh, mặc định false**; `agent_weights_fine_tuned` = **không thực hiện**.
