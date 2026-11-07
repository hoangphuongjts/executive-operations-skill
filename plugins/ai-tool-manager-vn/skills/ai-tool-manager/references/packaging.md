# Quy trình tạo gói và xác minh

## Trước khi tạo

- Kiểm tra có plugin/skill cùng tên hoặc cùng chức năng chưa; nếu có, đề xuất dùng/khôi phục/cập nhật thay vì tạo trùng.
- Tên gói lowercase kebab-case, không quá 64 ký tự. Ghi nguồn và phiên bản; không đổi tên repo gốc trong phần attribution.
- Theo cấu trúc Agent Plugins 1.0 và hướng dẫn chính thức của Plugin Creator trong phiên sử dụng. Dữ liệu dưới đây chỉ là mô hình tổ chức, không thay thế chuẩn schema chính thức đang áp dụng.

## Cấu trúc tối thiểu của plugin skills-only

    example-plugin/
      plugin.json
      skills/example-workflow/SKILL.md
      agents/openai.yaml          # tùy chọn, giúp ChatGPT gợi ý agent
      skills/example-workflow/references/... # tùy chọn

Manifest dùng schema `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`; mô tả hiển thị nằm dưới `extensions.com.openai.interface`. Skill có YAML frontmatter `name` và `description`. Khi cần gọi API/MCP thật, phải bổ sung `mcp.json` với endpoint và auth đã kiểm chứng, không đặt địa chỉ ví dụ vào package triển khai.

## Quy trình tạo

1. Thiết kế chức năng đo được, input/output và quyền.
2. Soạn một hoặc nhiều skill tách biệt theo nhiệm vụ, cung cấp examples và điều kiện lỗi.
3. Chỉ nhúng tài nguyên có quyền sao chép và phù hợp giấy phép.
4. Kiểm tra JSON, YAML, manifest, đường dẫn, cấu trúc ZIP/tar.gz; tránh file thừa và secrets.
5. Với plugin riêng tư, dùng Plugin Creator `create_plugin` nếu có. Với plugin sẵn có do người dùng sở hữu, dùng `update_plugin` khi được ủy quyền. Không dùng thao tác tạo làm phép thử placeholder.
6. Kiểm tra phản hồi lưu tài khoản và công cụ mới nạp. Chạy thử một lệnh an toàn khi công cụ thực sự có sẵn. Không tuyên bố “tự động” nếu chỉ có tài liệu.
7. Báo rõ trạng thái: **đóng gói** / **lưu** / **kết nối** / **kích hoạt** / **kiểm thử**.

## Mẫu báo cáo

- **Công cụ:** tên và nguồn chính thức.
- **Nhận diện:** nguồn là repo/app/model/tài liệu; gói mới là Skill/Plugin/Agent/Workflow.
- **Mức độ tích hợp:** chỉ dẫn / skill ChatGPT / API / MCP / runtime ngoài.
- **Bảo mật/giấy phép:** đã xác minh hoặc rủi ro còn lại.
- **Trạng thái:** đã có, đã tạo gói, đã lưu tài khoản, cần kết nối, đã kiểm thử, hoặc chưa thể triển khai.
- **Kết quả:** ID/link xác thực và thao tác kế tiếp (nếu có).
