---
name: external-capability-bridge
description: "Định tuyến 181 Skill ngoài Core và 14 plugin cá nhân vào 16 cụm theo chức năng, dùng cầu liên kết federated không xóa hay sao chép plugin nguồn."
---

# External Capability Bridge — 16 cụm chuyên môn

## Phạm vi
- Danh mục chuẩn: `references/EXTERNAL_16_CLUSTER_REGISTRY.json`, gồm 181 URI Skill và 14 plugin cá nhân do tài khoản sở hữu (theo snapshot 2026-11-05).
- Đây là **liên kết định tuyến**; không chuyển quyền sở hữu, không di chuyển binary, không nhân bản plugin và không tự mở kết nối MCP/API.
- Phân loại theo từng nhiệm vụ/Skill, mỗi Skill có **một cụm chính**. Có thể phối hợp cụm phụ khi xử lý đầu vào thực tế, nhưng không tính trùng vào số lượng.

## Quy trình nhận nhiệm vụ
1. Nhận intent; so với 16 cụm hiện hữu; đọc chỉ mục `EXTERNAL_16_CLUSTER_REGISTRY.json` để tìm Skill phù hợp.
2. Chọn tối đa 1–3 Skill nguồn liên quan theo `source_uri`, đọc nội dung Skill thực từ host trước khi thực thi, không suy diễn từ tên.
3. Kiểm tra `host-visible` và tool-calling thực tế: nếu Skill chỉ là hướng dẫn thì dùng hướng dẫn; nếu công cụ plugin không có, báo `requires_connection`, tuyệt đối không giả lập lời gọi.
4. Chọn Agent Role Core chỉ khi cần, không giả định Agent là một tiến trình riêng. Workflow chỉ thực thi qua runtime/automation thực được cho phép.
5. Read-only có thể làm theo quyền đang có; mọi write, credit, publish, dữ liệu nhạy cảm, thay OAuth cần quyền và phê duyệt đúng phạm vi.
6. Xác minh kết quả từ response/log; báo rõ `registry_linked`, `host_visible`, `tool_executed`, `e2e_verified`, `blocked` riêng biệt.
7. Đối với trùng Skill, sử dụng URI nguồn làm khóa định danh; không thay thế bản gốc hay tăng bộ đếm Core Skill nội bộ.

## Đảm bảo tương thích
Giữ nguyên 7 Skill gốc, 128 hồ sơ Agent, 108 mã học tập, Core 16 cụm, các phiên bản và thiết lập plugin khác. Không tự cài ứng dụng hoặc chạy agent nền. Core điều phối theo tác vụ trong phiên nơi các tool được cấp quyền; không thể tự gọi tool ngoài những công cụ host hiện diện.

## Kiểm toán
Trigger Accuracy: đúng intent/cụm; Context Bloat: chỉ đọc Skill liên quan; Logic Robustness: kiểm tra thiếu quyền và fallback; Safety: nguồn không tin cậy, least privilege; Format Compliance: trạng thái và bằng chứng chính xác. Skill không có mô tả đọc kiểm tra thực tế khi chạy nên mapping từ tên chỉ là bước đầu, không phải chứng nhận chuyên môn.

## Chú ý định danh cụm Core
Bảng `EXTERNAL_16_CLUSTER_REGISTRY.json` dùng phân nhóm nghiệp vụ riêng, **không phải** 16 ID cụm gốc trong `CLUSTER_16_ASSET_REGISTRY.json`. Khi điều phối Agent/Workflow, phải đọc `../agent-workflow-16-cluster-bridge/references/AGENT_WORKFLOW_16_CANONICAL.json`, đối chiếu lại nguồn Skill và lấy ID cụm gốc.
