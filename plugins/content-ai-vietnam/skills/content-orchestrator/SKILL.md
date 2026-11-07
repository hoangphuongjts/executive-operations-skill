---
name: content-orchestrator
description: Điều phối chiến dịch nội dung nhiều bước hoặc nhiều định dạng từ nghiên cứu đến đo lường. Dùng khi cần quy trình tổng thể; một bài riêng lẻ dùng skill viết tương ứng.
---

# Điều phối Content AI Việt Nam

Xác định kết quả cần bàn giao, người xem, kênh và nguồn lực thực tế. Không bắt người dùng hoàn thành toàn bộ biểu mẫu trước một yêu cầu đơn giản. Đọc [brief chung](../../references/content-brief.md) khi công việc có nhiều đầu ra; dùng một brief đã thống nhất xuyên suốt, chỉ hỏi thông tin thật sự chặn việc.

## Chọn chuyên môn
- Chưa hiểu người xem: [audience-research](../audience-research/SKILL.md).
- Cần giọng riêng: [brand-voice](../brand-voice/SKILL.md).
- Chọn chủ đề, trụ cột: [content-strategy](../content-strategy/SKILL.md).
- Chiến dịch có thời hạn: [campaign-planning](../campaign-planning/SKILL.md).
- Trang bán hàng: [copywriting](../copywriting/SKILL.md); quảng cáo trả phí: [ad-creative](../ad-creative/SKILL.md).
- Bài mạng xã hội: [social](../social/SKILL.md); kịch bản: [video](../video/SKILL.md).
- Câu chuyện sản phẩm địa phương: [product-storytelling](../product-storytelling/SKILL.md).
- Tái sử dụng tư liệu: [content-repurposing](../content-repurposing/SKILL.md).
- Biên tập: [copy-editing](../copy-editing/SKILL.md); website đang hoạt động: [seo-audit](../seo-audit/SKILL.md).
- Có số liệu: [content-performance](../content-performance/SKILL.md).

Chỉ đọc nhánh liên quan. Một người viết có thể thực hiện các vai trò; không giả rằng đã gọi nhiều agent. Với dự án lớn, nêu đầu vào, phụ thuộc và tiêu chí nghiệm thu cho từng nhánh, rồi kiểm tra tính nhất quán giữa chúng.

## Thực hiện và bàn giao
Dùng bằng chứng chung theo [sổ bằng chứng](../../references/evidence-ledger.md). Giữ cùng mã nội dung khi chuyển từ ý tưởng sang bản nháp và báo cáo. Mã là định danh tài liệu, không phải bản ghi đã tự động lưu.
Kiểm tra lời hứa, giá, CTA, thời hạn và giọng văn giữa các kênh. Hoàn thành đầu ra được giao, kèm phần thiếu dữ liệu có ảnh hưởng và cách đo phù hợp. Không biến mọi yêu cầu thành một chiến dịch lớn.

Plugin này cung cấp hướng dẫn và tài liệu; không kèm backend, bộ lập lịch hoặc kết nối dữ liệu. Tìm công cụ thật khi nhiệm vụ cần, đọc hướng dẫn chuyên biệt và xác minh kết quả. Việc nâng cấp plugin không cho phép tự đăng, gửi tin hay chi tiền.

## Phối hợp phản biện với bộ đồng hành

Khi Hoàng Phương gọi cả Trợ Lý Xây Kênh và Content AI Việt Nam cho cùng một tác vụ, áp dụng [quy trình phản biện phối hợp](../../references/paired-debate.md). Hai bên đề xuất, phản biện có căn cứ và chốt phương án theo mục tiêu, nguồn lực thực tế; sau đó hoàn thành đầu ra đã được giao. Chỉ dùng tác tử độc lập khi công cụ và hướng dẫn phiên cho phép; nếu tự phân tích theo hai vai trò thì nói rõ.

## Giọng đọc local miễn phí
Khi cần tạo lời đọc, clone từ file được phép hoặc dịch vụ hết credits, đọc [free-voiceover](../free-voiceover/SKILL.md) và dùng adapter có kiểm tra quyền. Đây là luồng bổ sung, không chứng minh engine đã cài hay chạy. Với video bắt buộc có lời đọc, thiếu giọng phải báo bản nháp chưa hoàn chỉnh; không tự coi nhạc và chữ thay cho lời đọc đã yêu cầu.

## Xuất sang Gemini — quy tắc mặc định của bộ kỹ năng

Từ phiên bản này, khi người dùng yêu cầu đóng gói/xuất/chuyển bộ kỹ năng sang Gemini Web/Gems hoặc Gemini CLI, **bắt buộc** đọc [`gemini/EXPORT_POLICY.md`](../../gemini/EXPORT_POLICY.md) và đóng kèm hướng dẫn ngay trong chính gói xuất. Không chuyển chỉ mã skill rồi để người dùng tự ghép prompt.

- Gemini Web: dùng `gemini/GEM_INSTRUCTIONS.txt` làm Instructions, `gemini/README.md` để thêm Knowledge; không nói Gem đã được cài khi chưa thực hiện.
- Gemini CLI: dùng `gemini/GEMINI.md` làm `GEMINI.md` tại thư mục dự án, các skill trong `.gemini/skills`, giữ references/scripts; không tự cấp quyền tool.
- Khi phối hợp Trợ Lý Xây Kênh và Content AI Việt Nam, kèm `gemini/GEM_PHOI_HOP.txt` trong gói hợp nhất.
- Ở những lần cập nhật sau, duy trì quy tắc này và làm mới tệp hướng dẫn để tương thích với nội dung skill hiện hành. Việc lưu quy tắc ở plugin **không tự động đồng bộ** các thay đổi sang Gemini.
