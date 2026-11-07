---
name: toolchain-guidance
description: "Dùng khi cần lựa chọn và hướng dẫn cài công cụ phân tích ứng dụng trên Windows, macOS hoặc Linux theo nguồn chính chủ."
---

# Toolchain theo môi trường

1. Hỏi/chọn môi trường phù hợp: Windows 11, macOS, Linux, VM/Android emulator, thiết bị thử. Đọc danh mục `references/official-tools.md` trong skill này.
2. Đối chiếu tool với file đầu vào, phụ thuộc, giấy phép, phiên bản hiện hành tại trang chính chủ. Không tự tải binary từ nguồn lạ, không chạy script chưa thẩm định.
3. Trình tự: tải chính chủ -> kiểm tra release/chữ ký/hash nếu có -> cài dependency -> mở trong VM/sandbox -> thử với mẫu mình sở hữu -> ghi phiên bản/log.
4. Không đề xuất cài mọi tool một lượt; chọn đúng 1-3 công cụ cho định dạng thực tế, tránh phung phí RAM/đĩa.
5. Trước cài remote connector/MCP/OAuth, xác minh endpoint thật, scope, dữ liệu và phí; không dựng endpoint giả để tuyên bố tích hợp.
6. Cần máy Windows/macOS thực tế để dịch ngược hoặc build trên máy người dùng; plugin ChatGPT này chỉ hướng dẫn/điều phối, không cài phần mềm lên OS hoặc tích hợp runtime tự động.
7. Cần Xcode/macOS để build và ký iOS. Android Studio/Java có yêu cầu tương thích, đọc tài liệu chính thức trước khi cài.
