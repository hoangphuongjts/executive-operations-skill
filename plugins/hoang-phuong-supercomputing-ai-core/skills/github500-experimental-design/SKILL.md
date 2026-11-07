---
name: github500-experimental-design
description: "Dùng khi cần thiết kế thực nghiệm khoa học, nghiên cứu nông nghiệp, sản xuất hoặc sản phẩm với randomization, replication, blocking, DOE và đánh giá sai lệch; không thay thế giám sát chuyên môn."
---

# GitHub 500 — Thiết kế thực nghiệm khoa học (thí điểm v14.6)

Biên soạn lại nguyên tắc từ `experimental-design` (K-Dense-AI/scientific-agent-skills, MIT). Tập trung **thiết kế bằng ngôn ngữ tự nhiên** và kiểm tra cấu trúc, không tự chạy Python. Nguồn và phạm vi ở `references/PROVENANCE.md`.

## Quy trình thiết kế
1. Xác định câu hỏi, giả thuyết có thể bị bác bỏ, tiêu chí đo, đơn vị thực nghiệm và đơn vị quan sát; không đánh đồng số đo lặp của một đơn vị với số mẫu độc lập.
2. Lập danh sách yếu tố tác động và yếu tố gây nhiễu (lô, ngày, địa điểm, nguyên liệu, thời tiết, nhân sự); thiết kế control thích hợp.
3. Chọn thiết kế bằng lập luận:
   - So sánh ít nhóm: random allocation hoặc randomized block nếu có nhóm đồng nhất.
   - Nhiều yếu tố: full hoặc fractional factorial theo khả năng chạy và câu hỏi interaction.
   - Tối ưu nhiều mức liên tục: response surface; phải kiểm soát giới hạn an toàn của biến.
   - Nhóm/cụm không thể phân tách: cluster randomized; phân tích theo đơn vị cụm.
   - Đo lặp/crossover: kiểm tra carryover, washout, correlation và thứ tự.
4. Xác định số lần lặp **độc lập**, cân bằng nhóm, seed và nguyên tắc che giấu phân bổ khi phù hợp; seed không thay thế kiểm soát thiên lệch.
5. Soạn bảng kế hoạch: run ID, block, treatment, randomization, mẫu và người thực hiện, đầu ra, tiêu chí loại trừ định trước, nguồn dữ liệu.
6. Kiểm tra power/cỡ mẫu và độ tin cậy bằng công cụ thống kê đã được người dùng cung cấp hoặc phê duyệt. Nếu không có thông số biến thiên/hiệu ứng thì không tự cho con số.
7. Giả định độc lập, nhiễu đo, pseudoreplication, multiple comparisons, missingness, attrition, extreme values và tính tái lập. Mọi thử nghiệm y tế/vật nuôi yêu cầu giám sát đạo đức/an toàn theo quy định.

## Mẫu kết quả
- Câu hỏi & endpoint: ...
- Biến độc lập & mức: ...
- Đơn vị thực nghiệm, số nhóm, block, control: ...
- Quy tắc phân bổ: ...
- Dữ liệu và biểu mẫu kiểm soát chất lượng: ...
- Phân tích dự kiến: ...
- Phản ví dụ, nhiễu, giới hạn: ...
- Cỡ mẫu/power: CHƯA TÍNH nếu thiếu dữ liệu

**Không tự ý làm thực nghiệm lâm sàng hoặc điều khiển thiết bị.** Các script Python/NumPy/pydoe trong repo nguồn **chưa được cài/chạy** và phải qua kiểm toán phụ thuộc riêng.
