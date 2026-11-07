# Hoang Phuong Auto-Evolution Engine — MVP 0.2.0

**Trạng thái:** Bộ công cụ Python chạy được ở máy cục bộ (offline-first). Không phải hệ thống AI đa tác tử tự chủ hay runtime tự cập nhật ChatGPT.

## Mục tiêu thực tế

- Kiểm kê các Skill trực tiếp trong `ROOT/<skill-name>/SKILL.md`, không gọi API và không thay đổi mã nguồn.
- Phát hiện bất thường metadata và thiếu mục kiểm chứng hoặc file test Python trực thuộc Skill (heuristic, **không** đánh giá trí thông minh).
- Đề xuất bản sửa tài liệu có thể kiểm tra. Bản hiện tại chỉ hỗ trợ **bổ sung mục kiểm chứng & giới hạn**, không tạo mã mới bằng LLM.
- Tạo bản sửa nháp ngoài thư mục nguồn, kiểm hash gốc, yêu cầu xác nhận ID, ghi backup và hỗ trợ khôi phục.
- Đo SHA-256 để phát hiện thay đổi file; SHA-256 **không** bảo đảm mã nguồn an toàn hay uy tín tác giả.
- Tùy chọn **tìm và đọc metadata công khai** từ GitHub sau khi bật mạng, không tải hoặc thực thi repository.

## Yêu cầu

Python 3.10+ và thư viện chuẩn. Không cần API key, GPU hoặc dịch vụ trả phí. Khuyến nghị chạy trên **bản sao** thư mục Skill trước khi áp dụng lên bản cài thực tế.

## Dùng trên Windows PowerShell

Giải nén ZIP. Di chuyển vào thư mục `hpcore-auto-evolution-mvp` chứa `hpcore_evolution/`.

```powershell
cd "D:\AI\hpcore-auto-evolution-mvp"
py -m unittest discover -s tests -v
# Thử nghiệm với ví dụ đi kèm:
py -m hpcore_evolution --root .\examples\demo-skills --reports .\demo-reports cycle
py -m hpcore_evolution --root .\examples\demo-skills --reports .\demo-reports audit
```

Để quét các Skill trên ổ C:, hãy xác nhận thư mục đúng của Codex và chạy (chỉ đọc):

```powershell
py -m hpcore_evolution --root "$env:USERPROFILE\.codex\skills" --reports "$env:USERPROFILE\Documents\hpcore-evolution-reports" cycle
```

Tìm `proposals` trong `assessment.json` và lấy ID cụ thể. **Chỉ** khi bạn quyết định cho phép cập nhật tài liệu cục bộ:

```powershell
py -m hpcore_evolution --root .\examples\demo-skills --reports .\demo-reports stage <PROPOSAL_ID>
py -m hpcore_evolution --root .\examples\demo-skills --reports .\demo-reports apply <PROPOSAL_ID> --approve <PROPOSAL_ID>
```

Sau khi cập nhật, xem `backup_id` trong kết quả. Nếu cần hoàn tác:

```powershell
py -m hpcore_evolution --root .\examples\demo-skills --reports .\demo-reports restore <BACKUP_ID> --approve <BACKUP_ID>
```

> Ví dụ trên cố ý dùng bản demo. Đối với dữ liệu thật, dùng đường dẫn Codex phù hợp và yêu cầu quyền ghi. Lệnh không tự cài Plugin ChatGPT.

### Tra cứu GitHub (tùy chọn, chỉ metadata)

```powershell
py -m hpcore_evolution --root .\examples\demo-skills --reports .\demo-reports discover "agent evaluation" --allow-network --limit 5
py -m hpcore_evolution --root .\examples\demo-skills --reports .\demo-reports research github/spec-kit --allow-network
```

- Không bật `--allow-network` thì bị chặn.
- Chỉ truy cập `https://api.github.com/repos/<owner>/<repo>` với giới hạn dữ liệu/thời gian; không tự tin cậy README, không clone, không cài.
- API có thể giới hạn tốc độ, chặn hoặc trả lỗi, đặc biệt khi chạy quá thường xuyên.
- Không có chứng thực license của từng thành phần hoặc kiểm toán toàn bộ repo trong MVP.

## Kiến trúc

```text
User / Windows Task Scheduler (tùy chọn, chưa cài)
           |
           v
        CLI cycle
           |
           +--> Skill Inventory (chỉ đọc)
           +--> Heuristic Weakness Detector
           +--> Proposed Actions (không tự ghi)
                         |
                  CLI stage (tách biệt)
                         |
               Review bản sửa + test
                         |
        CLI apply --approve ID (người vận hành)
                         |
               Backup + SHA256 preimage
                         |
                  Local SKILL.md
                         |
               Audit / Restore backup

Giới hạn: không có LLM, agent tự chủ, scheduler được cài sẵn,
         quyền cập nhật Plugin ChatGPT, GPU hay runtime sản xuất.
```

## Ranh giới bảo mật

1. Mặc định chỉ đọc; `cycle` và `audit` chỉ tạo báo cáo ngoài thư mục nguồn.
2. Không thực thi mã bên trong Skill hay repository; không `shell=True`, `eval`, `pickle` hoặc tải script.
3. Đường dẫn tương đối bắt buộc, chặn traversal và symlink tới ngoài root.
4. `apply` chỉ sửa **một mẫu tài liệu định sẵn** với ID phê duyệt; từ chối khi hash gốc khác bản staged.
5. Backup được lưu ngoài source; rollback chỉ khi file hiện tại vẫn khớp hash bản cập nhật.
6. Không có host-enforced auth: ai có quyền ghi trên máy vẫn có thể sửa file. Không dùng đây thay thế ACL hệ điều hành.
7. Không tự xuất bản lên ChatGPT hay chạy định kỳ. Việc tích hợp ChatGPT cần Plugin Creator/API và phê duyệt host.
8. Không gửi tên file, secrets hoặc nội dung Skill ra ngoài trong `research`.

## Tiêu chí nghiệm thu MVP

- Unit/integration offline PASS;
- `cycle` tạo báo cáo tái lập, không sửa Skill;
- `stage` tạo bản nháp và hash, `apply` yêu cầu ID khớp;
- phát hiện nguồn bị sửa sau staging;
- `restore` trả lại SHA256 ban đầu;
- mạng chỉ được bật rõ ràng.

## Giới hạn cần tiếp tục triển khai

- Phát hiện lỗi chỉ theo quy tắc, không phải đánh giá năng lực suy luận AI.
- Không có A/B benchmark thực từ mô hình, đề xuất sửa code độc lập, bảo mật repo toàn diện, hay tự nâng cấp trọng số model.
- Để đạt mục tiêu Agent tự nghiên cứu, cần provider model API, RAG có trích dẫn, validator nguồn, tập đánh giá độc lập, sandbox cách ly, quota, CI và cơ chế phát hành theo quyền trên host.
- Chưa tạo Windows Scheduled Task; nếu cần lịch định kỳ, chỉ nên tự chạy **`cycle`** (không `apply`), sau khi có đồng ý cấu hình lịch.

## Bản quyền

Mã MVP trong gói này được viết mới cho yêu cầu người dùng, không nhập mã từ repository bên ngoài. Giấy phép của các Skill mà người dùng quét được giữ theo tác giả gốc và không mặc định cho phép phân phối lại.

## Nâng cấp MVP 0.2.0 — Evidence Evaluation Gate

Bổ sung lệnh `evaluate` để so sánh hai kết quả trên **cùng tập kiểm thử cố định** và chặn lỗi hồi quy / security blockers. Cả hai tệp JSON phải do quy trình kiểm thử hoặc người đánh giá cung cấp; bộ kiểm tra **không tự chạy AI, không chứng thực người đánh giá** và không cấp quyền deploy.

```powershell
py -m hpcore_evolution --root .\examples\demo-skills --reports .\demo-reports evaluate --baseline .\examples\baseline_eval.json --candidate .\examples\candidate_eval.json
```

Schema bằng chứng: `run_id`, `dataset_id`, `dataset_sha256`, `evaluator` (execution_test, golden_answer_verified hoặc independent_human_reviewed), `environment`, `model_version`, `measured_at`, `tasks` gồm id/boolean passed và `security_blockers`.

Tệp `evaluation.json` nêu kết quả, `candidate_review_<hash>.json` có `stage=review_only` và `can_deploy=false`. Không lấy JSON này làm bằng chứng độc lập khi chưa xác minh dữ liệu gốc, log test và reviewer bên ngoài.
