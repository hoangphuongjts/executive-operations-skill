---
name: github500-ab-testing
description: "Dùng để thiết kế thí nghiệm A/B có đối chứng trong marketing, nội dung, UX, tăng trưởng; xác định giả thuyết, thước đo, chia nhóm và dừng thử nghiệm an toàn."
---

# GitHub 500 — Thiết kế thử nghiệm A/B (thí điểm v14.6)

Được biên soạn lại bằng tiếng Việt từ ý tưởng phương pháp và Skill `ab-testing` trong `coreyhaines31/marketingskills` (MIT); xem `references/PROVENANCE.md`. **Không sao chép các script hoặc tài nguyên phụ thuộc** từ repo nguồn.

## Khi nào dùng
Khi người dùng cần so sánh biến thể tiêu đề, thumbnail, landing page, CTA, email, mô tả video, trải nghiệm app. Nếu muốn chứng minh tác động, yêu cầu kiểm soát các biến gây nhiễu. Không lẫn lộn thử nghiệm A/B ngẫu nhiên với so sánh trước/sau không đối chứng.

## Quy trình
1. **Phát biểu giả thuyết có thể bác bỏ**: giả thuyết, nhóm người quan sát, yếu tố A/B, mức tác động tối thiểu đáng quan tâm, cơ sở dữ liệu quan sát.
2. **Định nghĩa đơn vị phân bổ** (tài khoản/người dùng/cụm), tính độc lập và tránh một người xem nhiều phiên bản; không tự mặc định số hiển thị bằng số người dùng.
3. **Chọn một chỉ số chính** đã thống nhất trước, chỉ số phụ, và guardrail (spam, hoàn tiền, retention, khiếu nại, latency).
4. **Thiết kế phân bổ, can thiệp và theo dõi**: random hóa nhất quán, thời gian phủ các ngày trong tuần, sự cố tracking, chiến lược rollout và rollback.
5. **Cỡ mẫu & thời hạn**: đưa ra công thức, đầu vào baseline, power, alpha, MDE; nếu thiếu số liệu thì để trống và gợi ý nguồn tính, không bịa n/độ tin cậy. Không tự dừng sớm khi p-value nhất thời dưới ngưỡng, trừ thiết kế sequential được xác định trước.
6. **Kiểm soát chọn mẫu**: kiểm tra sample-ratio mismatch, đo đối tượng thực sự được tiếp xúc. Không lọc theo hành động bị biến thể ảnh hưởng để tạo thiên lệch hậu can thiệp.
7. **Phân tích và kết luận**: effect size và khoảng tin cậy nếu có dữ liệu, phân nhóm khi được đăng ký trước, giới hạn đo lường; không tuyên bố nhân quả nếu không có randomization hợp lệ.

## Đầu ra
| Mục | Cần cung cấp |
|---|---|
| Câu hỏi nghiên cứu | ... |
| Biến A và B | ... |
| Đơn vị phân bổ | ... |
| Chỉ số chính, guardrail | ... |
| Baseline / MDE / alpha / power | ... hoặc CHƯA CÓ |
| Thời lượng & quy tắc dừng | ... hoặc CẦN TÍNH |
| Kịch bản sai lệch & phản ví dụ | ... |
| Cách nghiệm thu và rollback | ... |

Trường hợp thử trên mạng xã hội không có công cụ phân bổ đối tượng ngẫu nhiên, chỉ gọi là **so sánh định hướng**, không khẳng định A/B test chuẩn.

## Chính sách chung
- Chỉ hướng dẫn; không có quyền truy cập nền tảng quảng cáo, không tự bật campaign hay phát sinh phí.
- Bằng chứng hoặc dữ liệu chưa có phải ghi CHƯA XÁC MINH.

Xem nguồn và quyền sử dụng: `references/PROVENANCE.md`.
