---
name: release-verification
description: "Dùng khi kiểm tra quyền sở hữu, giấy phép, bảo mật, chất lượng và độ hoàn chỉnh trước khi công bố ứng dụng tái tạo."
---

# Kiểm định trước bàn giao

## Quyền và giấy phép
- Phân biệt học hỏi ý tưởng/chức năng với sao chép biểu đạt, mã nguồn, asset, thương hiệu, dữ liệu và kỹ thuật bảo vệ.
- Ghi bằng chứng quyền phân tích/phân phối. Kiểm tra SPDX license của dependency, asset, model; các giấy phép GPL/AGPL có điều kiện phân phối riêng.
- Dừng phần rủi ro: xâm nhập trái phép, phá DRM/license/anti-cheat, lấy secret, dữ liệu riêng tư, giả mạo ứng dụng hoặc phát tán bản sao trái phép.

## An toàn
- Kiểm tra static dependencies, lỗ hổng, runtime sandbox, malware trong đầu vào, SBOM, quyền file; không mặc định chạy file được đưa vào.
- Xác định đường dữ liệu cá nhân, mật mã, token, logs, auth/session, lưu trữ và backup. Không yêu cầu credentials qua chat.

## Chất lượng
- Chứng minh test bằng log; test trên phiên bản OS và thiết bị xác định.
- Ma trận feature parity: parity đạt / khác thiết kế / chưa thể xác minh. Không dùng từ "giống 100%" nếu thiếu bằng chứng.
- Bảo đảm installer/build, screenshot, build reproducibility, kiến trúc, README, rollback và provenance.

## Format kết luận
`Đã có bản thiết kế`, `Đã tạo mã`, `Đã build`, `Đã kiểm thử`, `Chưa có runtime` là các mức riêng biệt. Đính kèm danh sách blocker, không suy đoán thành công.
