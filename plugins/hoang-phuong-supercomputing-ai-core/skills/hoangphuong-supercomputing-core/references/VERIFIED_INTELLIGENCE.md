# Verified Intelligence Core v13.1 — Protocol

## 1. Quy tắc chứng cứ và mức độ trưởng thành

| Trạng thái | Bằng chứng tối thiểu | Không có nghĩa là |
|---|---|---|
| Documented | Tài liệu kỹ năng và ràng buộc rõ ràng | Có backend thực thi |
| Bundled testable | Tệp mã có thể đọc/chạy khi được cấp runtime | Đã chạy trên máy của người dùng hoặc ChatGPT |
| Locally verified | Lệnh đã chạy trên môi trường được xác nhận, có output và ngày | Triển khai dịch vụ ngoài môi trường đó |
| Integrated/deployed | Kết nối/endpoint hoạt động được kiểm tra, logs và xác nhận quyền | Có SLA, QPU, hàng triệu QPS |
| Research only | Mục tiêu, giả thuyết và tiêu chí nghiệm thu | Kết quả khoa học đã chứng minh |

**Chỉ gắn nhãn `verified` khi có lệnh, ngày, môi trường, kết quả thực tế.** Không suy ra năng lực từ tên plugin hoặc mục tiêu nghiên cứu.

## 2. Lệnh kiểm thử (chỉ thực thi trong thư mục plugin đã giải nén)

Cần Python 3.10+; không cần thư viện bên thứ ba:

```bash
python skills/hoangphuong-supercomputing-core/scripts/verified_intelligence.py verify --root .
python -m unittest discover -s skills/hoangphuong-supercomputing-core/scripts -p 'test_*.py' -v
python skills/hoangphuong-supercomputing-core/scripts/verified_intelligence.py evaluate --root .
python skills/hoangphuong-supercomputing-core/scripts/verified_intelligence.py benchmark --size 4096 --iterations 300 --seed 131
python skills/hoangphuong-supercomputing-core/scripts/verified_intelligence.py report --root . --output ./verified-intelligence-report.json
```

- `verify`: kiểm tra 2 manifest cùng version/identity, 7 Skill gốc còn đủ, 64 vai trò đúng số, 4 module, capability matrix, và checksum bất biến của 8 tệp. Exit code `1` khi fail, `0` khi tất cả pass.
- `unittest`: có negative tests; không cần kết nối mạng.
- `evaluate`: đọc JSONL `id`, `expected`, `actual`, `evidence` (mảng string). Metrics: normalized exact-match, evidence presence; *không chứng minh correctness của câu trả lời chưa có ground truth*.
- `benchmark`: so sánh linear vs bisect search trên tập dữ liệu giống nhau, seed cố định, kiểm tra kết quả khớp, đo `ops_per_second` và p50/p95/p99 bằng `perf_counter_ns`. Đây là phép đo local Python, không phải benchmark AI model hay HPC.
- `report`: in/tạo JSON tổng hợp kiểm tra cấu trúc, eval **minh họa** và ma trận năng lực. Tạo file chỉ khi chỉ định `--output`.
- **Tài liệu không tự gọi các lệnh.** Cần công cụ thi hành và quyền người dùng để thực thi.

## 3. Chấm đánh giá có hệ thống

Với mỗi tác vụ dùng 5 trục đánh giá cũ: Trigger Accuracy, Context Bloat, Logic Robustness, Safety, Format Compliance. Mỗi trục cần tiêu chí đạt/trượt và ví dụ test. Dùng đánh giá độc lập từ dữ liệu thật trước khi công bố accuracy, đảm bảo tập kiểm thử không trùng tập huấn luyện/prompt mẫu.

- Bắt buộc có test đầu vào bình thường và đối kháng, kiểm tra cấu hình và phản ví dụ.
- Cho phép báo cáo số ca đúng/sai, coverage theo từng hạng mục và dữ liệu nguồn.
- Không chế tạo logs hoặc số liệu benchmark khi không chạy được.
- Khi thiếu runtime, chuyển trạng thái thành `Not executed` chứ không để `Passed`.

## 4. Gate phát hành

Trước phát hành: đọc release ID, kiểm tra đồng nhất manifest, đo checksum 7 Skill và `ROLES_64.md` hiện tại, đóng gói patch không sửa tệp gốc, chạy unittest, đánh giá các thay đổi. Cập nhật bằng Plugin Creator với expected release ID để tránh ghi đè cạnh tranh. Sau phát hành: đọc lại metadata, xem file list, kiểm tra checksum như baseline, xác nhận không có plugin trùng. Nếu full-tree test cần runtime mà không chạy được, ghi rõ hạn chế.

## 5. Ghi chép khi báo cáo năng lực

- `capability_id` và claim chính xác;
- `declared_status` từ matrix và `observed_status` có kiểm tra;
- `evidence` có đường dẫn/hash/log, timestamp, môi trường;
- `limitations` và điều kiện tiếp theo;
- `acceptance_status`: `pass`, `fail`, `not_run`, hoặc `not_applicable`.

Cấm suy diễn QPU, 1M QPS, p99 <30 µs, hàng nghìn tác tử, zero hallucination hoặc formally verified chỉ từ bộ quy trình này.
