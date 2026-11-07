# Nguồn và giấy phép

Skill này là bản tiếng Việt được biên soạn lại từ `stats-reporting-audit` trong [Boom5426/Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills), tại commit `00ecc183dddc5aba23462c1d547d250836122962` (nhánh `main`, ngày 2026-11-03).

- Tệp upstream được chọn: `skills/core/stats-reporting-audit/SKILL.md`.
- Giấy phép áp dụng cho skill upstream: Apache License 2.0. Tệp giấy phép đầy đủ và NOTICE đi kèm tại thư mục này.
- ATTRIBUTION.md của repo ghi skill upstream có nguồn gốc từ `nature-statistics` trong `Yuan1z0825/nature-skills`.
- Bản này đã dịch, rút gọn và sắp xếp lại luồng công việc cho người dùng tiếng Việt; các điểm chính về đơn vị độc lập, giả lặp, đối chiếu hai chiều giữa Phương pháp và Kết quả, báo cáo hình, câu hỏi cần tác giả xác nhận và giới hạn kết luận được giữ lại.
- Không chép script, chương trình, installer, manifest phụ thuộc hoặc bộ dữ liệu. Skill hoạt động như hướng dẫn văn bản; không cài package, gọi API hay tự thực thi phân tích.

Các script upstream được giữ ngoài plugin. Triage tĩnh tại commit nêu trên nhận diện installer tải nguồn từ mạng, giải nén và gọi bộ quản lý cài đặt có ghi/đổi tệp trong thư mục đích, tạo bản sao lưu và dọn thư mục staging; `section_corpus.py` truy cập dịch vụ bài báo và ghi đầu ra cục bộ. Những script này không được chạy. Đây không phải kiểm toán bảo mật đầy đủ cho toàn bộ repository.
