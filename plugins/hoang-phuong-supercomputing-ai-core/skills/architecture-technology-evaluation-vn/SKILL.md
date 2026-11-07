---
name: architecture-technology-evaluation-vn
description: "Đánh giá và chọn stack công nghệ cho hệ thống bằng ma trận 12 tiêu chí có trọng số, kịch bản chất lượng và ATAM; dùng khi cần so sánh ít nhất hai phương án trước khi lập ADR, không cài hoặc gọi CLI ANWS."
---
# Đánh giá lựa chọn công nghệ có bằng chứng (prompt-only)

**Loại**: kỹ năng hướng dẫn, không phải ANWS runtime hay công cụ tự cài. Kích hoạt khi người dùng yêu cầu chọn giữa >=2 công nghệ/stack dựa trên ràng buộc; không dùng thay cho `system-design-planning-vn` khi nhiệm vụ là thiết kế kiến trúc tổng thể, `architecture-documentation-arc42-vn` khi cần hồ sơ đầy đủ, hoặc `github500-architecture-blueprint` khi cần phân tích codebase.

## Đầu vào bắt buộc
- Chức năng/mục đích, yêu cầu chất lượng, khối lượng và quy mô hiện tại/dự báo.
- Kỹ năng đội ngũ, khả năng vận hành, chi phí sở hữu dài hạn (TCO), thời gian, tích hợp, tuân thủ, hạn chế đặc biệt.
- Có ít nhất **hai ứng viên được nêu tên**. Thiếu dữ liệu: ghi **[GIẢ ĐỊNH H-xx]**, câu hỏi cần xác minh và ảnh hưởng tới kết luận; không tự coi giả định là sự thật.

## Quy trình
1. **Chốt ranh giới và mục đích so sánh.** Tách tiêu chí loại trực tiếp (ví dụ bắt buộc triển khai on-premises, hạn chế giấy phép) khỏi tiêu chí có thể cân nhắc; đánh dấu chứng cứ và ngày xác minh thông tin thay đổi theo thời gian.
2. **Đối chiếu ít nhất hai ứng viên.** Chỉ chọn bản phát hành/framework đã có chứng cứ. Không dùng bảng điểm để hợp thức hóa ứng viên vi phạm hard constraints.
3. **Ma trận 12 chiều**, mỗi ứng viên điểm 1–5 hoặc `N/A + lý do` cho: (1) phù hợp chức năng; (2) khả năng mở rộng; (3) hiệu năng; (4) bảo mật/tuân thủ; (5) năng lực đội; (6) thị trường nhân lực; (7) tốc độ phát triển; (8) TCO; (9) hệ sinh thái; (10) bảo trì dài hạn; (11) tích hợp; (12) sẵn sàng AI (hoặc N/A có căn cứ). Công khai trọng số, dữ liệu dẫn chứng, cách tính và biên độ bất định; không tạo điểm số giả khi thiếu chứng cứ.
4. **Phân tích trade-off theo ATAM.** Đặt ít nhất một kịch bản thuộc tính chất lượng với tải, điều kiện, ngưỡng quan sát được; cho mỗi ứng viên: bằng chứng, tình huống thất bại, rủi ro, nhạy cảm với giả định; giải thích tại sao phương án hạng hai không được chọn.
5. **Giảm thiên lệch.** Tự chất vấn phương án dẫn đầu bằng 3–7 luận điểm phản chứng độc lập; kiểm tra khi thay đổi trọng số/giả định thì thứ hạng có đảo không; bổ sung phép thử POC phù hợp khi nguồn chưa đủ. Nếu cần công cụ chuyên biệt mà không có, ghi `CHƯA THỂ KIỂM CHỨNG` chứ không giả lập kết quả.
6. **Bản nháp quyết định cho ADR (chưa chấp nhận).** Xuất `Context`, `Drivers`, `Alternatives`, `Decision proposed`, `Consequences`, `Evidence / References`, `Scope of impact`, `Verification / tests`. Không ghi ADR `Accepted` hoặc thay đổi tệp dự án khi chưa có bước phê duyệt. Trong ANWS gốc, `/genesis` Step 3 chỉ tạo bảng so sánh, Step 5 mới ghi ADR; khi dùng ngoài ANWS cũng giữ ranh giới **đánh giá ≠ phê duyệt triển khai**.

## Đầu ra
- Bảng ràng buộc và giả định; 12 dòng × N phương án có trọng số và dẫn chứng (N>=2).
- Các kịch bản chất lượng, trade-off, rủi ro, phép thử và kiến nghị có điều kiện.
- Bảng chuyển tiếp vào ADR, phương án thứ hai cùng lý do loại, điều kiện làm thay đổi quyết định.
- Kết luận được phân loại `đủ chứng cứ` / `cần đo đạc` / `bị loại do ràng buộc`.

## Cổng nghiệm thu
- Không khẳng định số đo/benchmark thực nếu chưa kiểm chứng; không suy diễn khả năng bảo mật từ tên công nghệ.
- Mỗi điểm cao/thấp có nguồn hoặc lý do được ghi; tổng điểm tính lại được; chênh lệch trọng số được kiểm tra.
- Các hạng mục thiếu nguồn không được biến thành khuyến nghị chắc chắn.
- Không chạy `anws`, Node.js, `sequential-thinking` CLI, script, install/update hoặc tự ghi/xóa thư mục `.anws/`.

## Provenance và giới hạn
Chuyển thể prompt-only từ `Haaaiawd/ANWS` (MIT), commit `3f3d9116aa3be07fc7f8a5c26d996d60323c0b95`, phần `src/anws/templates_en/.agents/skills/tech-evaluator/SKILL.md` và `references/ADR_TEMPLATE.md`. Thực hành lập luận 3–7 điểm thay cho phụ thuộc vào CLI `sequential-thinking` là điều chỉnh **được công bố**, không sao chép nguyên xi workflow `/genesis`. Ranh giới không tạo ADR sớm, ma trận 12 tiêu chí, ATAM, yêu cầu chứng cứ và test tiers được giữ. Xem `references/PROVENANCE.md` và `references/UPSTREAM_LICENSE_MIT.txt`.
