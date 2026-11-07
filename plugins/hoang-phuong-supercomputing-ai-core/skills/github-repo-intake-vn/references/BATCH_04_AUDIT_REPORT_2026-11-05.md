# Báo cáo kiểm tra batch 04 — 2026-11-05

## Phạm vi và kết quả

Đã xử lý tuần tự Cụm 1, hạng 9–12 từ registry ở commit đã ghim. Ba skill hướng dẫn tiếng Việt được thêm vào phạm vi nghiên cứu khoa học; một repo bị loại. Mọi thành phần được thêm đều là prompt/documentation. Không chạy mã upstream, installer, renderer hoặc dependency.

| Hạng | Repo / commit | Giấy phép | Kết quả |
|---:|---|---|---|
| 9 | [LeonChaoX/qinyan-academic-skills](https://github.com/LeonChaoX/qinyan-academic-skills/commit/df5a498a81e0f9c8f79d814446dcf9e9b8f68888) | MIT tại repo | Thêm `scientific-figure-planning-vn` từ `skills/沁言学术skills/qinyan-nature-figures/SKILL.md`. Phạm vi: figure dữ liệu định lượng, panel, đơn vị thí nghiệm, bất định, chú thích, khả năng đọc và provenance. Kho có 187 SKILL.md. `figure_preflight.py` được rà soát tĩnh hẹp và không sao chép; `install.sh` không chạy. |
| 10 | [BAIKEMARK/happy-figure-skill](https://github.com/BAIKEMARK/happy-figure-skill/commit/6292597250ed874d65756d13a492f6eefe07fb65) | CC BY-NC-SA 4.0 | Loại: giấy phép không đáp ứng khả năng sử dụng thương mại dự kiến và chức năng tạo prompt hình khoa học trùng với skill figure MIT được chọn. Script trích xuất dùng subprocess và phụ thuộc công cụ ngoài; không chạy/nhập. |
| 11 | [lgwrightlab/schematic-figure](https://github.com/lgwrightlab/schematic-figure/commit/09d8b6e98d04b91de6e8b6632b3356b9fc237417) | MIT tại repo | Thêm `schematic-figure-design-vn` từ `.claude/skills/schematic-figure/SKILL.md` cho hình cơ chế/thiết bị/khái niệm. Renderer JavaScript, mã Blender, demo, font và phụ thuộc Chrome/Blender không được đóng gói. |
| 12 | [gaasher/Agent-Loop-Skills](https://github.com/gaasher/Agent-Loop-Skills/commit/f1169e6db0b0f8a83ced3a18562b7c57e14a748a) | MIT tại repo | Thêm `research-question-refiner-vn` từ `loops/research-question/SKILL.md` để tinh chỉnh câu hỏi nghiên cứu theo độ cụ thể, khả năng trả lời, độ mới, tính khả thi và ý nghĩa. Không đưa helper Python hoặc công cụ tìm tài liệu upstream vào plugin. |

## Rà soát trùng lặp và dependency

- Figure planning xử lý biểu đồ và figure nhiều panel dựa trên dữ liệu; schematic design xử lý sơ đồ khái niệm/cơ chế. Hai đầu ra có mục đích riêng.
- Question refinement nằm trước các kỹ năng giả thuyết, thiết kế thực nghiệm, tổng quan văn liệu và viết grant hiện có.
- Kỹ năng từ hạng 10 có thể bao phủ tạo prompt hình, nhưng không được giữ do license và overlap.
- Các dependency/runtime upstream không được cài. Không có mã upstream được sao chép, thực thi hoặc nhập.

## Giới hạn kiểm toán

Kiểm tra gồm commit, license, dạng SKILL.md, khả năng trùng lặp, manifest/dependency và triage script trong phạm vi nêu trên. Kiểm toán bảo mật toàn bộ bốn repository chưa hoàn tất; các dòng được tích hợp giữ `source_code_audited: false`.

## Readback

Sau khi Plugin Creator cập nhật, đọc lại từng file thay đổi, kiểm tra version/release ID, kiểm tra sự hiện diện của ba SKILL.md mới, registry, manifest, trạng thái 16 cụm, 128 profile và 108 mã. Chỉ khi readback thành công mới xác nhận 3 repo host_verified.
