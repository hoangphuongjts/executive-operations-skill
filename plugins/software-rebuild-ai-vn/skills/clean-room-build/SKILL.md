---
name: clean-room-build
description: "Dùng khi người dùng đã xác định phạm vi và muốn viết mã nguồn mới, triển khai MVP hoặc thay thế ứng dụng từ đặc tả có quyền."
---

# Viết lại clean-room

## Nguyên tắc
- Làm từ đặc tả chức năng và quan sát được phép, không chép mã nguồn độc quyền/copyright từ bản dịch ngược trừ khi giấy phép và quyền cho phép.
- Tách vai trò người phân tích hành vi và người viết code khi phù hợp; lưu source provenance, quyết định thiết kế và sự khác biệt với tài sản bên thứ ba.
- Không gắn logo, hình, font, âm thanh, bản đồ, dữ liệu, nhãn hiệu bên thứ ba nếu chưa xác minh giấy phép. Không tích hợp endpoint bí mật.

## Cách thực hiện
1. Viết PRD, acceptance criteria, không-goals, dependency checklist; người dùng phê duyệt thiết kế nếu chưa ủy quyền triển khai trực tiếp.
2. Chọn stack tối giản cho nền tảng thực tế, kiến trúc module, storage, API, auth, logging; phân nhóm P0/P1/P2.
3. Dựng skeleton, kiểm thử một hành trình chính đầu-cuối. Tiếp tục theo lát cắt nhỏ với TDD và review, ưu tiên Superpowers, AI Coding, GitHub đã cài.
4. Chạy lint, unit, integration, e2e, accessibility, vulnerability scanning và build trong môi trường cấp quyền; nếu không có runtime nói rõ là mới sinh mã/chưa kiểm thử.
5. Tạo hướng dẫn cài, env-example không chứa secrets, README, license rõ, migration, backup, deployment và rollback.

## Bàn giao
Repo mới, ma trận tính năng, test report thực tế và bảng "đã làm / chưa làm / rủi ro". Mọi lời khẳng định ứng dụng chạy phải gắn với log kiểm thử.
