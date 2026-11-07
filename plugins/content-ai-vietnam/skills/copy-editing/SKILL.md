---
name: copy-editing
description: Dùng khi đã có bản nháp cần rà lỗi, làm rõ, giữ giọng văn hoặc cập nhật nội dung cũ.
metadata:
  source_version: 2.2.1
  verified_on: 2026-11-02
---

# Copy Editing — biên tập nội dung

## Vai trò

Cải thiện bản nháp mà không làm mất thông điệp, giọng văn hoặc ý định của người viết. Mỗi sửa đổi phải có lý do cụ thể.

## Chọn mức biên tập

- **Bản trống/chung chung:** xây lại từ dữ kiện người dùng cung cấp và chỉ rõ chỗ thiếu.
- **Có giọng và lập luận riêng:** giữ góc nhìn, cách nói và điểm nhấn; chỉnh phần làm giảm độ rõ hoặc thuyết phục.
- **Sửa một điểm:** chỉ chỉnh câu/từ được yêu cầu và phần tối thiểu liên quan. Không biên tập toàn bài.

## Bảy lượt rà soát cho bản cần chỉnh đầy đủ

1. **Rõ nghĩa:** câu có dễ hiểu, cụ thể, đủ bối cảnh không?
2. **Giọng điệu:** có nhất quán với người viết và thương hiệu không?
3. **Ý nghĩa:** người đọc hiểu vì sao thông tin này đáng quan tâm không?
4. **Bằng chứng:** tuyên bố nào cần nguồn hoặc điều kiện?
5. **Cụ thể:** có thể thay từ chung chung bằng chi tiết thật không?
6. **Cảm xúc:** mức cảm xúc có phù hợp và trung thực không?
7. **Rủi ro:** có mơ hồ, gây hiểu nhầm, sai chính tả, hoặc lời hứa vượt bằng chứng không?

Sau khi sửa, đọc lại để bảo đảm một chỉnh sửa không làm hỏng điểm đã đạt ở lượt trước.

## Đầu ra

Với bài đầy đủ, đưa bản đã chỉnh và ghi chú ngắn những thay đổi quan trọng. Với sửa một điểm, chỉ trả về dòng mới và lý do. Đánh dấu riêng phần cần chủ sở hữu thương hiệu xác nhận.

## Lưu ý

Không “làm cho hay” bằng cách thay mọi câu bằng giọng AI. Không đổi sự thật, ý kiến, đại từ, độ thân mật hay mức cam kết nếu người dùng chưa cho phép.

## Prompt bắt đầu

> Hãy biên tập nội dung sau theo hướng dẫn Copy Editing. Chọn đúng mức: [rà toàn bài / giữ giọng người viết / sửa đúng một điểm]. Độc giả và giọng văn: [mô tả]. Giữ nguyên các dữ kiện. Trả bản đã sửa cùng lý do ngắn; đánh dấu tuyên bố cần kiểm chứng, không tự điền thông tin.

**Nguồn đối chiếu:** [Skill copy-editing của kho gốc](https://github.com/coreyhaines31/marketingskills/blob/main/skills/copy-editing/SKILL.md).

## Phối hợp trong bộ mở rộng

Với nhiều đầu ra liên quan, dùng [brief chung](../../references/content-brief.md) và giữ nhất quán dữ kiện, giọng văn, CTA. Với tuyên bố cần kiểm chứng, dùng [sổ bằng chứng](../../references/evidence-ledger.md). Chỉ khi người dùng giao chiến dịch nhiều bước, đọc [điều phối nội dung](../content-orchestrator/SKILL.md); không mở rộng một yêu cầu nhỏ thành chiến dịch.
