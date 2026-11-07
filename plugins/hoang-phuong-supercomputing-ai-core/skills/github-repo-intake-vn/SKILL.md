---
name: github-repo-intake-vn
description: "Dùng khi cần tiếp nhận, tải và phân loại repository GitHub vào 16 cụm HoangPhuong Core, phát hiện trùng nguồn, xem xét thay thế và kiểm toán an toàn trước khi cài."
---

# GitHub Repo Intake — 16 cụm, vòng kiểm toán trước cài đặt

**Trạng thái:** Skill hướng dẫn + bộ công cụ Python có thể chạy riêng; không phải 384 repo đã tải/cài, không phải dịch vụ tự động chạy nền. Chỉ tiêu nhận dựa trên 16 cụm × 24 vị trí là kế hoạch, không phải tổng Skill đã được nghiệm thu.

## Phân loại và giữ nguyên hệ thống
1. Đọc danh mục gốc ở `../hoangphuong-supercomputing-core/references/GITHUB_16x24_CANDIDATES.json` cùng `../core-16-cluster-router/SKILL.md`. **Không đổi ID, tên hoặc vai trò của 128 Agent; giữ nguyên bảy Skill gốc và 108 mã học tập.**
2. Phân nhóm repo theo `cluster_id` 1–16; gắn một cụm chính và cụm tham chiếu. Không đếm cùng repo nhiều lần như hai Skill đã cài.
3. Khi có nguồn trùng hoặc archived, dùng `references/CANDIDATES_SELECTED.json` để đề xuất thay. **Bốn ứng viên đó chưa được cài, chưa đạt source audit.**
4. Xác minh owner/repo trên GitHub, commit SHA 40 ký tự, giấy phép từng phần, README, scripts, dependencies, network egress, secrets, symlink, mã độc và prompt injection. Không sao chép mã khi chưa có bằng chứng quyền sử dụng.
5. Mã `runtime/source/quarantine_download.py` tải ZIP từ **commit cố định** vào quarantine trên môi trường có mạng và quyền chạy. Nó không giải nén hay thực thi upstream; cần xem README. Bản kiểm thử mock không chứng minh đã tải live.
6. Dùng `runtime/source/audit_candidates.py` để lọc, quét tĩnh repo đã được người dùng cho phép; chưa chứng nhận an toàn nếu scanner không tìm thấy cảnh báo.
7. Chỉ sau khi có audit báo cáo và sandbox tests mới đề xuất chuyển qua `source_audited` → `packaged` → `host_integrated` → `host_verified`. Cài Plugin qua Plugin Creator phải kiểm tra release ID và phê duyệt cập nhật tương ứng.

## Quy trình an toàn
`DISCOVER → DEDUP → PIN COMMIT → LICENSE → AUDIT → SANDBOX TEST → PROPOSE → APPROVE → INSTALL → VERIFY`

**Mặc định:** `review_only`, chưa chạy mạng, không cài package, không tự sửa Plugin. Không coi thư viện/framework có mã Python/Node là Skill ChatGPT tự kích hoạt.

## Lệnh Python offline
Từ thư mục `runtime`:

```text
python -m unittest discover -s tests -v
python source/audit_candidates.py curate --input /path/to/GITHUB_16x24_CANDIDATES.json --output /path/to/report.json
python source/audit_candidates.py scan --checkout /path/to/authorized/source --output /path/to/static_scan.json
python source/quarantine_download.py --repo OWNER/REPO --commit EXACT_40_HEX_COMMIT --output /path/to/quarantine/repo.zip
```

`download` cần kết nối mạng và có thể tải mã chưa đáng tin; không thực thi và chỉ dùng sau khi đã chọn commit rõ ràng. **Không chứa token GitHub.**

## Trạng thái nguồn
- Số 384 là candidate slots trong catalog, không có bằng chứng đã cài 384 repo.
- Repo upstream mới tải: **0** trong phiên tạo công cụ (GitHub raw/clone không khả dụng qua mạng container). Chỉ các tệp README/LICENSE chọn lọc được xem thông qua GitHub connector; `blob sha` khác với commit sha.
- Runtime downloader: **12 bài kiểm thử offline**, mô phỏng HTTP response, chưa được kiểm thử live với GitHub API.
- Bộ công cụ Python này là mã tự viết/tái sử dụng từ bản kiểm toán do Core xây trước; các repo ngoài chưa sao chép vào Plugin.
