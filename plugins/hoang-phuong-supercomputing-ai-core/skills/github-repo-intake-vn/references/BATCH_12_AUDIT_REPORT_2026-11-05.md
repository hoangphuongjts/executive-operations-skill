# Báo cáo kiểm tra batch 12 — 2026-11-05

Đã xử lý bốn bản ghi CSV toàn cục 41–44, tương ứng Cụm 2 “Kiến trúc hệ thống”, hạng 17–20. Hai nguồn có license phù hợp được chuyển thể thành skill hướng dẫn prompt-only; một repo catalog và một workshop không có license bị loại. Không sao chép mã hoặc cài dependency.

| Bản ghi | Repo / commit ghim | Giấy phép | Kết luận |
|---:|---|---|---|
| 41 | [EdwinVW/pitstop](https://github.com/EdwinVW/pitstop/commit/6ab69be3ce6140c56292ee2eaa1866afdf4888c9) | Apache-2.0 | Repo là ứng dụng mẫu .NET microservices, không có SKILL.md. Các tài liệu arc42 và ADR có cấu trúc đủ để chuyển thể thành architecture-documentation-arc42-vn: soạn tài liệu 12 phần, gắn nguồn, phân biệt sự kiện/giả định/đề xuất và kiểm tra tính nhất quán. Cây 1.110 đường dẫn gồm nhiều service, Docker, Kubernetes, Istio/Linkerd và Vite frontend. Đã xem tĩnh các script dừng/xóa toàn bộ Docker containers, xóa dangling images, dựng lại images, apply manifests và gỡ Istio; không script nào được chép hoặc chạy. Chỉ chuyển thể tài liệu, không tích hợp ứng dụng hay dependencies. |
| 42 | [drveillard/distributed-systems-architecture](https://github.com/drveillard/distributed-systems-architecture/commit/8cb52fb281e293378cd875f3903ab70ee986045a) | MIT | Cây 81 đường dẫn là danh mục bài viết, sách, tài liệu kiến trúc công ty và liên kết. Có LICENSE nhưng không có SKILL.md, scripts hoặc dependencies. Loại vì không có workflow độc lập để tích hợp. |
| 43 | [sujatas93/ai-native-llm-architecture-workshop](https://github.com/sujatas93/ai-native-llm-architecture-workshop/commit/73a49f76579b108129ba3131d2536f09cb84adb9) | Không xác định; không có license metadata hoặc LICENSE | Cây 24 đường dẫn có bảy notebook, các module Python trong support_utils và .env.example; không có SKILL.md hay dependency manifest. Không mở/chạy notebook hoặc code, không cài dependency. Loại vì thiếu license và là workshop có runtime, không phải skill tự chứa. |
| 44 | [Ali-Meh619/System_Design_ML_Principles](https://github.com/Ali-Meh619/System_Design_ML_Principles/commit/09ddcc6f0f140829c2fda10e27b31a70b0c5ec7f) | MIT | Repo là guide tĩnh với 49 chủ đề, không có SKILL.md, scripts hoặc dependency manifest. Tài liệu ML system design mô tả quy trình riêng từ mục tiêu dự đoán, dữ liệu/feature, training/evaluation, serving, rollout, monitoring đến retraining/rollback. Đã chuyển thể thành ml-system-architecture-vn, không sao chép website, notebook, dữ liệu hoặc mã. |

## Skill mới trong bản phát hành dự kiến 16.0.30

- architecture-documentation-arc42-vn — lập tài liệu kiến trúc 12 phần theo arc42, có sổ bằng chứng, ADR, quality scenarios và khoảng trống cần xác minh.
- ml-system-architecture-vn — thiết kế vòng đời hệ thống ML sản xuất từ dữ liệu tới serving, vận hành và rollback. Được ánh xạ chính vào Cụm 2, liên quan thứ cấp tới Cụm 7.

Hai skill là bản hướng dẫn tiếng Việt; chưa kiểm toán bảo mật toàn repo cho các nguồn. Không mã hoặc dependency upstream nào được thực thi, nhập, cài hay đóng gói.

## Trùng lặp và trạng thái

- Bốn repo trong batch này khác nhau và không trùng với các repo đã xử lý.
- Sau khi readback mục tiêu: 13/384 repo host_verified; 29/384 bị loại; 342/384 còn chờ/đang rà soát. Có 382 repo duy nhất và hai bản ghi lặp liên cụm trong registry.
- Cụm 1: 14/24; Cụm 2: 6/24; tổng skill chuyên môn dự kiến 46. Cụm lõi 16 skill, 128 hồ sơ agent và 108 mã được giữ nguyên.
