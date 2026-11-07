# Báo cáo kiểm tra batch 11 — 2026-11-05

Đã xử lý bốn bản ghi CSV toàn cục 37–40, tương ứng Cụm 2 “Kiến trúc hệ thống”, hạng 13–16. Cả bốn repo đã được ghim commit và kiểm tra metadata, license, skill manifest, cây file, scripts/dependencies. Không có repo nào được tích hợp.

| Bản ghi | Repo / commit ghim | Giấy phép | Kết luận |
|---:|---|---|---|
| 37 | [isr-uci-edu/ArchStudio5](https://github.com/isr-uci-edu/ArchStudio5/commit/61aeb2edc0674f395e257a6fe12e28d09dae1286) | License tùy chỉnh kiểu BSD của Regents/UC Irvine; phần Xalan-J có Apache-2.0 | Cây có 3.358 đường dẫn, không có SKILL.md. Đây là ứng dụng Java/Eclipse/OSGi để mô hình hóa kiến trúc, có Ant build; commit rất cũ. License nằm sâu trong feature và liệt kê các điều khoản thành phần khác nhau. Loại vì đây là sản phẩm phần mềm chứ không phải skill độc lập, đồng thời license không đồng nhất toàn repo. Không chạy build hoặc mã. |
| 38 | [jemmy512/software-engineer](https://github.com/jemmy512/software-engineer/commit/8a0fc33b7cebe561ef6af2d8fc4b1492472b49a5) | Không xác định; không có license metadata hoặc LICENSE trong cây ghim | Cây có 571 đường dẫn với danh mục học tập, ví dụ code và .gitmodules tham chiếu repo BookNotes bên ngoài. Không có SKILL.md hay dependency manifest. Không tải submodule hoặc chạy code. Loại vì đây là bộ sưu tập tài nguyên học tập/code không có license xác nhận, không phải skill tự chứa. |
| 39 | [lab-cursor/swarch-arch4AI](https://github.com/lab-cursor/swarch-arch4AI/commit/e539c60bc57dbdb4de9b3c891fbbcb11fd68d243) | Không xác định; không có license metadata hoặc LICENSE trong cây ghim | README mô tả bài tập đại học về fallback/cascade/cache cho demo ba service. Không có SKILL.md. requirements.txt khai báo FastAPI, Uvicorn, HTTPX, scikit-learn và pytest. run_all.py khởi chạy service bằng subprocess; data/make_data.py ghi CSV tổng hợp. Em chỉ đọc nội dung tĩnh, không chạy script hoặc cài dependency. Loại vì đây là tutorial có runtime, không có license xác nhận. |
| 40 | [theodesp/stable-systems-checklist](https://github.com/theodesp/stable-systems-checklist/commit/cbeef7c9d0950815b13e5a0076db2c759a0bb0ac) | Không xác định; không có license metadata hoặc LICENSE trong cây ghim | Cây chỉ có README và .gitattributes; README là checklist về thuộc tính hệ thống, thực hành nhóm và độ ổn định. Không có skill manifest, script hoặc dependency. Dù đúng chủ đề, không có license grant nên không sao chép/chuyển thể. |

## Trùng lặp và an toàn

- Bốn repo trong batch này là các repo riêng biệt; không trùng với các repo đã rà soát trước đó.
- Registry tiếp tục giữ hai bản ghi trùng liên cụm đã biết trong toàn bộ 384 dòng.
- Không có mã hoặc dependency upstream nào được tải, cài, nhập hay thực thi. Chưa hoàn tất kiểm toán bảo mật toàn repo cho các nguồn này.

## Trạng thái sau batch

- Bản ghi đã kiểm metadata: 40/384.
- Skill prompt-only từ repo đã host_verified: 11/384.
- Repo bị loại: 27/384.
- Bản ghi còn chờ/đang rà soát: 346/384 (gồm các bản ghi chưa xử lý và hai bản ghi trùng liên cụm đang chờ đối chiếu).
- Cụm 1: 14/24; Cụm 2: 4/24; tổng skill chuyên môn hiện được ánh xạ: 44.
- Cụm lõi 16 skill, 128 hồ sơ agent và 108 mã hiện hữu được giữ nguyên. Plugin hiện 16.0.28; batch kế tiếp nhắm 16.0.29.


## Xác minh sau phát hành 16.0.29

Plugin Creator readback xác nhận batch 11 và registry đã ghi nhận 40 bản ghi có metadata, 11 skill host_verified, 27 repo bị loại và 346 bản ghi còn chờ/đang rà soát. Danh sách file xác nhận 16 skill cụm, 128 hồ sơ agent và baseline có 108 mã. Batch 11 không thêm skill mới.
