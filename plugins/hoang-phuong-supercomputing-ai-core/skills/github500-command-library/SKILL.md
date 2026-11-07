---
name: github500-command-library
description: "Dùng khi tra cứu hoặc gợi ý các câu lệnh chat AI được khai báo với tiền tố /gh500-, tránh trùng bộ 108 mã học tập và định tuyến tới các Skill đã cài."
---

# Github 500 — Command Library

**Chế độ:** embedded_skill_guidance. **Nguồn phương pháp:** [github/awesome-copilot](https://github.com/github/awesome-copilot/blob/main/skills/boost-prompt/SKILL.md). Không chạy mã hoặc gọi API ngoài theo mặc định.

## Lệnh gợi ý của thư viện GitHub 500 (chỉ là cú pháp hội thoại)
| Lệnh | Tác vụ | Skill tương ứng |
|---|---|---|
| `/gh500-find` | Tìm repository theo ngành/công cụ | `github500-research` |
| `/gh500-audit` | Kiểm toán plugin, dependencies, license | `github500-agent-supply-chain` |
| `/gh500-evaluate` | Benchmark chất lượng agent | `github500-agent-evaluation` |
| `/gh500-govern` | Xây chính sách quyền agent | `github500-agent-governance` |
| `/gh500-prompt` | Cải thiện prompt | `github500-prompt-refiner` |
| `/gh500-prompt-safety` | Rà soát prompt injection | `github500-prompt-safety` |
| `/gh500-flow` | Thiết kế automation | `github500-workflow-design` |
| `/gh500-hypothesis` | Lập giả thuyết khoa học | `github500-hypothesis-research` |
| `/gh500-eda` | Phân tích dữ liệu khám phá | `github500-exploratory-data` |
| `/gh500-cad` | Thiết kế CAD/fabrication plan | `github500-lab-cad-planning` |

### Quy tắc khớp lệnh
- Khi người dùng nhập tên lệnh đầy đủ và nội dung, áp dụng Skill tương ứng; không cần hỏi lại nếu đã đủ dữ liệu.
- Khi người dùng nhập chỉ `/gh500-`, hiển thị đúng các lệnh trên. Khi nhập tiền tố khác, **không** bịa tên mã; nếu có bộ 108 mã học tập trong ngữ cảnh, ưu tiên quy tắc gốc.
- Những tên lệnh này **không được đăng ký thành lệnh nền tảng ChatGPT**; đây chỉ là các alias được giải thích trong Skill.
- Không thay đổi bất cứ một mã nào trong bộ 108 mã gốc. Không tự tạo slash code trong namespace đó.
- Chỉ gọi công cụ thực sự có trong host; chỉ báo hoàn thành sau khi có bằng chứng.

## Kiểm tra bằng chứng và tích hợp
Đây là Skill hướng dẫn đã viết lại cho ChatGPT; các đoạn mã ở repo gốc và công cụ tùy chọn **không** được sao chép, cài hay chạy. Không đọc 500 hồ sơ cùng lúc. Khi cần, liên kết chuyên gia Core và các Skill khác theo tác vụ.

Xem `references/PROVENANCE.md`.
