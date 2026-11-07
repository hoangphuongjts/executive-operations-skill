---
name: api-contract-compatibility-testing-vn
description: "Dùng khi cần xây ma trận kiểm thử tương thích contract API giữa provider và consumer, kiểm tra null, enum, lỗi và phiên bản wire-level từ đặc tả và mã thực tế, không thay thế skill thiết kế API."
---
# Kiểm thử tương thích hợp đồng API từ hai phía

**Loại:** Prompt-only, không chứa mã hay dependency upstream. **Nguồn:** sickn33/agentic-awesome-skills, skill api-contract-testing tại commit ghim; MIT. Xem `references/PROVENANCE.md`, `references/UPSTREAM_LICENSE_MIT.txt`.

## Khi dùng
Khi API/JSON Schema/OpenAPI/protobuf/events thay đổi, các client/server build thành công nhưng bất đồng runtime, hoặc cần xác nhận thay đổi có tương thích ngược. Không tự gọi production, không publish API, không chuyển dữ liệu thật hay credentials vào báo cáo.

## Quy trình độc lập
1. **Khóa bằng chứng:** xác định provider, transport, version, hợp đồng nguồn, consumer đã biết, payload thực tế đã được phép dùng; phân biệt lời hứa tài liệu, wire output và generated types.
2. **Phân loại delta:** rà soát required/optional, missing/null, kiểu dữ liệu, enum mới, field thừa, header/status code/error envelope, pagination, event duplicate/order/version. Xác nhận chính sách client đối với field lạ.
3. **Ma trận phiên bản:** old consumer ↔ new provider, new consumer ↔ old provider nếu được hỗ trợ; ghi rõ tổ hợp nào phải chạy qua kiểm thử thật và tổ hợp nào chưa kiểm chứng.
4. **Dữ liệu thử an toàn:** xây fixtures tổng hợp cho success, empty, malformed, missing, explicit null, unknown enum, error bodies và boundary conditions; không dùng dữ liệu khách hàng hay token thật.
5. **Kiểm chứng đúng tầng:** đối chiếu schema, serialize provider, parse consumer, error mapping; mocks chỉ kiểm tra giả định bên trong mock, không chứng nhận thực thi server; nếu không có runtime được phép, chỉ soạn test plan và trạng thái `NOT EXECUTED`.
6. **Báo cáo:** `Contract change | Affected consumer | Fixture | Expected | Observed | Evidence | Compatibility | Risk`; nếu breaking, đề xuất versioning, adapter, staged rollout/rollback có chủ sở hữu.

## Cổng an toàn
Không chạy tool ở endpoint production hoặc thay đổi state nếu chưa được phép; giữ nguyên dữ liệu, giao diện công khai và security policy hiện hữu. Bằng chứng must-pass là test chạy thật trong môi trường được phép; thiết kế test ≠ test pass.

## Phân biệt Skill đang có
`addy-api-and-interface-design` và `system-design-planning-vn` ưu tiên thiết kế interface; Skill này **kiểm thử sự tương thích provider–consumer ở dạng thực thi qua wire** và phân biệt giả lập/đặc tả với kiểm chứng thực.
