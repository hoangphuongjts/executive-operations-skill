---
name: app-rebuild-router
description: "Dùng khi người dùng muốn nhân bản, dịch ngược hợp pháp, phân tích hoặc viết lại ứng dụng/phần mềm thuộc bất kỳ nền tảng nào."
---

# Điều phối dự án tái xây dựng phần mềm

## Vai trò
Nhận đầu vào: URL, ảnh chụp, video thao tác, mã nguồn được phép, bản binary/APK/IPA/EXE, tài liệu API hoặc đặc tả. Phân tích và tái xây dựng bản mới có kiểm soát thay vì hứa hẹn sao chép nguyên mã nguồn.

## Quy trình bắt buộc
1. Nhận diện nền tảng và hiện vật. Đánh dấu nguồn chứng cứ: **quan sát trực tiếp**, **mã nguồn được phép**, **đặc tả/tài liệu**, **giả định**; không biến giả định thành sự thật.
2. Xác nhận phạm vi quyền: do người dùng sở hữu, giấy phép nguồn mở, được chủ sở hữu cho phép, hoặc chỉ phân tích hành vi công khai để thiết kế giải pháp độc lập. Nếu thiếu quyền sao chép, không trích xuất/đưa lại tài sản độc quyền. Luôn tôn trọng điều khoản sản phẩm và luật hiện hành.
3. Tách ba hướng: (A) fork/chỉnh sửa mã có giấy phép phù hợp, (B) clean-room viết lại hành vi đã quan sát hợp pháp, (C) xây sản phẩm cùng bài toán với thiết kế gốc. Chọn hướng ít rủi ro nhất, hỏi tối đa một câu khi thiếu dữ kiện quyết định.
4. Phân loại: web -> web-rebuild; Android -> android-rebuild; iOS/iPadOS -> ios-rebuild; desktop/binary -> desktop-rebuild; game/extension -> game-extension-rebuild; API/hệ thống dữ liệu -> api-data-rebuild.
5. Tạo **App Reconstruction Brief**: mục tiêu, hệ điều hành, loại đầu vào, quyền, đối tượng người dùng, ảnh và màn hình, luồng chức năng, dữ liệu, đăng nhập, phụ thuộc, API, các điểm chưa xác minh, rủi ro, giới hạn.
6. Lập ma trận tính năng P0/P1/P2, user journey, sơ đồ màn hình, sơ đồ dữ liệu; đề xuất stack và tách bản MVP có thể kiểm thử.
7. Giao phần viết lại cho clean-room-build; đánh giá bởi release-verification. Ưu tiên tái sử dụng Skill Superpowers, AI Coding, GitHub khi có.
8. Trước mọi thao tác cài phần mềm/chạy binary/upload/ghi đè/đẩy public, xác nhận quyền công cụ thực tế. Không tự báo "đã cài", "đã dịch ngược", "đã chạy" nếu chưa có bằng chứng.

## Mẫu đầu ra
- Loại phần mềm + mức xác định
- Quyền được phép + giới hạn
- Bảng hiện vật/chứng cứ
- Danh sách màn hình và tính năng, đánh dấu chắc chắn/chưa xác minh
- Hai hoặc ba hướng tái xây dựng, lợi ích và đánh đổi
- Dự kiến stack, module, kế hoạch kiểm thử và bước tiếp theo

Không yêu cầu cung cấp mật khẩu, cookie phiên, khóa riêng, dữ liệu cá nhân để phân tích. Nếu một mẫu thực thi không tin cậy, dùng môi trường cách ly và chỉ đọc tĩnh khi phù hợp.
