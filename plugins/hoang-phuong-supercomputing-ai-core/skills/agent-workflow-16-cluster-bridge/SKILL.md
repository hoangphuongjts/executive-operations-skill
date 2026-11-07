---
name: agent-workflow-16-cluster-bridge
description: "Định tuyến 128 Agent Role, 16 workflow bản thiết kế và 181 Skill nguồn vào 16 cụm gốc; bản 16.0.41 có hợp đồng kiểm thử ngoại tuyến và cổng quyền mặc định đóng."
---

# Agent & Workflow Bridge v16.0.41

- Nguồn chính: `references/AGENT_WORKFLOW_16_CANONICAL.json` và `references/STAGING_RUNTIME_POLICY.json`.
- **Dùng đúng 16 cụm Core gốc** theo `CLUSTER_16_ASSET_REGISTRY.json`, không dùng số thứ tự 16 nhãn nghiệp vụ trước đây.
- 128 role profiles vẫn ở vị trí gốc; đề xuất một tập nhỏ vai trò liên quan trong workflow, không coi role là process riêng.
- Các mục Skill là liên kết federated, chưa sao chép source và không tự cấp quyền hoặc kích hoạt plugin.
- Đọc Skill nguồn khi truy cập được để xác thực chuyên môn. Các mapping được xem là `review_candidate`, không phải semantic certified. Khi source mơ hồ, dừng để rà soát.
- `offline_router.py` là mô phỏng hợp đồng thuần Python **không có runtime thực**, không có hành động ghi, mạng hay API.
- Với yêu cầu mới: xác định đầu vào, chọn đúng cụm và workflow, kiểm tra quyền và chi phí rồi định tuyến đến công cụ thực sự hiện diện của ChatGPT nếu host cho phép. Không dùng module offline để gọi tool thật.
- Giao dịch ghi, xuất bản, mua dịch vụ, sửa OAuth, chạy secret hay production chỉ thực hiện sau phê duyệt riêng và xác minh host runtime; mặc định fail-closed.
- Bản lưu Core hiện hữu phải được giữ nguyên; không xóa Skill, ID, registry, role profile, 108 mã học tập, OAuth hoặc dữ liệu gốc.
- Đầu ra phân biệt: `SOURCE_VISIBLE`, `METADATA_PASS`, `MOCK_TEST_PASS`, `E2E_NOT_TESTED`, `BLOCKED`, `DEPLOYED` khi có chứng cứ thực.
