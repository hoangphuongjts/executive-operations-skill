---
name: nango-security-vn
description: Dùng khi thiết kế bảo mật, kiểm tra scope, so sánh Nango Management MCP và runtime MCP, hoặc chuẩn bị Nango OAuth/API key cho ChatGPT và các AI Agent.
---

# Nango Security VN

## Phân vùng quyền
- `https://mcp.nango.dev/mcp`: Management MCP phục vụ kỹ sư triển khai, quản trị kết nối và proxy, đăng nhập bằng Nango environment API key Bearer.
- `https://api.nango.dev/mcp`: Tool-calling MCP để Agent sử dụng một kết nối cụ thể, cần `environment:mcp`, `connection-id` và `provider-config-key` theo tài liệu Nango. Không gộp 2 key; không kết nối runtime agent bằng key quản trị.

## Nguyên tắc bảo mật
- Chỉ tạo/sử dụng khóa cho môi trường dev/staging và quyền tối thiểu cần thiết.
- Không cấp `environment:integrations:read_credentials` hoặc `environment:connections:read_credentials` cho Agent trừ khi thực sự bắt buộc, được thẩm định và duyệt.
- Không hướng dẫn người dùng dán API key, cookie, mật khẩu vào nội dung chat hoặc plugin ZIP. Cấu hình secrets chỉ trong UI kết nối được tin cậy.
- Mặc định đọc metadata, không sửa hoặc triển khai. Trước lệnh có tác động ra ngoài, tóm tắt quyền, hệ thống và hành động; xin phê duyệt.
- Không tự ý mở public proxy, không tự động gửi dữ liệu bên thứ ba, không tự động xuất bản nội dung.
- Theo GitHub nguồn, Nango có giấy phép Elastic License 2.0 (ELv2), có các hạn chế cung cấp lại dịch vụ; đừng mô tả nó là MIT/Apache hay đảm bảo vô điều kiện dùng thương mại.

Tài liệu: https://nango.dev/blog/how-to-build-ai-agent-integrations-using-the-nango-management-mcp
