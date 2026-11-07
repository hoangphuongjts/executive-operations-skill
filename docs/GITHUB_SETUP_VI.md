# Xuất bản lên GitHub (Private, không tính phí)

**Đích dự kiến:** `hoangphuongjts/hoangphuong-chatgpt-portable`.
**Trạng thái:** Không tự nhận đã tạo GitHub repository. Bộ nguồn đang là Git repo local cho tới khi `gh repo view` xác nhận remote.

## Cách nhanh trên Windows

1. Cài [Git](https://git-scm.com/downloads) và [GitHub CLI](https://cli.github.com/), bằng nguồn chính thức. Không cần token đưa vào ChatGPT.
2. Mở PowerShell trong thư mục repository, chạy `gh auth login`, chọn HTTPS và đăng nhập tài khoản GitHub của chính bạn qua trình duyệt.
3. Nhấp đúp file `CHAY_TAO_REPO_GITHUB.cmd` để chạy kiểm tra và tạo repo Private, hoặc chạy `powershell -ExecutionPolicy Bypass -File .\scripts\PUBLISH_PRIVATE_GITHUB.ps1`.
4. Chương trình xác minh GitHub login, repository riêng tư và hỏi xác nhận bằng chữ **TAO** trước khi tạo/push. Không tự động đổi quyền repo đang có.
5. Sau khi xong, xem repository bằng `gh repo view hoangphuongjts/hoangphuong-chatgpt-portable --web`.

## Không có GitHub CLI?

- Vào https://github.com/new bằng tài khoản `hoangphuongjts`.
- Name: `hoangphuong-chatgpt-portable`. Chọn **Private**. Đừng tạo README/.gitignore/LICENSE tự động vì repo local đã có.
- Mở terminal trong thư mục repo này và chạy:

```powershell
git remote add origin https://github.com/hoangphuongjts/hoangphuong-chatgpt-portable.git
git push -u origin main
```

Không đăng công khai khi chưa kiểm toán nguồn và giấy phép. **Không** bật tự động hóa Actions hoặc dịch vụ tính phí.
