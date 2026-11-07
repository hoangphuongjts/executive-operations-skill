# KIỂM TOÁN RỦI RO & KIỂM SOÁT

Ngày kiểm toán: 2026-11-04. Môi trường: sandbox local, Python 3.13; không truy cập plugin gốc trên máy người dùng.

| Threat / kiểm soát | Trạng thái | Bằng chứng / giới hạn |
|---|---|---|
| Kill switch mặc định bật | OFFLINE_TESTED (sau test) | Unit test khởi tạo Orchestrator mặc định |
| Hành động nhạy cảm fail-closed | OFFLINE_TESTED (sau test) | write, publish, delete, payment, admin, network bị chặn |
| Allowlist tài nguyên | OFFLINE_TESTED (sau test) | nguồn ngoài local:plan/local:demo bị từ chối |
| Giới hạn chi phí/đầu vào | OFFLINE_TESTED (sau test) | estimated_cost_usd và task length; không đo actual provider bill |
| Bất biến registry gốc | NOT_IN_SCOPE | Không được mount/chỉnh sửa registry gốc; chưa có hash baseline trực tiếp |
| Audit chain integrity | OFFLINE_TESTED (sau test) | phát hiện sửa row trong cùng SQLite; không ngăn administrator xóa/ghi lại toàn bộ chain |
| Chống prompt injection từ repo | DESIGNED | chưa nạp hoặc thực thi tài liệu repo |
| Bí mật, key storage | BLOCKED | không có vault/KMS; HMAC key test chỉ phục vụ thử nghiệm |
| Xác thực/ủy quyền multi-user | BLOCKED | không có API/server; không được đưa vào internet |
| OAuth/MCP/host permission | BLOCKED | registry metadata không phải quyền truy cập |
| Independent multi-agent runtime | BLOCKED | không có model endpoint, scheduler hoặc isolation |
| Production SLO, load testing | BLOCKED | benchmark local không đánh giá tải hệ thống thật |

## Kiểm toán 5 chiều
- Trigger Accuracy: Router heuristic đơn giản; thiếu hold-out có nhãn ⇒ chưa đánh giá độ chính xác thực.
- Context Bloat: max_input_chars và max_steps đã cấu hình; chưa có tokenizer / summary quality.
- Logic Robustness: tests negative path, unknown actions, tamper detection; chưa có concurrency/load/fuzz đầy đủ.
- Safety: các hành động có tác động ngoài mặc định từ chối; thiếu hardening tầng OS/host.
- Format Compliance: JSON CLI, file báo cáo, unit tests; chưa có hợp đồng API công khai / schema versioning.

## Quy trình release gate (phải hoàn thành trước khi gọi production)
1. Gắn phiên bản + hash registry gốc và overlay, có người review độc lập.
2. Golden hold-out tối thiểu 200 truy vấn do người đánh giá gắn nhãn; đánh giá CI được lặp lại.
3. Hardening network, authN/Z, per-tenant secret storage, cost accounting, sandbox và egress controls.
4. Phê duyệt tool-side quyền ghi/đăng/xóa, audit backend bất biến, diễn tập rollback.
5. Canary pilot rồi mới dần nâng hạn mức; có theo dõi và kiểm chứng thật.
