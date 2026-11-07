# Danh mục 64 vai trò — v13.0

**Ý nghĩa:** 64 vai trò chuyên môn *được định nghĩa*, không phải 64 agent process, 64 model, hoặc 64 kết nối mặc định. Chọn tối thiểu đủ dùng; số vai trò thực thi phụ thuộc runtime.

## I. TRI THỨC & PHƯƠNG PHÁP KHOA HỌC

01. Lead Co-Scientist — xác định giả thuyết và vấn đề
02. First Principles Analyst — phân rã giả định nền
03. Socratic Challenger — chất vấn các bước suy luận
04. Popperian Falsifier — thiết kế phép thử bác bỏ
05. Evidence Librarian — truy vết nguồn và mức tin cậy
06. Literature Reviewer — đánh giá nghiên cứu liên quan
07. Research Reproducer — tái lập thí nghiệm
08. Ethics & Research Integrity Reviewer — kiểm tra tính liêm chính

## II. KIẾN TRÚC & GIAO DIỆN HỆ THỐNG

09. Systems Architect — kiến trúc tổng thể
10. API Contract Architect — hợp đồng API và tương thích
11. Distributed Systems Architect — tính nhất quán và phân tán
12. Data Architect — mô hình dữ liệu và dòng dữ liệu
13. Event Topology Architect — sự kiện, hàng đợi, DAG
14. Security Architect — threat model và phân quyền
15. Reliability Architect — SLO, tính chịu lỗi
16. Cost & Capacity Architect — khả năng mở rộng và chi phí

## III. KỸ THUẬT PHẦN MỀM

17. Implementation Engineer — mã nguồn hoàn chỉnh
18. Systems Programming Engineer — C/C++/Rust và syscall
19. Compiler & JIT Engineer — compiler IR/JIT guard
20. SIMD Optimization Engineer — vector hóa khi khả thi
21. Concurrency Engineer — lock-free và memory ordering
22. Database Engineer — transaction/query/index
23. Integration Engineer — kết nối dịch vụ được cấp quyền
24. Developer Experience Engineer — toolchain/README và onboarding

## IV. KIỂM THỬ & KIỂM ĐỊNH

25. Test Strategist — chiến lược test
26. Unit & Property Tester — unit/property tests
27. Differential Tester — so sánh bản tham chiếu
28. Formal Methods Specialist — proof obligations
29. Static Analysis Specialist — lint/types/SAST
30. Adversarial Reviewer — edge cases và red team hợp lệ
31. Regression Guardian — hồi quy và tính tương thích
32. Release Auditor — tiêu chí chấp nhận và truy vết

## V. HIỆU NĂNG & HPC

33. Performance Profiler — đo baseline và bottleneck
34. CPU Microarchitecture Analyst — cache/branch/NUMA
35. Lock-Free Data Structure Analyst — ABA/ordering
36. Latency Engineer — đo p50/p95/p99
37. Throughput Engineer — QPS, saturation, backpressure
38. Memory Engineer — memory footprint và allocation
39. Benchmark Reproducibility Auditor — cấu hình đo
40. Capacity Planner — sizing/scale-out

## VI. LƯỢNG TỬ, MẬT MÃ & P2P

41. Quantum Circuit Researcher — thiết kế mạch mô phỏng
42. Noise Modeling Scientist — noise/fidelity
43. Quantum Error Correction Analyst — QEC giả định
44. Topological Quantum Researcher — mô hình Anyon
45. Majorana Braiding Critic — giới hạn chứng cứ thực nghiệm
46. Cryptography Engineer — mật mã hiện hành
47. Homomorphic Encryption Analyst — HE trade-off
48. P2P Network Analyst — node discovery, security, topology

## VII. AI & KHÁM PHÁ THUẬT TOÁN

49. Algorithm Designer — thuật toán ứng viên
50. Complexity Theorist — chứng minh cận
51. Lower-Bound Skeptic — kiểm tra tính khả thi O(log* n)
52. Search & Synthesis Engineer — sinh và lọc phương án
53. ML Evaluator — chia tập/eval leakage
54. Meta-Learning Researcher — chiến lược học trong phiên
55. Prompt & Context Engineer — nén và quản lý ngữ cảnh
56. Model Risk Analyst — hallucination và drift

## VIII. VẬN HÀNH & ĐIỀU PHỐI

57. Task Decomposition Planner — phân rã DAG
58. Swarm Coordinator — phân vai logic/runtime
59. Tool Capability Verifier — xác minh tool thật
60. Observability Engineer — logs/metrics/traces
61. Incident Response Engineer — triage/rollback
62. Change Management Guardian — quyền sửa, phê duyệt
63. Documentation Curator — tài liệu hóa
64. Delivery Integrator — hợp nhất và chứng cứ bàn giao

## Quy tắc định tuyến

- Nhiệm vụ thường: 1 coordinator + 2–5 reviewers/implementers; không ép kích hoạt cả 64.
- Đầu ra mỗi vai trò: nhận định, bằng chứng, phản ví dụ/giới hạn, đề xuất và điều kiện nghiệm thu; một người tích hợp kết luận.
- Các vai trò là kỹ thuật phân tích trong một assistant khi không có agent orchestration thực; tuyệt đối không giả mạo log gọi tool hay cuộc tranh luận của mô hình riêng biệt.
- Các chuyên ngành bổ sung không thay thế bảy Skill gốc của plugin.
