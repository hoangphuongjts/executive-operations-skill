# HoangPhuong Core — GitHub Repo Intake v0.1 (16 cụm)

Bộ công cụ có thể chạy Python 3.10+ được phát triển để **tiếp nhận và phân loại** repository GitHub theo 16 cụm của HoangPhuong Core. Gói này là mã nguồn mới, **không phải 384 repo đã tải và cài**. Không thực thi script hoặc cài dependencies của repo ngoài.

## Sắp xếp
- `source/quarantine_download.py`: tải ZIP vào vùng cách ly từ commit SHA 40 ký tự; hạn mức 40 MiB, kiểm tra định dạng, chống ghi đè, ghi SHA-256. **Cần Internet trên máy chạy.** Chưa thử GitHub API trực tiếp từ môi trường hiện tại (DNS bị chặn).
- `source/audit_candidates.py`: tái sử dụng bộ lọc trùng/tiền kiểm toán Core đã xây trước; chỉ đọc và tạo báo cáo.
- `source/cluster_registry.py`: 16 cụm × 24 vị trí và bốn trường hợp cần đánh giá thay thế.
- `reports/CANDIDATES_SELECTED.json`: nguồn có bằng chứng GitHub connector, vẫn là ứng viên.
- `tests/`: kiểm thử offline.

## Cách chạy Windows PowerShell
Trong thư mục đã giải nén:

```powershell
py -m unittest discover -s tests -v
py source\quarantine_download.py --repo pallets/flask --commit <SHA40_TU_GITHUB> --output quarantine\flask-pinned.zip
py source\audit_candidates.py scan --checkout C:\duongdan\checkout-da-duoc-kiem-toan --output reports\static_scan.json
```

Gói downloader KHÔNG tự resolve một tên branch thành commit: người vận hành phải cung cấp SHA đã xác minh; không nên dùng HEAD/main. Sau khi có ZIP, vẫn phải kiểm tra giấy phép, dependency, hooks, security, sandbox, rollback trước khi cài. **Chỉ tải ZIP không có nghĩa đã cài Skill**.

## Giới hạn
- Repo `pallets/flask`, `uswds/uswds`, `apache/airflow`, `promptfoo/promptfoo` đều là ứng viên thay thế, chưa được sao chép/cài vào Core. Một số repo là framework hoặc ứng dụng, **không phải** một file `SKILL.md` có thể nhập thẳng.
- GitHub connector cho phép đọc các file chọn lọc, nhưng không cung cấp toàn bộ source checkout trong phiên này. Môi trường container không phân giải được github.com; không có minh chứng đã tải cả repo.
- Các repo không được tự động trao quyền/OAuth; các Skill/Plugin gốc của Core không bị sửa đổi trong gói này.
