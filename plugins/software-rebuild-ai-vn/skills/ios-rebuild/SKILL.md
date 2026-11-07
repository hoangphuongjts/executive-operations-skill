---
name: ios-rebuild
description: "Dùng khi phân tích hợp pháp và tái xây dựng ứng dụng iOS/iPadOS từ IPA, video, tài liệu hoặc Swift source."
---

# iOS/iPadOS -> đặc tả -> ứng dụng mới

- Xác minh quyền sở hữu hoặc giấy phép trước khi phân tích IPA; không hướng dẫn bẻ khóa hệ thống, vượt mã hóa/DRM, tháo certificate pinning hoặc trích xuất dữ liệu người khác.
- Quan sát UI, navigation, gestures, background modes, notifications, entitlement, deep links, privacy prompts, App Store constraints; ghi lại bằng ảnh/video được phép.
- Với mã nguồn hợp pháp: đọc project Xcode, Swift/Objective-C, Info.plist, dependency; với IPA không có source: nêu rõ giới hạn, chỉ khảo sát điều được quyền xem.
- Đề xuất SwiftUI/UIKit hoặc Flutter/React Native nếu cần đa nền tảng; thiết kế mô hình dữ liệu và API độc lập.
- Xây clean-room; dùng identity, app identifier và certificate riêng của người dùng; không sao chép signing assets hay bí mật.
- Kiểm thử trên Simulator và thiết bị của người dùng (khi có môi trường macOS/Xcode); kiểm tra Apple privacy, accessibility, offline và TestFlight/App Store khi được phê duyệt.
- Báo rõ phần nào chưa thể kiểm chứng nếu không có macOS, thiết bị hoặc quyền developer.
