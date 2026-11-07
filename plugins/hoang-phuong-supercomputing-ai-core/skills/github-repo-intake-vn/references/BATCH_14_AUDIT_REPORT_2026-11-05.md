# Batch 14 — dòng 49–52 — Kiểm tra nguồn tĩnh

Nguồn quyết định: danh sách 384 bản ghi theo plugin v16.0.34, nhánh mặc định và commit ghim trên GitHub.

| Dòng | Repo, commit | LICENSE | Quyết định |
|---:|---|---|---|
|49|addyosmani/agent-skills `301b02b12bff98e4688e6984af6556802322bbde`|MIT|Loại vì trùng bộ AI Coding Vietnamese Kit đã cài.|
|50|obra/superpowers `22f0b463e7a5e579904dd6211a520321035526f7`|MIT|Loại vì bộ `super-*` đã có.|
|51|MengTo/Skills `1de14e21b2ba8937c0f7f6ddca581cf7cd9d94af`|MIT|Chuyển thể duy nhất `web-technique-to-skill` thành `web-technique-skill-extraction-vn` (C3).|
|52|sickn33/agentic-awesome-skills `48de968b4615c294de601f72268aa7be88dde863`|MIT|Chuyển thể duy nhất `api-contract-testing` thành `api-contract-compatibility-testing-vn` (C3).|

Hai skill mới là hướng dẫn tiếng Việt độc lập; không sao chép mã, scripts, dependencies, dữ liệu, công cụ runtime hoặc media upstream. Root license MIT được bảo toàn, có provenance theo commit và file nguồn. Với repo 51/52 nguồn lớn có scripts và assets; **chưa audit toàn repository**, không kết luận an toàn để cài upstream. Soát sự phù hợp và trùng lặp trên file SKILL.md được chọn; không tính thành full-repo security audit.

Báo cáo này là quyết định đánh giá; trạng thái host_verified chỉ có hiệu lực khi đã đọc lại host sau release. Master 384 dòng chưa được sửa trong batch này.
