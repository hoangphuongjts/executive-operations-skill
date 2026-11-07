# Báo cáo kiểm tra batch 08 — 2026-11-05

Đã xử lý bốn bản ghi CSV toàn cục 25–28, tương ứng Cụm 2 “Kiến trúc hệ thống”, hạng 1–4. Không repo nào có `SKILL.md` hoặc workflow Agent độc lập; cả bốn bị loại. Không có mã hay tài sản upstream được sao chép, nhập hoặc chạy.

| Bản ghi | Repo / commit ghim | License | Kết luận |
|---:|---|---|---|
| 25 | [Developer-Y/Scalable-Software-Architecture](https://github.com/Developer-Y/Scalable-Software-Architecture/commit/b6400f3c63f5f693c88a0e660c5fd4cea465cfb7) | MIT | Pinned tree chỉ có `LICENSE` và `README.md`; README là danh mục talk, paper và link. Không có skill, script hay manifest dependency. Loại vì chỉ là catalog. |
| 26 | [javabuddy/best-system-design-resources](https://github.com/javabuddy/best-system-design-resources/commit/d73ed375effbe7e79a51bda3b149cee6622fda1c) | Không khai báo; không có `LICENSE` trong pinned tree | Chỉ có README tuyển chọn khóa học, sách, website và tài liệu phỏng vấn system design. Không có skill, script hay dependency. Loại vì vừa thiếu license vừa không phải skill. |
| 27 | [codersguild/System-Design](https://github.com/codersguild/System-Design/commit/59c31d7b7933478e668598ee44ec0550ca76df87) | GPL-3.0 | Có 101 mục, chủ yếu là README tập hợp bài viết/tài liệu bên ngoài; không có `SKILL.md`, mã chạy hay manifest dependency. README ghi rõ nhiều bài được sưu tầm từ tác giả khác. Loại vì là kho tham khảo, không phải skill; không sao chép nội dung liên kết. |
| 28 | [arpitbhardwaj/architecture-diagrams](https://github.com/arpitbhardwaj/architecture-diagrams/commit/554f5c5f82acac4cc955cf347cfa527408d1be78) | MIT ở repo | Gồm 13 sơ đồ draw.io và 13 ảnh PNG xem trước; không có `SKILL.md`, script hay manifest dependency. README ghi nguồn sơ đồ từ tài liệu bên ngoài, gồm ByteByteGo. Loại vì là bộ tài sản hình, không phải skill; không nhập hình hay nguồn sơ đồ. |

## Giới hạn kiểm tra

Đã ghim commit, kiểm tra metadata/license, README, cây tệp, hình thức skill, script và manifest dependency. Các repo này không có skill hoặc runtime code để tích hợp. `source_code_audited` vẫn là `false`; kiểm toán bảo mật toàn repo chưa được thực hiện.
