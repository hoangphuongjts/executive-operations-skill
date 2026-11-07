# Kiểm toán staging — Revidapi-com/revidapi-reup-video

Nguồn: `https://github.com/Revidapi-com/revidapi-reup-video`  
Commit tham chiếu từ GitHub: `9e2cc61e58fdad71194ce0f1e1b5452b777c4853`.  
Đã xem các tệp `reup/an_toan.py`, `api.py`, `cli.py`, `dung.py`, `ffprobe_thay.py`,
`giong.py`, `hieu_ung.py`, `kich_ban.py`, `phan_tich.py`, `__init__.py`,
ba tệp `tests/`, `pyproject.toml`, `requirements.txt`, `README.md` và `LICENSE`.
Giấy phép: MIT. Phụ thuộc khai báo: `faster-whisper>=1.0`,
`opencv-python-headless>=4.8`, `certifi` (dependency trực tiếp trong pyproject).
Các dependency transitives và CVE CHƯA được kiểm toán.

## Phát hiện
1. [HIGH] CLI `chay` gọi `kich_ban.viet()` (tạo request chat) trước khi hỏi `--dong-y`.
2. [HIGH] CLI `phan-tich` có thể tải từ URL qua `lay_mau` và dùng RevidAPI.
3. [MED] `an_toan.kiem_url_media` kiểm tra DNS trước kết nối; còn rủi ro DNS rebinding/TOCTOU.
4. [MED] `hieu_ung.cai` gọi script setup bên ngoài; commit ghim không đồng nghĩa an toàn tuyệt đối.
5. [MED] Dependencies dùng version range; thiếu lockfile + SBOM + CVE verification.
6. [MED] `hieu_ung.doc_ke_hoach` chuyển thành float, cần từ chối NaN/Infinity.
7. [MED] `tai_file` có thể để lại file `.tai` khi header Content-Length vượt trần hoặc mạng lỗi.
8. [LOW] `cli.main` không bắt `subprocess.CalledProcessError` thành lỗi CLI thân thiện.

## Bảo vệ hiện có
- `api._goi` dùng HTTPS fixed host, từ chối redirect khi mang key.
- `an_toan` hạn chế URL/file size, che key, dùng argv FFmpeg thay vì shell.
- `dung._ass_chu` lọc chuỗi để tránh chèn ASS tags.
- Kịch bản được giới hạn số đoạn và độ dài.

## Phạm vi bản vá
`adapter/patch_upstream.py` dự kiến thêm chốt API vào source upstream khi checkout thực
được truy cập với quyền. Trong phiên này chỉ chạy kiểm thử trên checkout giả lập;
KHÔNG chép, vá, hay chạy engine upstream thực. Bản vá CLI intentionally fail-closed:
tắt toàn bộ lệnh upstream khi chưa xác nhận quyền API. Dựng offline dùng adapter riêng.

## Kết quả kiểm chứng
5 unittest PASS; FFmpeg smoke render 1080x1920@30fps H264/AAC PASS.
Không có lệnh gửi RevidAPI hoặc sử dụng key. Đây không phải chứng minh
chặn egress ở cấp hệ điều hành; cần kiểm thử firewall/network namespace khi triển khai.
