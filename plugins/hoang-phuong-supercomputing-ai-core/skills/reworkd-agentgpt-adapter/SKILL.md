---
name: reworkd-agentgpt-adapter
description: "Dùng khi tích hợp, phân tích hoặc thử nghiệm ứng dụng AgentGPT của Reworkd cho tác vụ AI Agent tự chủ trên trình duyệt."
---

# Reworkd AgentGPT

Nguồn: https://github.com/reworkd/AgentGPT. GitHub ghi nhận repo được lưu trữ ngày 28/01/2026.

- Cụm chính 01 — Kỹ thuật phần mềm.
- Cụm tham chiếu 02 — Tự động hóa và DevOps.
- Phạm vi: hướng dẫn và định tuyến. Ứng dụng và các phụ thuộc chạy trong môi trường riêng.

## Quy trình

1. Xác định yêu cầu về ứng dụng AgentGPT của Reworkd. Với Microsoft AutoGen, dùng [adapter AutoGen](../microsoft-autogen-adapter/SKILL.md).
2. Chuyển mục tiêu thành đầu vào có phạm vi, tiêu chí kết thúc, số bước tối đa và giới hạn thời gian. Ghi lại từng hành động và kết quả. Nếu ánh xạ hồ sơ Agent của Core, giữ ID hiện hữu và dùng [bridge 16 cụm](../agent-workflow-16-cluster-bridge/SKILL.md).
3. Trước khi thử upstream, dùng [quy trình tiếp nhận repo](../github-repo-intake-vn/SKILL.md) để ghim commit và rà soát giấy phép, Docker Compose, scripts, phụ thuộc và các điểm gọi dịch vụ bên ngoài.
4. Khi được phép chạy sandbox, dùng đầu vào tổng hợp và phản hồi mô hình giả lập. Vô hiệu hóa công cụ thực thi và truy cập mạng cho bài thử. Xác minh workflow dừng đúng giới hạn và trả log.
5. Báo riêng trạng thái của Skill, cài đặt ứng dụng và kết quả chạy. Áp dụng các cổng phê duyệt hiện có cho API trả phí, quyền truy cập và triển khai.
