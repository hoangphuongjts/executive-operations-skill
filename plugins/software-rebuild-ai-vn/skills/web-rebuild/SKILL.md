---
name: web-rebuild
description: "Dùng khi cần phân tích và tái xây dựng website, web app, SaaS, PWA hoặc giao diện web từ URL, screenshot và hành vi hợp pháp."
---

# Tái xây dựng web app

## Khảo sát
- Xác định URL được phép truy cập, trang public/private, vai trò người dùng, mobile/desktop, luồng điều hướng và trường hợp lỗi.
- Dùng trình duyệt/DevTools được kết nối để xem DOM hiển thị, CSS, accessibility tree, request network được phép, cấu trúc routing, responsive; chỉ xem dữ liệu và phiên mà người dùng có quyền.
- Ghi màn hình, sơ đồ component, token màu/chữ/khoảng cách, trạng thái empty/loading/error, hành vi bàn phím và accessibility.
- Không khai thác lỗ hổng, không vượt xác thực/paywall/DRM, không lấy bí mật từ bundle, không sao chép logo, hình, font hay văn bản được bảo hộ nếu thiếu giấy phép.

## Viết lại
- Tạo bản PRD và ma trận tính năng; chọn Next.js/React/Vue/Svelte hoặc công nghệ người dùng hiện có, không tự ý đổi stack dự án đang vận hành.
- API, cơ sở dữ liệu, đăng nhập và phân quyền phải được định nghĩa độc lập từ thông tin hợp pháp; không giả định endpoint ẩn là giao diện công khai.
- Triển khai bằng component có thể tái sử dụng, thiết kế riêng biệt khi chưa có quyền sao chép UI.
- Kiểm thử Playwright: navigation, auth, validation, mobile viewport, form, accessibility; so sánh tính năng chứ không mặc định yêu cầu sao chép pixel-perfect.

## Bàn giao
Sitemap, user-flow, component tree, data model, API contract, repo/source gốc mới, báo cáo screenshot và test checklist. Phải phân biệt mockup và ứng dụng chạy thật.
