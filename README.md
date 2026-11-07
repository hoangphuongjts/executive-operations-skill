# Hoàng Phương — ChatGPT Skill / Plugin / Agent Portable (STAGING)

**Kho Git nguồn để sao lưu và tái cài đặt có kiểm chứng**, không phải một plugin tự hoạt động khi clone. Bản nguồn dùng **Core v16.0.50** và 17 plugin riêng (16 ZIP ứng viên, 1 App/Site account-bound).

> 🔒 **PRIVATE ONLY:** Repository dự kiến `hoangphuongjts/hoangphuong-chatgpt-portable`. Không công khai mã nội bộ hoặc bí mật. Không có OAuth token, API key hay việc tự động cấp quyền.

## Thư mục

| Đường dẫn | Nội dung |
|---|---|
| `plugins/` | Mã nguồn văn bản và cấu hình đã giải nén từ 16 ZIP ứng viên; dễ kiểm diff/review | 
| `packages/` | 16 ZIP ứng viên để nhập từng plugin qua ChatGPT Plugin Creator | 
| `migration/MANIFESTS/` | 17 plugin, phiên bản, thứ tự nhập |
| `migration/RECONNECT/` | Ma trận OAuth/MCP, hướng dẫn kết nối lại tài khoản đích |
| `migration/REPORTS/` | Kết quả QA staging và giới hạn thật |
| `migration/TESTS/` | Bộ test offline từ gói ban đầu |
| `archive/` | Gói staging v2 nguyên bản làm điểm khôi phục |
| `scripts/` | Bộ kiểm tra độc lập và script PowerShell tạo repository riêng tư |
| `docs/` | Hướng dẫn cài ChatGPT, GitHub, bảo mật, xuất xứ |

## Thao tác nhanh

```bash
python scripts/VERIFY_REPO.py
python scripts/CHECK_PACKAGES.py
```

Trên Windows (đã cài Git, GitHub CLI và Python 3), **nhấp đúp `CHAY_TAO_REPO_GITHUB.cmd`** để đăng nhập GitHub bằng trình duyệt, chạy QA và tạo/push repo private khi bạn gõ xác nhận `TAO`. Hoặc dùng PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\PUBLISH_PRIVATE_GITHUB.ps1
```

Xem [cài đặt GitHub](docs/GITHUB_SETUP_VI.md), [cài đặt ChatGPT](docs/INSTALL_ON_CHATGPT_VI.md) và [bảo mật](docs/SECURITY_PRIVACY.md).

## Bằng chứng & giới hạn

- Gói STAGING v2 đã báo cáo `1749/1749` kiểm thử **tĩnh**; bộ `CHECK_PACKAGES.py` có thể chạy lại nguyên trạng qua thư mục tạm.
- Core đã công bố 92 skill, 128 hồ sơ agent, 108 mã gốc, 16 cụm. Đây không phải 128 runtime agent độc lập.
- Tài khoản ChatGPT nguồn đã thấy 193/197 Skill portable; riêng Core 92/92. Tài khoản đích **chưa thử cài**.
- Nango, Google và Ebook Library cần xác thực/host runtime riêng; 1 App/Site không portable bằng ZIP.
- 7 tệp `.pyc` không có trong bản sao văn bản. Không tuyên bố byte-for-byte đầy đủ hay hoạt động 100%.
- **Không có GitHub Actions tự chạy**, không sửa plugin production và không phát sinh chi phí API.
