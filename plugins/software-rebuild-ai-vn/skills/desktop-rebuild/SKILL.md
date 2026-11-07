---
name: desktop-rebuild
description: "Dùng khi phân tích hợp pháp và tái xây dựng EXE, DLL, MSI, MSIX, DMG, APP, ELF, DEB, RPM, ứng dụng desktop .NET, Electron hoặc native."
---

# Windows/macOS/Linux desktop -> đặc tả -> phần mềm mới

## Nhận dạng trước khi chọn tool
- PE/.exe/.dll: .NET? -> ILSpy; native C/C++/Rust/Go -> Ghidra khi có quyền và sandbox. Không có công cụ chung khôi phục C++ nguyên bản.
- Electron: nếu nguồn/package cho phép, kiểm tra ASAR và JavaScript/HTML; nêu giới hạn source map, bundling.
- macOS .app/.dmg: nhận dạng Mach-O và entitlement; Linux ELF/AppImage/DEB/RPM: package metadata, thư viện và giao diện, với permission phù hợp.
- Unity/games và browser extensions -> skill game-extension-rebuild.

## Quy trình
1. Kiểm kê nguồn, hash, chữ ký, license, hành vi hệ thống, installer, quyền admin và kết nối mạng; ưu tiên tĩnh, cô lập mẫu không tin cậy.
2. Quan sát các luồng UI và hệ thống: menu, file open/save, trình in, thiết bị ngoại vi, setting, auto-update, databases và lỗi.
3. Lập sơ đồ module, I/O, dependencies; xuất bảng dữ liệu cần di chuyển với quyền hợp pháp; tránh đưa secrets và mã độc vào repo mới.
4. Đề xuất stack phù hợp: .NET/WPF/WinUI, Electron/Tauri, Qt, Swift, GTK hoặc native; ưu tiên stack người dùng sở hữu.
5. Viết lại từ đặc tả và quan sát hợp pháp, không patch DRM/check bản quyền, không nhúng chữ ký/chứng chỉ/hình ảnh có bản quyền không phép.
6. Test package/installer trên VM mới, chạy smoke tests và kiểm tra code signing, cập nhật và rollback.

## Đầu ra
Dấu vết kỹ thuật, ma trận chức năng, kiến trúc, kế hoạch build, test các hệ điều hành thực sự đã thử; không tuyên bố hỗ trợ mọi OS nếu chưa thử.
