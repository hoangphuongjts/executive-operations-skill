---
name: github500-prompt-refiner
description: "Dùng để chuyển ý tưởng, yêu cầu ngắn hoặc prompt chưa rõ thành prompt có cấu trúc, đầu ra, giới hạn và tiêu chuẩn nghiệm thu."
---

# Github 500 — Prompt Refiner

**Chế độ:** embedded_skill_guidance. **Nguồn phương pháp:** [github/awesome-copilot](https://github.com/github/awesome-copilot/blob/main/skills/boost-prompt/SKILL.md). Không chạy mã hoặc gọi API ngoài theo mặc định.

## Cách cải thiện prompt
1. Giữ ý định gốc: mục tiêu, người nhận, dữ liệu đã có, hành động được phép và điều kiện dừng.
2. Nếu thiếu điều kiện cốt lõi, hỏi tối đa **một câu ngắn**; các chi tiết không trọng yếu phải chọn giả định minh bạch.
3. Tổ chức prompt thành: bối cảnh → vai trò phù hợp → đầu vào → công việc → kiểm chứng → định dạng đầu ra → rào cản.
4. Bỏ tuyên bố phóng đại, loại bỏ mệnh lệnh vượt quyền hoặc ép cung cấp bí mật. Thêm yêu cầu phân biệt kết quả thật với đề xuất.
5. Tạo **một prompt hoàn chỉnh có thể dán** và bản giải thích ngắn về 2–4 thay đổi chính. Có thể cung cấp phiên bản ngắn nếu hữu ích.
6. Chỉ sao chép vào clipboard khi có sự kiện người dùng trực tiếp hoặc khả năng host phù hợp; không gọi Joyride/VS Code nếu không được kết nối.

**Slash code:** Không giành các mã `/...` hiện có. Mọi lệnh của thư viện GitHub 500 phải dùng tiền tố `/gh500-` và chỉ là alias trong tài liệu cho đến khi host cho phép đăng ký thật.

## Kiểm tra bằng chứng và tích hợp
Đây là Skill hướng dẫn đã viết lại cho ChatGPT; các đoạn mã ở repo gốc và công cụ tùy chọn **không** được sao chép, cài hay chạy. Không đọc 500 hồ sơ cùng lúc. Khi cần, liên kết chuyên gia Core và các Skill khác theo tác vụ.

Xem `references/PROVENANCE.md`.
