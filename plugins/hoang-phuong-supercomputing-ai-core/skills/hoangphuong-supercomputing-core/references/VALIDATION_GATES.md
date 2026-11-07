# VALIDATION GATES — v13.0

## 1. Phân loại trước hành động

| Cấp | Phương pháp xác nhận | Cách báo cáo |
|---|---|---|
| Concept | Logic, nguồn chính thống | `[ĐỀ XUẤT]` |
| Code generated | File/mã thật tạo ra | `[ĐÃ TẠO]` |
| Verified | Test/proof/benchmark đã chạy và đầu ra | `[ĐÃ KIỂM THỬ]` |
| Deployed | Runtime/service phản hồi hoặc logs | `[ĐÃ TRIỂN KHAI]` |
| Research target | Chưa có môi trường/bằng chứng | `[CHƯA XÁC MINH]` |

## 2. Bộ kiểm toán năm trục

1. **Trigger Accuracy:** Có nhận đúng tác vụ, kích hoạt đúng module và tuân thủ quyền truy cập?
2. **Context Bloat:** Có chọn tối thiểu vai trò, rút gọn prompt, tránh chạy mọi vai trò?
3. **Logic Robustness:** Có bất biến, phản ví dụ, kiểm thử edge cases, kiểm tra tính đúng?
4. **Safety:** Có an toàn dữ liệu, bản quyền, quyền chạy/sửa, rollback, key management?
5. **Format Compliance:** Kết quả có đúng định dạng, file đã xác minh, metadata/version hợp lệ?

## 3. Gate nghiên cứu thuật toán

- Ghi mô hình tính toán (RAM/word-RAM, parallel, randomised, approximation, amortized), input size và cận lý thuyết.
- Nêu đặc tả, baseline, thuật toán ứng viên, tính đúng; đo với dữ liệu đối kháng/chia thang; đính kèm seed/hardware/software/commit khi có.
- Chỉ công bố O(log* n) khi chứng minh và điều kiện áp dụng. Không suy luận độ phức tạp từ một benchmark.

## 4. Gate HPC/JIT/lock-free

- Preflight CPU flags, compiler version, AVX-512 support, NUMA, concurrency model và production safety.
- Kiểm tra safety under data races, linearizability/ABA, memory ordering, độ trễ đo dưới tải (QPS, burst, percentiles); so sánh p99 và confidence intervals.
- Chỉ nêu p99 < 30 μs hoặc 1M QPS khi log thực nghiệm hỗ trợ, nêu scope workload và percentile method.
- Tối ưu và self-patching chỉ với quyền sửa nguồn, test suite, canary & rollback; không tự patch executable khi người dùng chưa cho phép.

## 5. Gate quantum/P2P/HE

- Nhận diện mô phỏng/classical backend vs thiết bị QPU; phân biệt mô hình anyon/Majorana với bằng chứng phần cứng thực.
- Kèm noise/decoherence assumptions, QEC overhead, qubit count, simulator cost.
- P2P: threat model, transport, peer trust, consent; HE: scheme, key size, key storage, plaintext/ciphertext semantics.
- Không chứng nhận “fault tolerant” hay “quantum speedup” từ mô phỏng lý tưởng.

## 6. Gate phân vai tự học

- Có routing table + người tích hợp, tránh recursion vô hạn; giới hạn vòng lặp, chi phí, context, quyền truy cập.
- Được phép tự sửa đề xuất ở mức hội thoại, không có cơ chế training weights hay persistent self-edit trừ khi được tích hợp và cho phép.
- Ghi rõ synthetic role-play so với external tools/agents thực sự được gọi.

## 7. Bàn giao

Mỗi lần bàn giao: **mục tiêu → giả thuyết → bằng chứng/test → kết quả → giới hạn → bước tiếp theo**; khi không có cơ hội chạy test phải ghi rõ chưa kiểm thử, không tự tạo số liệu đo.
