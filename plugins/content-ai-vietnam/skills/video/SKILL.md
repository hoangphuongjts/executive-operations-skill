---
name: video
description: Dùng khi cần ý tưởng, cấu trúc, lời thoại, danh sách cảnh quay hoặc phương án sản xuất video marketing.
metadata:
  source_version: 2.4.0
  verified_on: 2026-11-02
---

# Video — ý tưởng và kịch bản video

## Vai trò

Giúp chọn cách thể hiện video theo mục tiêu và nguồn lực: người dẫn hình, lời đọc, quay sản phẩm, quay màn hình, tư liệu sẵn có, công cụ tạo hình hoặc dựng theo mẫu. Có thể chuẩn bị kịch bản mà chưa cần chọn công cụ dựng.

## Quy trình

1. Xác định mục tiêu, người xem, nền tảng, thời lượng, lời kêu gọi hành động và điều khán giả cần nhớ.
2. Kiểm kê tư liệu thật, người có thể xuất hiện, khả năng ghi âm/quay, thời gian và ngân sách.
3. Chọn cách sản xuất phù hợp. Giải thích đánh đổi giữa quay thật, tái sử dụng tư liệu, công cụ tạo sinh và dựng theo mẫu.
4. Viết hook, các cảnh theo thứ tự, lời thoại/voice-over, chữ trên màn hình, chỉ dẫn hình ảnh/âm thanh và CTA.
5. Kiểm tra lời thoại với dữ kiện được cung cấp; ghi rõ cảnh nào cần quay hoặc tư liệu nào cần xin.
6. Nếu yêu cầu có dựng bằng mã hoặc công cụ AI, mô tả yêu cầu và điều kiện trước. Không chạy mã, tải tiện ích hay tiêu ngân sách nếu chưa được yêu cầu rõ.

## Đầu ra

- Mục tiêu, định dạng, thời lượng và cách sản xuất.
- Bảng phân cảnh: thời gian, hình, lời thoại, chữ và âm thanh.
- Danh sách tư liệu/thiết bị cần chuẩn bị.
- Ghi chú kiểm chứng và phiên bản công cụ cần xác minh trước khi triển khai.

## Lưu ý

Không trình bày video AI hoặc cảnh minh họa như tư liệu thật. Không tự khẳng định giá, quyền sử dụng hay khả năng hiện tại của công cụ video; kiểm tra tài liệu chính thức trước khi chọn. Kỹ năng này viết kế hoạch/kịch bản, không tự render hoặc xuất bản video.

## Prompt bắt đầu

> Hãy làm theo hướng dẫn Video này. Tôi cần video [mục tiêu] cho [kênh], dài khoảng [thời lượng]. Người xem là [ai]. Tư liệu và ngân sách hiện có: [liệt kê]. Hãy đề xuất cách sản xuất và viết bảng phân cảnh gồm thời gian, hình, lời thoại, chữ trên màn hình và CTA. Không thêm lời khẳng định chưa được chứng minh.

**Nguồn đối chiếu:** [Skill video của kho gốc](https://github.com/coreyhaines31/marketingskills/blob/main/skills/video/SKILL.md).

## Phối hợp trong bộ mở rộng

Với nhiều đầu ra liên quan, dùng [brief chung](../../references/content-brief.md) và giữ nhất quán dữ kiện, giọng văn, CTA. Với tuyên bố cần kiểm chứng, dùng [sổ bằng chứng](../../references/evidence-ledger.md). Chỉ khi người dùng giao chiến dịch nhiều bước, đọc [điều phối nội dung](../content-orchestrator/SKILL.md); không mở rộng một yêu cầu nhỏ thành chiến dịch.

## Giọng đọc local miễn phí
Khi cần tạo lời đọc, clone từ file được phép hoặc dịch vụ hết credits, đọc [free-voiceover](../free-voiceover/SKILL.md) và dùng adapter có kiểm tra quyền. Đây là luồng bổ sung, không chứng minh engine đã cài hay chạy. Với video bắt buộc có lời đọc, thiếu giọng phải báo bản nháp chưa hoàn chỉnh; không tự coi nhạc và chữ thay cho lời đọc đã yêu cầu.

Với video Tò Mò Lab, ưu tiên preset Adam vidIQ đã dùng trước đây theo cấu hình trong [hướng dẫn Adam](../free-voiceover/references/TO_MO_LAB_ADAM.md). Kiểm tra catalog và quota trước khi gọi; nếu unavailable thì để lời đọc chờ, không tự thay sang voice khác.
Nếu muốn dùng Adam từ một TTS khác, kiểm tra [bảng tương thích catalog](../free-voiceover/references/ADAM_PORTABILITY.md); chỉ route khi exact voice ID được xác nhận ở công cụ đó.
