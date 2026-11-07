---
name: github500-research
description: "Dùng để tra cứu, phân loại, kiểm tra giấy phép, đánh giá và đề xuất tích hợp repository GitHub đa lĩnh vực vào Hoangphuong Supercomputing Core. Catalog 500 repo là kết quả khám phá, chưa phải 500 bản cài; không tự chạy script bên ngoài."
---

# Github 500 Research — Skill tra cứu và đánh giá repository đa ngành

Đây là **Skill gốc mới, do người vận hành Core tạo từ quy trình kiểm kê**, không phải mã sao chép từ 500 repository. Dùng danh mục tại `../hoangphuong-supercomputing-core/references/GITHUB_500_MASTER_CATALOG.json` và quy định tại `../hoangphuong-supercomputing-core/references/GITHUB_500_SOURCE_POLICY.md`.

1. Khi người dùng cần công cụ, nhận diện lĩnh vực và mục tiêu; tìm trong catalog (không tải toàn bộ 500 hồ sơ vào ngữ cảnh). Danh mục ghi nguồn GitHub và lĩnh vực theo *truy vấn tìm kiếm*, không chứng nhận phù hợp thực tế.
2. Đề xuất tối đa 5 kết quả liên quan; xác minh từng URL, README, commit, giấy phép toàn bộ, dữ liệu/quyền và cấu trúc code bằng GitHub connector hiện có trước khi đánh dấu đủ điều kiện.
3. Gán trạng thái: `discovered_not_audited`, `license_metadata_checked`, `security_reviewed`, `packaged`, `verified_in_host`, `external_runtime_opt_in` — không nhảy cấp chỉ vì tồn tại repository.
4. Chỉ tải/cài/đưa mã về Core khi đủ giấy phép, kiểm tra prompt injection và mã phụ thuộc, không xung đột với Skill hiện có, được thử trong môi trường an toàn và có bằng chứng hợp lệ.
5. Giữ nguyên 7 Skill ban đầu, 128 agent, 16 cụm, Academy, runtime dự phòng và 108 mã slash gốc. Không tạo lệnh `/...` mới trùng tên hoặc thay đổi tên lệnh gốc.
6. Mặc định `embedded_skills_only`; không tự chạy Docker, server, endpoint AI, thanh toán hoặc script chưa duyệt. Chỉ gọi công cụ host đang thực sự khả dụng và được cấp phép.
7. Khi phù hợp, sử dụng 1–4 lăng kính agent Core, #32 phản biện và #64 tổng hợp. Tất cả thuộc một mô hình ChatGPT trừ khi có trace mô hình độc lập.
8. Kết quả phải báo số đã tìm, đã kiểm tra, đã tải, đã tích hợp và đã kiểm thử tách biệt. Không đồng nhất 500 catalog với 500 plugin/Skill chạy thật.

CLI offline tùy chọn (Python 3.10+), **không cần chạy khi chỉ đọc Skill**:

```
python skills/hoangphuong-supercomputing-core/scripts/github500_router.py report
python skills/hoangphuong-supercomputing-core/scripts/github500_router.py search --query agriculture
python skills/hoangphuong-supercomputing-core/scripts/github500_router.py pilot
```
