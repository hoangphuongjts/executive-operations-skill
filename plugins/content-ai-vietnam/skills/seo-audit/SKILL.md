---
name: seo-audit
description: Dùng khi cần rà soát SEO cho website/trang đã tồn tại và có thể truy cập hoặc có dữ liệu kiểm tra.
metadata:
  source_version: 2.2.2
  verified_on: 2026-11-02
---

# SEO Audit — rà soát SEO website

## Vai trò

Tìm vấn đề có thể kiểm chứng trên trang web, giải thích mức độ ảnh hưởng và đề xuất việc sửa theo thứ tự. Cần URL, phạm vi kiểm tra và nếu có thì dữ liệu Search Console/analytics hoặc kết quả crawl.

## Quy trình

1. Xác nhận loại website, mục tiêu kinh doanh, nhóm truy vấn, phạm vi trang và thay đổi gần đây.
2. Kiểm tra khả năng truy cập/lập chỉ mục: robots, sitemap, canonical, điều hướng và trang mồ côi khi có dữ liệu phù hợp.
3. Rà nền tảng kỹ thuật, tốc độ, thiết bị di động, bảo mật và cấu trúc URL dựa trên bằng chứng có thể xem được.
4. Rà nội dung trên trang: tiêu đề, mô tả, heading, ý định tìm kiếm, liên kết nội bộ, hình ảnh và mức độ hữu ích.
5. Với website đa ngôn ngữ/địa phương, kiểm tra cấu trúc ngôn ngữ và tín hiệu phiên bản khu vực nếu phạm vi liên quan.
6. Xếp phát hiện theo tác động, độ tin cậy của bằng chứng và công sức sửa. Phân biệt lỗi chắc chắn với giả thuyết cần thêm dữ liệu.
7. Ghi cách kiểm tra lại sau khi sửa.

## Đầu ra

Bảng gồm phát hiện, bằng chứng/URL, mức ưu tiên, khuyến nghị, công sức ước tính và cách kiểm tra lại. Nêu rõ giới hạn công cụ hoặc trang không truy cập được.

## Lưu ý

Không kết luận website bị lỗi nếu chưa xem được dữ liệu hỗ trợ. HTML tĩnh có thể bỏ lỡ dữ liệu có cấu trúc được chèn bằng JavaScript; không báo “không có schema” chỉ dựa trên một bản tải tĩnh. Hãy đối chiếu hướng dẫn Google hiện hành cho quy tắc có thể thay đổi. Nếu chưa có website, dùng Content Strategy hoặc Copywriting thay vì tạo một báo cáo SEO giả.

## Prompt bắt đầu

> Hãy rà soát SEO theo hướng dẫn này. Website/trang: [URL]. Phạm vi: [toàn site / danh sách trang]. Mục tiêu và truy vấn ưu tiên: [nêu]. Dữ liệu có sẵn: [Search Console, analytics, crawl hoặc chưa có]. Chỉ đưa ra phát hiện có bằng chứng; tách việc đã xác minh khỏi giả thuyết và đề xuất cách xác nhận tiếp.

**Nguồn đối chiếu:** [Skill seo-audit của kho gốc](https://github.com/coreyhaines31/marketingskills/blob/main/skills/seo-audit/SKILL.md).

## Phối hợp trong bộ mở rộng

Với nhiều đầu ra liên quan, dùng [brief chung](../../references/content-brief.md) và giữ nhất quán dữ kiện, giọng văn, CTA. Với tuyên bố cần kiểm chứng, dùng [sổ bằng chứng](../../references/evidence-ledger.md). Chỉ khi người dùng giao chiến dịch nhiều bước, đọc [điều phối nội dung](../content-orchestrator/SKILL.md); không mở rộng một yêu cầu nhỏ thành chiến dịch.
