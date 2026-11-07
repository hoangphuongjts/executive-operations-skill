---
name: microsoft-autogen-adapter
description: "Dùng khi tích hợp hoặc kiểm thử Microsoft AutoGen, AgentChat, AutoGen Core, AutoGen Studio hoặc AutoGen Bench trong Hoàng Phương Core."
---

# Microsoft AutoGen

- Nguồn upstream: https://github.com/microsoft/autogen
- Cụm chính: 01 — Kỹ thuật phần mềm.
- Cụm tham chiếu: 02 — Tự động hóa và DevOps.
- Loại: Skill hướng dẫn và định tuyến. Runtime Python, Studio và Bench cần môi trường thực thi riêng.
- Tình trạng nguồn: README upstream ghi AutoGen đã được lưu trữ và Microsoft đã ngừng bảo trì.

## Định tuyến và thực hiện

1. Dùng AgentChat cho thử nghiệm nhóm Agent và hội thoại nhiều lượt. Dùng AutoGen Core khi cần truyền thông điệp theo sự kiện. Dùng Studio để thử giao diện và Bench để đánh giá trong môi trường riêng.
2. Khi thiết kế workflow, dùng hồ sơ Agent hiện hữu làm nguồn ánh xạ. Giữ ID gốc, xác định đầu vào, đầu ra, số lượt tối đa, timeout và tiêu chí kết thúc. Tham chiếu [bridge 16 cụm](../agent-workflow-16-cluster-bridge/SKILL.md).
3. Trước khi cài runtime, dùng [quy trình tiếp nhận repo](../github-repo-intake-vn/SKILL.md) để ghim commit, kiểm tra giấy phép, phụ thuộc và quyền. Thử trong môi trường Python cô lập bằng phản hồi giả lập, tắt tool thực thi lệnh và truy cập mạng.
4. Báo riêng trạng thái adapter, cài đặt runtime và kết quả chạy. Chỉ xác nhận chạy nhiều Agent khi có log từ runtime. Giữ các cổng phê duyệt hiện hữu cho gọi API, cấp quyền và triển khai.
