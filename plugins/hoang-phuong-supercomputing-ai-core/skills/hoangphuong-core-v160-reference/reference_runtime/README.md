# Hoàng Phương Supercomputing Core — v15.2 → v16.0

**Bộ triển khai mẫu an toàn (additive prototype)**, không phải bản nâng cấp đã được cài vào tài khoản ChatGPT. Mục tiêu: có thể chạy offline trên Windows/macOS/Linux với Python >=3.10 và chỉ dùng thư viện chuẩn cho runtime. **Plugin gốc v15.1.3 vẫn nguyên vẹn.**

## Khởi chạy nhanh (không cài đặt package)
```bash
cd HP_Core_v15_2_to_v16_0
PYTHONPATH=src python -m hpcore.cli doctor
PYTHONPATH=src python -m hpcore.cli plan --task "kiểm thử API"
# Kết quả mặc định: BLOCKED do kill switch bật
PYTHONPATH=src python -m hpcore.cli plan --enable-local-plan --task "kiểm thử API"
PYTHONPATH=src python -m hpcore.cli audit-verify
```
Windows PowerShell: thay `PYTHONPATH=src` bằng `$env:PYTHONPATH='src';` trước lệnh `python`.

## Kiểm thử và benchmark
```bash
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python benchmarks/run_benchmark.py benchmark_results.json
```

Các lệnh tạo file audit `.sqlite3` tại thư mục hiện hành; benchmark tạo JSON report. Không có kết nối mạng, không gọi LLM, không chạy script bên ngoài.

## Hồ sơ bàn giao
- `docs/ARCHITECTURE.md`: sơ đồ, kiến trúc, roadmap, hợp đồng tích hợp, release gates.
- `docs/SECURITY_AUDIT.md`: kiểm toán và lỗ hổng cần khắc phục.
- `src/hpcore/core.py`: policy, router, orchestration cục bộ, audit, registry.
- `tests/test_core.py`: tests hành vi an toàn.
- `benchmarks/run_benchmark.py`: benchmark synthetic, có kết quả trong `reports/` sau khi chạy.
- `configs/runtime.example.json`: cấu hình chuẩn mặc định khóa.

## Không có những gì?
Không có bản sao Skill gốc, 128 agent runtime độc lập, 500 GitHub repo đã cài, API server production, giao diện desktop/mobile, connector credentials, integration token, hạ tầng nền hoặc benchmark độc lập thực tế. Không sử dụng prototype này để tự động gửi/xóa/trả tiền.

## Bảo toàn hệ thống gốc
Không ghi vào bất kỳ plugin ChatGPT nào. Muốn tích hợp sau này: cấp bản nguồn gốc hoặc kết nối công cụ cho phép đọc; so hash & kiểm thử hồi quy; chỉ tích hợp thông qua lớp adapter mới và giữ rollback. Không viết đè plugin gốc.
