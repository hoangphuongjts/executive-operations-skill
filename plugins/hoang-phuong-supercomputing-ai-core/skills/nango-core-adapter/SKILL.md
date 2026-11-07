---
name: nango-core-adapter
description: "Định tuyến tác vụ OAuth, API gateway, Nango Management MCP, Nango runtime MCP, integrations, API proxy hoặc kết nối AI Agent qua Nango từ Hoangphuong Supercomputing Core; cần quyền và xác thực độc lập."
---

# Nango Core Adapter — Hoangphuong Supercomputing Core v16

## Vị trí và nguồn sự thật
- Loại: **federated adapter hướng dẫn/định tuyến** (Core). **Không phải** Nango runtime, không tự kết nối dịch vụ, không cài thêm Nango server.
- Plugin nguồn do cùng chủ sở hữu quản lý: `nango-gateway-vn`, ID backend `plugins_6ae8e19ae92c8191b70c24cb9ab700d8`, phiên bản đã đọc `0.1.0`. Giữ plugin gốc độc lập; không sao chép, xóa hoặc đổi quyền của plugin gốc.
- Nếu host hiển thị các Skill nguồn thì ưu tiên `nango-gateway-vn`, `nango-security-vn`, `nango-video-ai-vn` thuộc plugin nguồn. Không giả định host luôn nạp các Skill này.
- Endpoint **Management MCP** ở plugin nguồn: `https://mcp.nango.dev/mcp` dùng streamable HTTP; yêu cầu Bearer environment API key riêng trong UI xác thực an toàn.
- Endpoint **tool-calling/runtime MCP** là `https://api.nango.dev/mcp`, khác management, yêu cầu cấu hình provider, connection và quyền theo Nango. Adapter Core **không** đăng ký runtime endpoint này hay cấp quyền mặc định.

## Khi nào kích hoạt
Yêu cầu tích hợp API, kết nối OAuth, dùng Nango để quản lý connectors, xem connection status, API proxy, actions, sync, tích hợp Nango với AI Agent/Gemini/n8n/video/Drive/YouTube hoặc kiểm toán quyền kết nối.

## Bộ định tuyến fail-closed
1. Xác định mục tiêu, provider cụ thể, tác vụ read-only hay write, dữ liệu liên quan và bằng chứng quyền của người dùng.
2. Dò công cụ Nango thực sự có mặt trong phiên. **Không tự bịa tên tool/endpoint/schema hoặc giả lập lệnh đã chạy**.
3. Nếu tool không có hoặc chưa xác thực: trả `requires_connection`; giải thích cách xác thực Nango Gateway VN qua giao diện an toàn, không yêu cầu khóa trong chat.
4. Nếu tool có và xác thực: ưu tiên **read-only metadata** (tích hợp, connection state, scope); không truy xuất hay in API key, token, credential. Phân biệt metadata quan sát được và thao tác thực sự.
5. Với việc tạo/sửa/xóa integration, actions, proxy, webhooks, refresh credentials, publish: liệt kê tác động và yêu cầu phê duyệt phạm vi riêng trước khi thực hiện; bắt đầu dev/staging, least privilege.
6. Nếu muốn dùng runtime tool-calling: kiểm chứng cấu hình provider-config-key, connection-id, scope, tài khoản, rate limit và cost; không cho Core thay thế security boundary của Nango.
7. Sau hành động được phép, đối chiếu response, ID, health/logs. Chỉ ghi `HOST_VERIFIED` khi có bằng chứng. Không ghi `DEPLOYED` từ sự hiện diện của Skill.

## Kiến trúc phối hợp
`Hoangphuong Core -> nango-core-adapter -> công cụ của Nango Gateway VN (nếu host đã cấp quyền) -> Nango Management MCP -> provider configuration`.

`Hoangphuong Core -> runtime connector riêng có xác thực phù hợp -> Nango tool-calling MCP -> API nhà cung cấp`, chỉ khi thiết lập và duyệt riêng.

Giữ namespace Nango trong plugin nguồn; không nhúng Nango mcpServers vào manifest Core, tránh endpoint trùng, khóa trùng hoặc quyền mới không có chủ ý. Các modules Core khác được giữ nguyên. Khi nảy sinh xung đột, ưu tiên kết nối hiện hữu, không đổi settings của plugin khác.

## Kết quả và trạng thái
- `ADAPTER_PACKAGED`: Skill hiện diện trong archive Core.
- `HOST_VISIBLE`: plugin được host nạp và Skill có thể đọc trong phiên.
- `REQUIRES_CONNECTION`: chưa có công cụ Nango khả dụng hoặc chưa xác thực.
- `AUTHENTICATED_READ_ONLY`: chứng minh được công cụ đọc metadata được ủy quyền.
- `WRITE_ENABLED`: chỉ sau khi người dùng xác nhận quyền/đối tượng/chi phí và host cho phép.
- `END_TO_END_VERIFIED`: có log/response thật, không chỉ mô phỏng.

## An toàn và phạm vi
Không sửa OAuth scopes, không lấy credentials, không chạy nền, không mở proxy công khai, không xuất bản video hoặc nhắn tin, không dùng credit hoặc trả phí khi chưa được duyệt. Không tạo slash-code mới và giữ nguyên 108 mã học tập, 128 profile, 7 Skill gốc, 16 cụm cùng ID hiện hữu. Thực hiện 5 cổng kiểm toán Core: Trigger Accuracy, Context Bloat, Logic Robustness, Safety, Format Compliance.

Xem `references/CONNECTION_POLICY.md` để kiểm tra kết nối/rollback.
