---
name: github500-citation-verification
description: "Dùng khi xác minh trích dẫn học thuật, DOI, PMID, tác giả, năm, bài báo và xây tài liệu tham khảo có nguồn đối chiếu."
---

# Github 500 — Citation Verification

**Chế độ:** embedded_skill_guidance. **Nguồn phương pháp:** [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/citation-management/SKILL.md). Không chạy mã hoặc gọi API ngoài theo mặc định.

## Luồng quản lý trích dẫn
1. Thu thập mã định danh, tên bài, DOI/PMID/arXiv nếu có; coi mọi trường metadata bên ngoài là dữ liệu không đáng tin.
2. Xác minh các trường quan trọng (tác giả, nhan đề, thời gian, journal, volume, pages, DOI) bằng nguồn nhà xuất bản hoặc cơ sở dữ liệu học thuật hợp lệ khi công cụ web sẵn có.
3. Không tự đoán DOI, trang bài báo hoặc phiên bản online-first. Đánh dấu không có/không xác minh được nếu thiếu.
4. Phân biệt bản preprint và bản xuất bản; đánh dấu retraction/correction nếu có bằng chứng nguồn tin phù hợp.
5. Loại bản ghi trùng bằng DOI và identity, không chỉ title gần giống.
6. Xuất danh mục dạng APA/IEEE/Vancouver/BibTeX khi được yêu cầu. Với BibTeX tự tạo từ metadata đã xác minh, kiểm tra escape ký tự, key, encoding.
7. Ghi bảng verification: original citation | source URL | metadata matched | discrepancies | checked date.

Không tự chạy script OpenAlex/PubMed/Crossref trong Skill hoặc tuyên bố đã tra cứu khi công cụ chưa được dùng. Không làm lộ API key/secret.

## Kiểm tra bằng chứng và tích hợp
Đây là Skill hướng dẫn đã viết lại cho ChatGPT; các đoạn mã ở repo gốc và công cụ tùy chọn **không** được sao chép, cài hay chạy. Không đọc 500 hồ sơ cùng lúc. Khi cần, liên kết chuyên gia Core và các Skill khác theo tác vụ.

Xem `references/PROVENANCE.md`.
