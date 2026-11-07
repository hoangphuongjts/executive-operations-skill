---
name: channel-operations
description: Tổ chức lịch sản xuất, hàng đợi nội dung, phản hồi cộng đồng và bàn giao đăng bài có trạng thái kiểm chứng.
---

# Vận hành và phản hồi cộng đồng

Đọc [hồ sơ kênh](../../references/channel-brief.md) và [trạng thái công việc](../../references/channel-workflow.md). Cân lịch theo giờ làm thật; phân biệt công việc sản xuất với thời gian chờ render hoặc duyệt.
Mỗi nội dung có ID, phiên bản, mục tiêu, nguồn, tài sản, người duyệt, kênh và trạng thái. Lịch đề xuất không phải lịch đã lưu trong nền tảng. Đăng đa kênh cần trạng thái riêng cho từng nơi.
Với bình luận, nhóm câu hỏi, phản hồi, khiếu nại và spam theo dữ liệu đã đọc. Soạn câu trả lời hữu ích, không bịa chính sách bán hàng hoặc lời hứa giải quyết. Không tiết lộ thông tin cá nhân trong trả lời công khai.
Trước đăng, xác nhận nội dung cuối, tài khoản, thời điểm/múi giờ và quyền hành động theo yêu cầu công cụ. Nếu đã có ủy quyền đủ rõ thì không hỏi lại. Sau thao tác, lưu ID/URL và kiểm tra trạng thái; lỗi không đổi thành đã đăng.
Nếu thao tác có kết quả không rõ, đọc trạng thái trước khi thử lại để tránh trùng. Dừng sau hai lỗi giống nhau nếu không có cách khắc phục mới; báo phần đã làm và phần còn chặn. Không tự hẹn chạy nền khi chưa có tự động hóa được thiết lập.
