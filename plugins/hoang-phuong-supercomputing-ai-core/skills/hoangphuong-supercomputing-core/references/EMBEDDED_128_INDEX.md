# EMBEDDED 128 — Danh mục tải theo nhu cầu

Các agent 001–128 dưới đây là **hồ sơ/vai trò kỹ năng** thuộc một plugin. Mặc định phân tích trong **một mô hình ChatGPT**, không gọi 128 mô hình độc lập.
Chọn lĩnh vực trước, sau đó xem `profiles/agent-NNN.json` nếu cần thông tin chuyên sâu. Không cần nạp toàn danh sách cho tác vụ thường.

## Cụm 01: Tri thức & phương pháp khoa học (agent 001–008)
- `001` **Lead Co-Scientist** — xác định giả thuyết và vấn đề
- `002` **First Principles Analyst** — phân rã giả định nền
- `003` **Socratic Challenger** — chất vấn các bước suy luận
- `004` **Popperian Falsifier** — thiết kế phép thử bác bỏ
- `005` **Evidence Librarian** — truy vết nguồn và mức tin cậy
- `006` **Literature Reviewer** — đánh giá nghiên cứu liên quan
- `007` **Research Reproducer** — tái lập thí nghiệm
- `008` **Ethics & Research Integrity Reviewer** — kiểm tra tính liêm chính

## Cụm 02: Kiến trúc hệ thống (agent 009–016)
- `009` **Systems Architect** — kiến trúc tổng thể
- `010` **API Contract Architect** — hợp đồng API và tương thích
- `011` **Distributed Systems Architect** — tính nhất quán và phân tán
- `012` **Data Architect** — mô hình dữ liệu và dòng dữ liệu
- `013` **Event Topology Architect** — sự kiện, hàng đợi, DAG
- `014` **Security Architect** — threat model và phân quyền
- `015` **Reliability Architect** — SLO, tính chịu lỗi
- `016` **Cost & Capacity Architect** — khả năng mở rộng và chi phí

## Cụm 03: Kỹ thuật phần mềm (agent 017–024)
- `017` **Implementation Engineer** — mã nguồn hoàn chỉnh
- `018` **Systems Programming Engineer** — C/C++/Rust và syscall
- `019` **Compiler & JIT Engineer** — compiler IR/JIT guard
- `020` **SIMD Optimization Engineer** — vector hóa khi khả thi
- `021` **Concurrency Engineer** — lock-free và memory ordering
- `022` **Database Engineer** — transaction/query/index
- `023` **Integration Engineer** — kết nối dịch vụ được cấp quyền
- `024` **Developer Experience Engineer** — toolchain/README và onboarding

## Cụm 04: Kiểm thử & kiểm định (agent 025–032)
- `025` **Test Strategist** — chiến lược test
- `026` **Unit & Property Tester** — unit/property tests
- `027` **Differential Tester** — so sánh bản tham chiếu
- `028` **Formal Methods Specialist** — proof obligations
- `029` **Static Analysis Specialist** — lint/types/SAST
- `030` **Adversarial Reviewer** — edge cases và red team hợp lệ
- `031` **Regression Guardian** — hồi quy và tính tương thích
- `032` **Release Auditor** — tiêu chí chấp nhận và truy vết

## Cụm 05: Hiệu năng & HPC (agent 033–040)
- `033` **Performance Profiler** — đo baseline và bottleneck
- `034` **CPU Microarchitecture Analyst** — cache/branch/NUMA
- `035` **Lock-Free Data Structure Analyst** — ABA/ordering
- `036` **Latency Engineer** — đo p50/p95/p99
- `037` **Throughput Engineer** — QPS, saturation, backpressure
- `038` **Memory Engineer** — memory footprint và allocation
- `039` **Benchmark Reproducibility Auditor** — cấu hình đo
- `040` **Capacity Planner** — sizing/scale-out

## Cụm 06: Lượng tử, mật mã & P2P (agent 041–048)
- `041` **Quantum Circuit Researcher** — thiết kế mạch mô phỏng
- `042` **Noise Modeling Scientist** — noise/fidelity
- `043` **Quantum Error Correction Analyst** — QEC giả định
- `044` **Topological Quantum Researcher** — mô hình Anyon
- `045` **Majorana Braiding Critic** — giới hạn chứng cứ thực nghiệm
- `046` **Cryptography Engineer** — mật mã hiện hành
- `047` **Homomorphic Encryption Analyst** — HE trade-off
- `048` **P2P Network Analyst** — node discovery, security, topology

## Cụm 07: AI & thuật toán (agent 049–056)
- `049` **Algorithm Designer** — thuật toán ứng viên
- `050` **Complexity Theorist** — chứng minh cận
- `051` **Lower-Bound Skeptic** — kiểm tra tính khả thi O(log* n)
- `052` **Search & Synthesis Engineer** — sinh và lọc phương án
- `053` **ML Evaluator** — chia tập/eval leakage
- `054` **Meta-Learning Researcher** — chiến lược học trong phiên
- `055` **Prompt & Context Engineer** — nén và quản lý ngữ cảnh
- `056` **Model Risk Analyst** — hallucination và drift

## Cụm 08: Điều phối & vận hành (agent 057–064)
- `057` **Task Decomposition Planner** — phân rã DAG
- `058` **Swarm Coordinator** — phân vai logic/runtime
- `059` **Tool Capability Verifier** — xác minh tool thật
- `060` **Observability Engineer** — logs/metrics/traces
- `061` **Incident Response Engineer** — triage/rollback
- `062` **Change Management Guardian** — quyền sửa, phê duyệt
- `063` **Documentation Curator** — tài liệu hóa
- `064` **Delivery Integrator** — hợp nhất và chứng cứ bàn giao

## Cụm 09: Sản phẩm & UX (agent 065–072)
- `065` **Product Discovery Researcher** — kiểm chứng nhu cầu và phân khúc sản phẩm
- `066` **UX Journey Analyst** — xác định hành trình và điểm nghẽn người dùng
- `067` **Accessibility Specialist** — đánh giá khả năng tiếp cận và WCAG
- `068` **Human Factors Researcher** — đánh giá tính dễ dùng, tải nhận thức
- `069` **Interaction Prototype Designer** — phát triển prototype và tương tác thử nghiệm
- `070` **Experiment Design Strategist** — thiết kế thí nghiệm A/B và định lượng ảnh hưởng
- `071` **Product Metrics Analyst** — định nghĩa retention, activation, funnel
- `072` **Release Adoption Analyst** — theo dõi tiếp nhận tính năng và feedback

## Cụm 10: Dữ liệu & tri thức (agent 073–080)
- `073` **Dataset Curator** — chuẩn hóa nguồn dữ liệu và metadata
- `074` **Data Quality Auditor** — đo trùng lặp, thiếu, drift và dữ liệu bất thường
- `075` **ETL Pipeline Designer** — thiết kế extract-transform-load có kiểm chứng
- `076` **Retrieval Architect** — thiết kế hệ thống tìm kiếm RAG và xếp hạng
- `077` **Knowledge Graph Modeler** — mô hình đồ thị tri thức và ontology
- `078` **Statistical Validity Reviewer** — đánh giá sampling, bias và kiểm định thống kê
- `079` **Causal Inference Researcher** — phân biệt tương quan và quan hệ nhân quả
- `080` **Data Privacy Steward** — quản trị vòng đời dữ liệu cá nhân và tối thiểu hóa

## Cụm 11: Agent & công cụ (agent 081–088)
- `081` **Agent Runtime Architect** — thiết kế runtime agent có ngân sách và deadline
- `082` **Agent Router Engineer** — chọn tác tử theo kỹ năng và đo độ chính xác định tuyến
- `083` **Tool Permission Auditor** — kiểm tra quyền gọi tool và phạm vi ủy quyền
- `084` **Agent Communication Engineer** — chuẩn hóa giao thức trao đổi và schema thông điệp
- `085` **Agent Memory Architect** — thiết kế bộ nhớ giới hạn và retention policy
- `086` **Multi-Agent Conflict Resolver** — xử lý mâu thuẫn giữa khuyến nghị tác tử
- `087` **Agent Budget Controller** — giám sát token, lượt gọi, thời gian và chi phí
- `088` **Agent Trace Auditor** — đối chiếu trace, kết quả và từng lần gọi agent

## Cụm 12: An toàn & bảo mật (agent 089–096)
- `089` **Prompt Injection Defender** — đánh giá ranh giới tin cậy và nội dung đầu vào độc hại
- `090` **Secrets Lifecycle Auditor** — kiểm tra API keys, rotation và lưu giữ bí mật
- `091` **Identity Access Reviewer** — đánh giá IAM, phân quyền tối thiểu và xác thực
- `092` **Supply Chain Security Analyst** — rà soát phụ thuộc phần mềm và SBOM
- `093` **Backup Restore Engineer** — thiết kế backup, khôi phục và kiểm tra dữ liệu
- `094` **Chaos Testing Designer** — xây bài kiểm tra lỗi mạng, disk, service
- `095` **Privacy Threat Modeler** — xây threat model cho dữ liệu cá nhân
- `096` **Compliance Evidence Reviewer** — kiểm tra dấu vết tuân thủ và chứng cứ

## Cụm 13: Nội dung & đa phương thức (agent 097–104)
- `097` **Scientific Script Editor** — biên tập kịch bản khoa học có nguồn kiểm chứng
- `098` **Storyboard Director** — thiết kế shot list, nhịp kể và storyboard
- `099` **Video Quality Inspector** — soát thời lượng, hình/tiếng, tỷ lệ và lỗi dựng
- `100` **Voice Synchronization Specialist** — đối chiếu voiceover, timeline và phụ đề
- `101` **Music Rights Reviewer** — kiểm tra quyền nhạc, giấy phép và bằng chứng sử dụng
- `102` **Multilingual Localization Editor** — bản địa hóa thông điệp và ngôn ngữ
- `103` **Creative Originality Auditor** — đánh giá tính nguyên gốc, sao chép và quyền dùng
- `104` **Channel Performance Analyst** — đánh giá analytics và thử nghiệm nội dung

## Cụm 14: Tài chính & quyết định (agent 105–112)
- `105` **Scenario Modeling Analyst** — dựng mô hình bull/base/bear có giả định
- `106` **Risk Budget Analyst** — đánh giá rủi ro theo kịch bản và danh mục
- `107` **Sensitivity Analysis Specialist** — đánh giá biến động đầu ra theo đầu vào
- `108` **Cash Flow Modeler** — dự báo dòng tiền và kiểm tra đơn vị
- `109` **Pricing Economics Analyst** — phân tích định giá, biên lợi nhuận và cạnh tranh
- `110` **Decision Quality Auditor** — kiểm tra thiên lệch quyết định và xác suất
- `111` **Market Evidence Researcher** — thu thập bằng chứng thị trường có nguồn
- `112` **Financial Assumptions Reviewer** — đối chiếu giả định và mức độ tin cậy

## Cụm 15: 3D, thiết bị & IoT (agent 113–120)
- `113` **Parametric CAD Designer** — thiết kế mô hình CAD kích thước tham số
- `114` **FDM Printability Engineer** — kiểm tra hướng in, overhang, tolerance
- `115` **Manufacturing Cost Estimator** — ước tính vật liệu, thời gian và hao hụt
- `116` **Geometry Validation Analyst** — kiểm tra manifold, collision và kích thước
- `117` **IoT Systems Architect** — thiết kế cảm biến, truyền nhận và dữ liệu
- `118` **Physical Experiment Planner** — thiết kế đo lường và kiểm soát biến vật lý
- `119` **Hardware Safety Reviewer** — đánh giá rủi ro điện/nhiệt/cơ khí
- `120` **Simulation Accuracy Auditor** — so khớp mô phỏng với thí nghiệm thực tế

## Cụm 16: Đánh giá & chất lượng (agent 121–128)
- `121` **Evaluation Dataset Architect** — xây bộ eval có nhãn và chia tập minh bạch
- `122` **Hallucination Claim Auditor** — phát hiện khẳng định thiếu nguồn hay vượt chứng cứ
- `123` **Benchmark Protocol Designer** — định nghĩa benchmark tái lập có baseline
- `124` **Drift Monitoring Analyst** — theo dõi lệch chất lượng giữa các bản phát hành
- `125` **SLO Acceptance Reviewer** — đặt tiêu chí p95, error budget và thời gian đáp ứng
- `126` **Release Evidence Publisher** — tổng hợp bằng chứng kiểm thử và nguồn gốc
- `127` **Rollback Decision Owner** — xác định ngưỡng quay lại bản trước
- `128` **Independent Quality Gatekeeper** — đối chiếu toàn bộ gate trước công bố hoàn thành

## Tệp nguồn được bảo toàn
- `references/ROLES_64.md` (ID 1–64)
- `references/ROLES_65_128.md` (ID 65–128)
- `references/AGENTS_128.json` (registry chuẩn để xác minh ID)
- `profiles/agent-001.json` … `profiles/agent-128.json` (hồ sơ sâu)
- `runtime/` và `scripts/` được lưu trong plugin để nâng cấp khi có phần cứng; **không chạy theo mặc định**.
