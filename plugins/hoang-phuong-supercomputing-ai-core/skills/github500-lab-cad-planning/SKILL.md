---
name: github500-lab-cad-planning
description: "Dùng để thiết kế thông số và kiểm tra dung sai của phụ kiện in 3D, jig, giá đỡ, adapter hoặc thiết bị phòng thí nghiệm trước khi tạo STL."
---

# Github 500 — Lab Cad Planning

**Chế độ:** embedded_skill_guidance. **Nguồn phương pháp:** [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/lab-hardware-cad/SKILL.md). Không chạy mã hoặc gọi API ngoài theo mặc định.

## Thiết kế CAD có thể chế tạo
1. Chọn loại chi tiết (giá đỡ, fixture, enclosure, mount, adapter, rack), môi trường làm việc, tải trọng, kích thước bản in và vật liệu.
2. Ghi kích thước giao tiếp lấy từ bản vẽ hãng, tiêu chuẩn hoặc phép đo người dùng. **Không đoán kích thước lắp ghép** từ trí nhớ; ghi min/max tolerance và clearance.
3. Phác thảo tham số CAD, đơn vị mm, độ dày, vùng chịu lực, hole pattern, khả năng hỗ trợ in FDM và hạn chế anisotropy.
4. Phân biệt CAD hình học với FEA/CFD và đánh giá an toàn vật liệu: Skill không chứng nhận thiết bị y tế/thiết bị chịu lực.
5. Đề xuất test hình học: watertight/manifold, kích thước bounding box, giao thoa, tolerance stack, độ dày tường, overhang, fit test thực tế.
6. Nếu tool tạo CAD thực tế hiện hữu và được phép, sinh mô hình STL/STEP/3MF rồi mở lại kiểm tra. Nếu không có, giao đặc tả thiết kế và hướng dẫn dùng công cụ có sẵn; không nói đã xuất STL khi chưa có file.
7. Trước in hàng loạt, ưu tiên mẫu thử nhỏ và đo lại kích thước thực tế.

Không cài `build123d`, OpenCascade, không thực thi model Python từ GitHub hoặc khởi động printer khi chưa được yêu cầu. Kiểm tra license và tình trạng source trước khi chuyển mô hình.

## Kiểm tra bằng chứng và tích hợp
Đây là Skill hướng dẫn đã viết lại cho ChatGPT; các đoạn mã ở repo gốc và công cụ tùy chọn **không** được sao chép, cài hay chạy. Không đọc 500 hồ sơ cùng lúc. Khi cần, liên kết chuyên gia Core và các Skill khác theo tác vụ.

Xem `references/PROVENANCE.md`.
