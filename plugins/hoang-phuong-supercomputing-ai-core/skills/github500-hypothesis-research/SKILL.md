---
name: github500-hypothesis-research
description: "Dùng khi xây giả thuyết khoa học có khả năng bác bỏ, thiết kế phép thử đối chứng và phân biệt dự đoán với chứng cứ."
---

# Github 500 — Hypothesis Research

**Chế độ:** embedded_skill_guidance. **Nguồn phương pháp:** [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/hypothesis-generation/SKILL.md). Không chạy mã hoặc gọi API ngoài theo mặc định.

## Quy trình khoa học
1. Ghi quan sát gốc, nguồn, thời gian, đối tượng, đơn vị đo, dữ liệu thiếu và những gì chỉ mới là suy luận.
2. Đặt câu hỏi có phạm vi đo lường được; định nghĩa biến đầu ra, nhóm so sánh, đơn vị thử nghiệm và rủi ro đạo đức.
3. Xây ít nhất hai giả thuyết cạnh tranh khi có cơ sở, trong đó xét sai số đo, nhiễu, đảo chiều nhân quả hoặc lựa chọn mẫu.
4. Đối với mỗi giả thuyết, viết **dự đoán quan sát được**, phương pháp bác bỏ, biến cần đo, negative control, kết quả có thể làm thay đổi kết luận.
5. Phân biệt nghiên cứu khám phá với nghiên cứu xác nhận; không gán từ “chứng minh” khi chỉ có tương quan.
6. Tra cứu tài liệu đã cấp phép khi có công cụ, ghi ranh giới ngày và truy vấn; không tuyên bố “chưa từng ai nghiên cứu” khi chưa tìm kiếm đầy đủ.
7. Kết luận bằng bảng hypothesis | predictions | evidence | counterevidence | test | status.

Trong sức khỏe, động vật, môi trường hay thử nghiệm trên người, ghi rõ điều kiện chuyên gia và đánh giá đạo đức. Không đưa chỉ dẫn thử nghiệm nguy hiểm.

## Kiểm tra bằng chứng và tích hợp
Đây là Skill hướng dẫn đã viết lại cho ChatGPT; các đoạn mã ở repo gốc và công cụ tùy chọn **không** được sao chép, cài hay chạy. Không đọc 500 hồ sơ cùng lúc. Khi cần, liên kết chuyên gia Core và các Skill khác theo tác vụ.

Xem `references/PROVENANCE.md`.
