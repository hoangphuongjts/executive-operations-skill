# Báo cáo kiểm tra batch 05 — 2026-11-05

## Phạm vi

Đã xử lý tuần tự Cụm 1, hạng 13–16 theo registry, tại commit đã ghim. Một skill hướng dẫn được bổ sung, ba repo bị loại theo tiêu chí tương thích/trùng lặp. Không mã upstream nào được chạy, nhập hoặc cài.

| Hạng | Repo / commit | Giấy phép | Kết quả |
|---:|---|---|---|
| 13 | [jxtse/scientific-research-skills](https://github.com/jxtse/scientific-research-skills/commit/68098d5565f423ffcfce1c9936de77ae230843aa) | MIT | Thêm `scientific-paper-reading-vn` từ `skills/paper-reading/SKILL.md`. Thư mục này chỉ có SKILL.md, không có dependency. Nó giúp đọc và giải thích một bài cụ thể; khác với đánh giá chất lượng bằng chứng và tổng hợp nhiều nguồn hiện có. |
| 14 | [bestagentkits/agency-skills](https://github.com/bestagentkits/agency-skills/commit/a837f9f81a4dc42b58a9ba87ab65e5110112a9c8) | MIT | Không thêm skill: scientific-critical-thinking trùng với appraisal hiện có; clinical-research phụ thuộc sáu script Python và tập trung nghiên cứu lâm sàng; research-ops-skills định tuyến qua bốn skill con. Không có mã được nhập hoặc chạy. |
| 15 | [ma-compbio-lab/SkillFoundry](https://github.com/ma-compbio-lab/SkillFoundry/commit/4a8cc0cd9f923cde47a7f542d4a84b92bbabc59f) | Apache-2.0 | Loại starter `reproducibility-cue-extraction-starter`: file không có frontmatter, tự mô tả chưa có runtime chuyên biệt và hướng dẫn chạy script ghi JSON resource anchors thay vì trích xuất cue tái lập. Script chỉ được đọc tĩnh, không chạy. |
| 16 | [modelscope/Awesome-Vibe-Research](https://github.com/modelscope/Awesome-Vibe-Research/commit/66a7ae0f2b55f87a297b0d44d8e5eb37e3cdb4d8) | Apache-2.0 | Loại vì commit ghim chỉ có README tiếng Trung/Anh và LICENSE, không có `SKILL.md`; đây là catalog liên kết tài nguyên. |

## Rà soát mã và dependency

- Repo 13 có generator tạo hình và bộ tải toàn văn ở các thư mục khác với skill được chọn. Triage tĩnh tìm thấy network, biến credential, thao tác ghi/xóa file, cùng dependency requests, bs4, openpyxl, pandas và pypdf. Không dùng các thành phần đó.
- Repo 14 có các script cho ước lượng cỡ mẫu, chọn endpoint và phase gate. Chúng không được đưa vào. Không chọn clinical workflow vì phạm vi chuyên môn hẹp và thiếu một triển khai đã kiểm toán.
- Repo 15 có `pyproject.toml` yêu cầu Python >=3.10 để cài framework. Script của starter chỉ đọc metadata/context JSON rồi ghi summary JSON, nhưng không tạo chức năng trích xuất cue đã hứa; không chạy/cài.
- Repo 16 không có mã hoặc skill độc lập tại commit đã kiểm tra.

## Giới hạn

`source_code_audited` vẫn là `false` cho cả bốn repo: kiểm tra commit, giấy phép, dạng skill, trùng lặp, dependency và triage tĩnh trong phạm vi đã nêu không tương đương kiểm toán bảo mật toàn repo. Ba repo bị loại không được tính vào tổng skill; repo 13 chỉ được tính sau khi Plugin Creator readback xác nhận.
