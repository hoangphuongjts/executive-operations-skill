---
name: android-rebuild
description: "Dùng khi tái xây dựng ứng dụng Android APK/AAB/DEX hoặc mã Kotlin/Java mà người dùng có quyền phân tích."
---

# Android APK/AAB -> đặc tả -> app mới

## Đầu vào và công cụ
- Android Studio/ADB với thiết bị kiểm thử được phép.
- JADX để đọc mã Java tái dựng và manifest; Apktool cho resource/smali khi có quyền; MobSF cho kiểm tra bảo mật. Các công cụ này cần máy ngoài ChatGPT và có giấy phép riêng.
- Các công cụ decompiler có thể lỗi và mất tên biến, type, comment, logic tối ưu hóa. Không coi mã dịch ngược là source gốc hoặc bản build sẵn.

## Các bước
1. Kiểm tra định dạng, hash, nguồn gốc và quyền; đánh dấu bản dùng để phân tích, không chạy binary lạ trên máy chính.
2. Quan sát UI và chức năng trên thiết bị thử được phép; liệt kê màn hình, trạng thái, quyền Android, notification, offline behavior, deep link, file storage.
3. Chỉ phân tích static những thành phần được phép; không lấy/khôi phục khóa ký, secret, token hay dữ liệu riêng của người khác.
4. Lập data-flow, use case, dependency map; đánh dấu API quan sát được vs giả định. Không bypass certificate pinning, DRM, license check hay attestation.
5. Viết lại clean-room bằng Kotlin/Jetpack Compose hoặc stack phù hợp; API phải có xác thực và lưu trữ an toàn.
6. Kiểm thử emulator và thiết bị thật: các luồng chính, quyền, offline, performance, accessibility, app-signing riêng.

## Đầu ra
Bảng tính năng, màn hình, manifest quyền, module kiến trúc, API, test plan, mã nguồn mới nếu công cụ lập trình được cấp quyền. Không ký hoặc phân phối lại APK gốc của bên khác.
