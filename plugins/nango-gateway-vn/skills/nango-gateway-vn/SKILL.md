---
name: nango-gateway-vn
description: Sử dụng khi người dùng muốn tìm hiểu, kết nối hoặc quản lý Nango API Gateway, Nango Management MCP, OAuth, API proxy, action, sync hoặc tích hợp API với AI Agent và ChatGPT.
---

# Nango Gateway VN — Sử dụng trong ChatGPT

Nguồn gốc: https://github.com/NangoHQ/nango. Các chức năng và điều kiện xác thực tham khảo https://nango.dev/docs/ và https://nango.dev/blog/how-to-build-ai-agent-integrations-using-the-nango-management-mcp.

## Khả năng thực sự
- Plugin có kết nối `nango-management` qua **Streamable HTTP** tại `https://mcp.nango.dev/mcp`, không chứa khóa bí mật.
- Trước khi dùng công cụ, cần người dùng chủ động đăng ký/đăng nhập Nango và cấp một Nango environment API key trong UI kết nối an toàn nếu ChatGPT hiển thị hỗ trợ; không yêu cầu dán khóa vào hội thoại.
- **Management MCP** chỉ để cấu hình, truy vấn và bảo trì Nango; có thể có quyền triển khai và proxy theo scope được cấp. **Runtime Tool-calling MCP** là máy chủ khác: `https://api.nango.dev/mcp`, yêu cầu `Authorization: Bearer`, `provider-config-key`, `connection-id`; plugin này không tự động có quyền dùng runtime server.
- Việc tạo plugin không tự đăng ký Nango, không kết nối tài khoản nhà cung cấp, không cấp quyền OAuth, không biến hàng nghìn API thành công cụ sử dụng được ngay.

## Cách làm việc
1. Bắt đầu bằng kiểm tra trạng thái công cụ Nango và chỉ thực hiện thao tác chỉ-đọc khi được cho phép.
2. Xác định API đích, hành động đọc hay ghi, tài khoản và dữ liệu liên quan.
3. Tạo môi trường thử nghiệm trước, cấp quyền tối thiểu, rồi xác thực qua cửa sổ nhà cung cấp.
4. Kiểm tra metadata của integration, kết nối, scope và endpoint; không đọc hoặc in khóa/credentials vào phản hồi.
5. Với thao tác ghi, tạo mới hoặc triển khai: trình bày đối tượng, tác động, quyền và yêu cầu người dùng xác nhận.
6. Sau triển khai, đọc logs và đối chiếu kết quả; không tự động đăng bài hay gửi thông tin nhạy cảm.

## Thực hành
- Chỉ gọi đúng tên/schemas tool thực sự được kết nối; không tự bịa tên lệnh.
- Nếu server chưa kết nối/chưa xác thực, chỉ đưa đường dẫn cấu hình và giải thích điều kiện còn thiếu.
- Hạn chế sao chép token ra log, webhook, chat hay file công khai.
- Tự lưu trạng thái triển khai chỉ sau khi có phản hồi thành công.
