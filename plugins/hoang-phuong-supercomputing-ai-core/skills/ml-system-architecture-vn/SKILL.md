---
name: ml-system-architecture-vn
description: "Thiết kế hoặc rà soát kiến trúc hệ thống có mô hình machine learning trong luồng sản phẩm; bao quát dữ liệu, đặc trưng, huấn luyện, phục vụ, đánh giá và vận hành."
license: MIT
---

# Thiết kế kiến trúc hệ thống machine learning

Dùng kỹ năng này khi một sản phẩm cần biến dữ liệu thành dự đoán hoặc quyết định trong môi trường thực. Tập trung vào toàn bộ vòng đời hệ thống ML; không chọn mô hình chỉ dựa vào tên thuật toán hay độ chính xác offline.

## Quy trình

1. **Xác định quyết định của sản phẩm.** Ghi đầu vào, dự đoán, hành động sau dự đoán, người sở hữu quyết định, thời điểm cần kết quả, độ mới dữ liệu và điều xảy ra khi mô hình không phản hồi. Hỏi riêng chi phí của dương tính giả, âm tính giả và trường hợp cần người duyệt.
2. **Chốt yêu cầu và giới hạn.** Thu thập độ trễ p95/p99, thông lượng, sẵn sàng, chi phí, yêu cầu giải thích, quyền riêng tư, lưu trữ, vùng triển khai và tốc độ nhận nhãn. Dùng khoảng hoặc để trống khi chưa có số đo; không tạo benchmark giả.
3. **Vẽ đường đi của dữ liệu.** Mô tả nguồn sự kiện, hợp đồng dữ liệu, kiểm tra chất lượng, xử lý batch/stream/request-time, tạo nhãn, feature store offline/online, backfill và tính đúng tại thời điểm dự đoán. Nêu rõ dữ liệu cá nhân, quyền truy cập, thời hạn lưu và cách xử lý xóa dữ liệu.
4. **Thiết kế vòng đời huấn luyện.** Xác định cách tạo tập nhãn, chia tập theo thời gian hoặc nhóm phù hợp, baseline, metrics theo từng nhóm người dùng/trường hợp, kiểm tra rò rỉ dữ liệu, calibration, tái lập thí nghiệm, lưu artifact và phê duyệt model registry. Phân biệt điểm số offline với kết quả sản phẩm.
5. **Thiết kế luồng phục vụ.** Theo dõi request từ xác thực và kiểm tra schema đến truy xuất đặc trưng, phiên bản mô hình, inference, ngưỡng chính sách và hành động. Đặt ngân sách độ trễ cho từng bước; mô tả timeout, retry có giới hạn, fallback, human review và log kiểm toán.
6. **Lập phương án phát hành.** So sánh batch với online hoặc hybrid theo độ mới, độ trễ, độ phức tạp và chi phí. Đề xuất shadow, canary hoặc challenger khi phù hợp; đặt guardrail và tiêu chí dừng trước khi mở rộng. Không tự phát hành hoặc thay ngưỡng quyết định.
7. **Thiết kế giám sát và phản hồi.** Theo dõi chất lượng dữ liệu, lỗi phục vụ, latency, chi phí, phân phối đầu vào, hiệu năng theo nhóm, drift và độ trễ nhãn. Nêu tín hiệu kích hoạt điều tra/huấn luyện lại, người chịu trách nhiệm, quy trình rollback và cách xử lý khi dữ liệu phản hồi sai lệch.
8. **Đánh giá trade-off và rủi ro.** So sánh 2–3 phương án khi lựa chọn còn mở. Ghi tác động của feature freshness, model size, batching, cache, fallback, explainability và human review. Tạo ADR cho quyết định quan trọng, kèm điều kiện xem xét lại.
9. **Bàn giao kế hoạch kiểm chứng.** Liệt kê giả định, sơ đồ thành phần/luồng dữ liệu, giao diện, yêu cầu chấp nhận, metrics offline và online, rủi ro, rollout, rollback cùng dữ kiện còn thiếu.

## Đầu ra gợi ý

- Mục tiêu dự đoán và quyết định nghiệp vụ.
- Sơ đồ dữ liệu, huấn luyện, đăng ký model, phục vụ và phản hồi.
- Bảng yêu cầu chất lượng và cách đo.
- Trade-off, ADR, guardrail, kế hoạch rollout/rollback.
- Nguồn đã dùng, giả định và câu hỏi còn mở.

## Giới hạn

- Không khẳng định độ chính xác, độ trễ hay chi phí nếu chưa có phép đo hoặc nguồn.
- Không coi model output là quyết định cuối cùng; nêu chính sách và người chịu trách nhiệm.
- Không mặc định hệ thống cần real-time, streaming, feature store hoặc LLM; chọn sau khi yêu cầu xác định.
- Không tự chạy notebook, huấn luyện mô hình, tải dữ liệu hoặc gọi dịch vụ.
- Với quy định, chuẩn hoặc benchmark có thể thay đổi, xác minh nguồn chính thức và phiên bản hiện hành.
- Với kiến trúc agent nhiều bước và công cụ, định tuyến sang skill chuyên về agent runtime nếu đã được nạp.

