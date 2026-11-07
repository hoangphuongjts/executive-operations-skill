# Quy tắc phân loại và chuyển đổi

| Nguồn gốc | Gói đích ưu tiên | Điều kiện cần để dùng được |
|---|---|---|
| Prompt/template/hướng dẫn/phương pháp | Skill | Soạn SKILL.md có đầu vào, bước thực hiện, tiêu chí chất lượng; không quảng cáo có tool |
| Nhiều bước liên quan nhau, lịch trình, phê duyệt | Workflow | Có trigger, dữ liệu vào/ra, retry, logging và approval; nếu chỉ là hướng dẫn thì đóng gói trong Skill |
| Vai trò chuyên gia, bộ định tuyến đa nhiệm | AI Agent | System/skill instructions, quyền công cụ, đánh giá kết quả; có thể đóng gói thành plugin skills-only nếu chưa có runtime riêng |
| API, dịch vụ SaaS, remote MCP endpoint | Plugin + MCP | Endpoint thật, xác thực, quyền phù hợp; không bịa ra server/URL |
| GitHub repo Python/Node/Rust | Skill hướng dẫn hoặc Plugin MCP | Repo không tự trở thành tool ChatGPT. Muốn chạy cần backend/host, license, dependency, bảo mật và endpoint xác minh |
| Mô hình AI có weights/CLI | Skill + dịch vụ chạy model khi có | Không giả vờ ChatGPT host đã cài weights hay GPU |
| Trang web, sản phẩm cloud, ứng dụng Windows | Workflow/Skill hoặc Plugin khi có API | Nếu không có API, hướng dẫn thủ công/automation được cấp quyền; không khai báo kết nối giả |
| Tập dữ liệu, bộ tài liệu | Skill + references hoặc thư viện | Chỉ thêm khi có quyền phân phối; tránh nhúng dữ liệu riêng tư |
| Source chưa rõ, tệp không tin cậy | Chưa đóng gói | Cần tìm nguồn, giấy phép và kiểm tra trước |

**Tiêu chí lựa chọn:** (1) Chức năng thực sự, (2) Quyền truy cập, (3) Có cần runtime, (4) Mức độ tự động hóa, (5) Khả năng cài trong ChatGPT, (6) Khả năng rollback, (7) Chi phí.

**Không được đồng nhất:** đóng gói hướng dẫn sử dụng repo ≠ cài repo trên Windows ≠ chạy repo ≠ tích hợp API. Mỗi trạng thái phải báo riêng.
