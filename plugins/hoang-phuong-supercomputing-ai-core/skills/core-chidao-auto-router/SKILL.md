---
name: core-chidao-auto-router
description: "Kích hoạt đồng thời hoangphuong-v16-active và chidao khi người dùng gọi @hoangphuong-supercomputing-core hoặc mở Core qua liên kết; điều phối nhiệm vụ mà không cần gõ /chidao."
---

# Hoàng Phương Core → tự áp dụng chidao

## Điều kiện kích hoạt
Khi người dùng mở plugin Hoàng Phương Core và gửi yêu cầu, hoặc nhắc `@hoangphuong-supercomputing-core`, áp dụng đồng thời hướng dẫn `../hoangphuong-v16-active/SKILL.md` và **nguyên văn** `../chidao/SKILL.md`. Không cần người dùng thêm `/chidao`.

## Quy trình
1. Hiểu mục tiêu, ràng buộc, độ phức tạp theo ba mức trong `/chidao`; lựa chọn chế độ phù hợp, tránh chia vụn một việc đơn giản.
2. Main Agent là Kiến Trúc Sư Trưởng: xác định mục tiêu, cụm chuyên môn, file/Neo Hồng Tâm và kiểm tra quyền.
3. Với nhiều nhiệm vụ độc lập, định tuyến Chuyên Viên tên rõ ràng, cùng một file không giao đồng thời cho nhiều người sửa; chỉ gọi Subagent thực khi có công cụ và quyền. Nếu không, tự thực hiện lần lượt và nói rõ không có Agent độc lập.
4. Khi sửa code, đọc file, nhắm đúng Semantic Anchor, giữ backward compatibility, kiểm tra thực tế và báo diff thật nếu có.
5. Nghiệm thu theo 5 cổng Core (Trigger Accuracy, Context Bloat, Logic Robustness, Safety, Format Compliance) và rubric `/chidao`; chỉ chấm PASS khi có bằng chứng.

## Ranh giới
- Đây là cơ chế hướng dẫn điều phối, không phải lời hứa tự mở Gemini/Argon/Opus, tự phê duyệt, thực thi bất đồng bộ hay cắt giảm 98% chi phí.
- Giữ nguyên `skills/chidao/SKILL.md` và các thành phần cũ: 16 cụm, 128 Agent Role, 108 mã học tập; giữ nguyên quyền và người phê duyệt.
- Skill gốc vẫn có thể gọi trực tiếp bằng `/chidao`.

## Bộ mã học tập 108 gốc và trình tra cứu (bổ sung)
- Khi người dùng gọi Core kèm mã học tập `/...`, sử dụng hướng dẫn chi tiết trong `references/STUDY_108_ROUTING.md`; tra đúng `STUDY_108_BASELINE.json` trước khi thực thi.
- Không đổi tên, chức năng, thứ tự 108 mã gốc; không tính `/chidao` là mã thứ 109.
- Với tiền tố `/g`, `/m`, v.v., chỉ gợi ý các mã gốc bắt đầu bằng tiền tố; với mã đầy đủ, thực hiện ngay và kết hợp chidao để kiểm soát quy trình.
- Có bảng HTML offline trong `skills/hoangphuong-supercomputing-core/references/STUDY_108_DASHBOARD.html`; không gọi bảng offline là web app đã deploy.
