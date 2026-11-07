# Tích hợp 16 cụm và nguồn GitHub — Hướng dẫn vận hành

- Bản gốc quan sát: `hoang-phuong-supercomputing-ai-core` v16.0.4.
- Giữ nguyên 16 cụm gốc và ID 001–128, 7 Skill ban đầu, bản 108 mã slash, runtime, 29 Skill hiện tại và quyền plugin.
- 16 Skill bổ sung thuộc nhóm hướng dẫn nguyên bản, **không bao gồm mã bên thứ ba**.
- 1 Skill mới `core-16-cluster-router` dùng để định tuyến khi được gọi.
- Danh mục ánh xạ đa cụm; dùng primary_cluster để tránh tính trùng 24 Skill/cụm.
- Đã thu thập 384 lượt ứng viên từ GitHub (24/cụm) — TẤT CẢ cần kiểm toán trước khi chấp thuận.
- Nguồn bên ngoài chỉ là tham chiếu, không di chuyển package hoặc quyền OAuth của plugin khác.
- Khi có Skill mới: đọc metadata → định tuyến (hoặc review thủ công) → kiểm tra nguồn/giấy phép/an toàn → thử chức năng → cài qua công cụ chính thức → đọc lại → đếm vào chỉ tiêu.
- CLI: `python skills/hoangphuong-supercomputing-core/scripts/cluster_skill_router_v165.py validate`.
- Cảnh báo: chỉ chạy tự phân loại khi CLI được gọi. Không có background service trong ChatGPT.
- Rollback: sử dụng release gốc v16.0.4 từ lịch sử Plugin Creator; cần kiểm chứng thao tác khôi phục, không tự tuyên bố đã tạo bản sao vật lý.
