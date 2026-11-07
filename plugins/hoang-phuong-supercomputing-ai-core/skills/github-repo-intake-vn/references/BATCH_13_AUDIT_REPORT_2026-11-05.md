# Batch 13 — kiểm toán tĩnh và quyết định (dòng 45–48) — 2026-11-05

**Nguồn gốc:** CSV master không được mount; dùng registry 384 mục trong bản plugin 16.0.32, release `pluginrel_6aec142f60988191a9d0c7af885f0182`. Chỉ đọc tĩnh GitHub ở commit cố định; không clone, chạy, import, cài dependency hoặc copy mã từ repo ngoài.

| Row | Repo, commit | Nhánh | License | Quyết định | Căn cứ |
|---:|---|---|---|---|---|
| 45 | [marcamillion/software-systems-architecture](https://github.com/marcamillion/software-systems-architecture/commit/94e8199ff46090e1e56b910567ca2cca7c173889) | master | MIT | LOẠI | 6 tệp, bốn bài phác họa mô hình domain, một trang TODO; không SKILL, không quy trình độc lập, script hay dependency. |
| 46 | [DreamOfTheRedChamber/Scalable-Software-Architecture](https://github.com/DreamOfTheRedChamber/Scalable-Software-Architecture/commit/02d6e5a9ec9b2ae8b556322695f06107959050d2) | master | MIT | LOẠI | Chỉ README ~30k chữ chứa link bài nói, tài liệu và LICENSE; không SKILL, script hay quy trình sở hữu. |
| 47 | [Haaaiawd/ANWS](https://github.com/Haaaiawd/ANWS/commit/3f3d9116aa3be07fc7f8a5c26d996d60323c0b95) | main | MIT | CHUYỂN THỂ 1 SKILL prompt-only; chờ readback | 17 skill trùng bản ngôn ngữ EN/ZH, nhiều phần gắn `anws` runtime. Chọn riêng `tech-evaluator` cho ma trận 12 chiều + ATAM, không copy CLI, script hay package. Quá trình đánh giá/ADR có tính độc lập sau khi chuyển thể và ghi rõ sai khác. |
| 48 | [ibrahimcanerdogan/Software-Design-and-Architecture-Specialization](https://github.com/ibrahimcanerdogan/Software-Design-and-Architecture-Specialization/commit/6f0db8c2e50318287cf815c05d08f4cbaa57db06) | main | MIT root | LOẠI | Tập hợp bài tập khóa học, tệp PDF/hình, dự án Android Java/Gradle; không SKILL. Gradle có các dependency cũ, jar snapshot, task clean xóa build dir. Không phân phối học liệu bên thứ ba. |

## Kiểm soát rủi ro
- MIT của repo **không** đồng nghĩa các link ngoài, khóa học và bản nhị phân có quyền phân phối tự do. Không sao chép chúng.
- ANWS `package.json`: Node >=18, `prepublishOnly` chạy `npm run sync`, `test` chạy Node test; CLI có `--yes` để tự xác nhận. `lib/init.js`, `lib/update.js`, `lib/copy.js` có chức năng ghi đè/ghi file; `update.js` có `fs.rm(... recursive: true, force: true)` cho thư mục legacy `.agent/` sau xác nhận/force. Chúng **không** được đóng gói/chạy/import.
- Chỉ kiểm tra một số tệp đại diện và đường dẫn toàn repo; **repo-wide security audit = 0**, không kết luận toàn bộ nguồn an toàn.
- Skill mới `architecture-technology-evaluation-vn`: input/output độc lập, giảm phụ thuộc ANWS; chỉ tư duy, có chứng cứ, khung ma trận tính lại được, không cho phép tự ghi ADR hoặc thao tác file.

## Theo dõi
- Trước batch: 13 host_verified / 29 excluded / 342 pending = 384; metadata 44; full audit 0.
- Sau khi readback mục tiêu: **14 host_verified / 32 excluded / 338 pending = 384**; metadata 48; full audit 0.
- Cụm 2: 6 -> 7/24 sau khi xác minh skill mới; Cụm 1: 14/24, 14 cụm khác giữ số cũ. 16 cụm/128 Agent/108 mã phải được bảo toàn.
- Master registry cũ vẫn có row 45-48 `discovered_not_audited`; **delta là sổ thay đổi bổ sung**, cần merge vào master trong batch kế tiếp khi có quyền lấy toàn bộ nội dung và ghi đè an toàn. KHÔNG trình bày master cũ như đã đồng bộ.
- Release chứa thay đổi dự kiến `16.0.33`; release ID và host_verified phải xác nhận bằng Plugin Creator readback, không điền dự đoán.
