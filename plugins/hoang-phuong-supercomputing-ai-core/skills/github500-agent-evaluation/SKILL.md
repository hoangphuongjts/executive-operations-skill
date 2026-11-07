---
name: github500-agent-evaluation
description: "Dùng khi thiết kế benchmark, đánh giá chất lượng trả lời của AI Agent, kiểm thử đối chứng, rubric độc lập và quy trình cải tiến có bằng chứng."
---

# Github 500 — Agent Evaluation

**Chế độ:** embedded_skill_guidance. **Nguồn phương pháp:** [github/awesome-copilot](https://github.com/github/awesome-copilot/blob/main/skills/agentic-eval/SKILL.md). Không chạy mã hoặc gọi API ngoài theo mặc định.

## Quy trình đánh giá theo bằng chứng
1. Xác định tác vụ, expected outcome, ràng buộc an toàn và dữ liệu đánh giá. Tách tập thiết kế, tập tuning và **tập kiểm thử giữ kín**.
2. Lập bộ test có ca đúng, ca sai, thiếu dữ liệu, yêu cầu mâu thuẫn và dữ liệu độc hại. Không xem điểm tự chấm của cùng model là chứng nhận độc lập.
3. Chọn rubric cân bằng accuracy, citation quality, robustness, safety, format, latency/chi phí; giải thích trọng số.
4. Với câu hỏi kiểm tra được, ưu tiên exact-match, execution test, golden answer và human review hơn LLM-as-judge đơn lẻ. Thống kê chất lượng theo từng nhóm và khoảng bất định nếu mẫu đủ.
5. Vòng cải thiện có giới hạn: Draft → Evaluate → Critique → Revise (tối đa 2 vòng theo mặc định); đóng băng prompt và rubric khi đánh giá ngoại mẫu.
6. Kiểm tra rò rỉ dữ liệu đánh giá, tính lặp lại, sai lệch giám khảo và nguy cơ “tối ưu điểm rubric” nhưng không đạt mục tiêu thật.
7. Báo cáo count pass/fail, từng test ID, môi trường, model/version, seed (nếu có), trace nguồn, ai là người đánh giá, trạng thái triển khai.

**Nhãn kết quả**: `evaluation_plan_only`, `offline_test_executed`, `model_self_review`, `independent_human_reviewed`. Không ghi số liệu khi chưa chạy test; không suy diễn năng lực giáo sư/tiến sĩ từ điểm phần mềm.

## Kiểm tra bằng chứng và tích hợp
Đây là Skill hướng dẫn đã viết lại cho ChatGPT; các đoạn mã ở repo gốc và công cụ tùy chọn **không** được sao chép, cài hay chạy. Không đọc 500 hồ sơ cùng lúc. Khi cần, liên kết chuyên gia Core và các Skill khác theo tác vụ.

Xem `references/PROVENANCE.md`.
