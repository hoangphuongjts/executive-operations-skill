---
name: game-extension-rebuild
description: "Dùng khi cần tái xây dựng game, tiện ích mở rộng trình duyệt, plugin của ứng dụng khác hoặc phần mềm nhúng được phép."
---

# Game, extension, tiện ích, embedded

## Phân loại
- Game Unity/Unreal/Godot/mobile/PC: hệ thống scene, input, camera, gameplay loop, physics, save states, performance và asset ownership.
- Browser extension: manifest MV3, content script, background service worker, permissions, UI popup/options, browser store policy.
- Embedded/firmware/IoT: kiến trúc CPU, giao thức phần cứng, tài liệu chip, firmware license, cập nhật an toàn và chạy trong môi trường cô lập; không áp dụng công cụ desktop một cách máy móc.

## Chuẩn tái xây dựng
- Quan sát hành vi hợp pháp và thiết kế gameplay/UX tương đương về bài toán, không sao chép artwork, âm thanh, nhân vật, level hay nhãn hiệu chưa được cấp phép.
- Không phá anti-cheat, license enforcement, DRM hay bypass biện pháp truy cập/bảo mật.
- Xây nguyên mẫu lõi đơn giản; kiểm tra latency, accessibility, offline/sync và tính tương thích thiết bị.
- Với firmware/công nghiệp, không thử binary hay flash lên thiết bị thật trước khi có môi trường lab và kế hoạch phục hồi.

## Deliverables
Functional spec, assets license manifest, test sandbox plan, clean-room architecture và source cho thành phần người dùng có quyền triển khai.
