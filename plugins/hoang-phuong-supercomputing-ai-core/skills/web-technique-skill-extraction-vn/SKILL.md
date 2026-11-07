---
name: web-technique-skill-extraction-vn
description: "Dùng khi đã có hiệu ứng giao diện web hoạt động và muốn bóc tách một cơ chế kỹ thuật thành Skill tái sử dụng, có bản demo và bằng chứng kiểm chứng. Không dùng thay skill thiết kế UI từ số không."
---
# Bóc tách kỹ thuật web thành Skill có bằng chứng

**Loại:** Quy trình hướng dẫn độc lập bằng prompt, không chứa mã hoặc runtime upstream. **Nguồn:** MengTo/Skills, skill web-technique-to-skill tại commit ghim; giấy phép MIT. Xem `references/PROVENANCE.md` và `references/UPSTREAM_LICENSE_MIT.txt`.

## Kích hoạt và ranh giới
Dùng khi người dùng sở hữu hoặc được phép phân tích một triển khai web đã chạy và muốn chuyển kinh nghiệm về một hiệu ứng CSS/DOM/Canvas/WebGL/Three.js/animation thành Skill. Không coi mockup hay mô tả marketing là bằng chứng chạy thực. Không sao chép giao diện, thương hiệu, ảnh hay đoạn mã của bên thứ ba không có quyền. Không chạy mã ngoài hoặc gọi trình duyệt khi không có quyền.

## Quy trình độc lập
1. **Khóa phạm vi:** ghi URL/tệp tham chiếu có quyền, mục tiêu tương tác, môi trường, kích thước màn hình và hành vi cần bảo toàn; mô tả cơ chế bằng một câu phản chứng: thiếu gì thì hiệu ứng biến mất.
2. **Xác minh stack:** đọc import/cấu hình nguồn hoặc dấu hiệu runtime để phân biệt DOM/CSS, Canvas 2D, WebGL/GLSL, Three.js, GSAP; nếu không có bằng chứng, ghi `NOT VERIFIED` chứ không đoán từ ảnh.
3. **Tách cơ chế khỏi sân khấu:** chia thành (a) thuật toán / state / timing / event, (b) màu sắc, typography, layout, hình ảnh demo, (c) chi tiết ngẫu nhiên. Chỉ (a) thuộc Skill; (b) chỉ được ở demo có quyền; (c) không chuyển.
4. **Mô tả ngưỡng và thất bại:** với mỗi quy tắc nêu điều kiện kích hoạt, giá trị/tham số thực tế nếu đã đo, failure mode và cách xác minh; không biến tính từ ‘mượt’, ‘nhẹ’ thành con số giả.
5. **Soạn Skill:** YAML `name`, `description` có trigger cụ thể; Inputs, Outputs, prerequisites, steps, guardrails, accessibility, performance budget, negative tests, licensing, limitations; chỉ dẫn link tới minh họa, không đặt cú pháp chạy tự động.
6. **Bộ kiểm chứng:** một demo cô lập cho cơ chế và một đối chiếu giữa demo với nguồn được phép; test kích thước, interaction, keyboard/reduced-motion, lỗi không hỗ trợ, performance. Nếu không có browser/runtime, đánh dấu `UNTESTED`.
7. **Cổng phát hành:** đối chiếu trùng Skill hiện hữu; kiểm tra bằng chứng thực nghiệm, liên kết tham chiếu, license/attribution, rollback. Chỉ công nhận đã kiểm thử khi có log/screenshot/test thực.

## Đầu ra
Bảng `Mechanism | Verified stack | Inputs | Parameters / assumptions | Failure modes | Demo evidence | License | Status`, một SKILL.md nháp và checklist nghiệm thu. Bàn giao kết quả là hướng dẫn; việc triển khai demo, cài package hoặc publish cần quyền riêng.

## Không trùng lặp
Khác `github500-workflow-design` (workflow tự động hóa chung), `github500-prompt-refiner` (chỉnh prompt) và `addy-frontend-ui-engineering` (xây giao diện); trọng tâm ở đây là **trích xuất cơ chế từ một hiệu ứng web đã chạy và kiểm chứng tính tái sử dụng**.
