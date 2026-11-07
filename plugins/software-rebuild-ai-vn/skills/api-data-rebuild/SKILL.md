---
name: api-data-rebuild
description: "Dùng khi phải suy ra đặc tả API và mô hình dữ liệu hợp pháp để viết lại phần mềm hoặc chuyển dữ liệu giữa ứng dụng."
---

# Đặc tả API và dữ liệu

- Chỉ dùng API docs chính thức, source được phép hoặc network traffic của tài khoản/test environment do người dùng kiểm soát. Không dò tìm API private khi không được phép, không đánh cắp token, khóa, cookie.
- Lập bảng endpoint, HTTP method, auth, schema, validation, pagination, retry, rate-limit, idempotency, error codes; đánh dấu chứng cứ thực tế vs giả định.
- Lập entity relationship diagram và migration plan; kiểm tra dữ liệu cá nhân, quyền riêng tư, backup, retention, xóa dữ liệu đúng quy định.
- Đề xuất OpenAPI/GraphQL/gRPC spec rõ ràng; có test contract, mock servers, integration tests và versioning.
- Thiết kế auth độc lập, không sử dụng thông tin đăng nhập hoặc khoá cũ không được chuyển giao hợp pháp.
- Mọi thao tác ghi/sửa/xóa dữ liệu thật cần xác nhận riêng và phương án rollback.
- Deliverable: API contract, data dictionary, ERD, sample JSON tổng hợp không chứa dữ liệu thật, test matrix.
