# v13.2 — 128 Agent Orchestration Protocol

## Danh mục và ý nghĩa
- 128 **vai trò logic** gồm 01–64 bất biến, 65–128 bổ sung. `AGENTS_128.json` là machine-readable registry, không phải 128 API keys hay tiến trình thực thi.
- Chức năng lõi đã đóng gói: `validate` kiểm tra cấu trúc, `catalog` xem vai trò, `plan` định tuyến không gọi API, `benchmark-routing` đo microbenchmark định tuyến, `run` mặc định xem trước, `run --execute` kết nối ngoài khi chủ động.
- Không tự cài model, kết nối cloud, tạo dịch vụ nền, khởi chạy 128 agent hoặc yêu cầu người dùng trả phí.

## Định tuyến
- Chọn tối đa 4–8 vai trò theo từ khóa có dấu tiếng Việt hoặc tiếng Anh; luôn có 57 planner, 32 independent reviewer, 64 integrator. Bộ chọn chỉ là heuristic tham khảo, phải đánh giá riêng trên nhãn thực tế.
- Luồng: input -> planner -> specialists (max 5) -> auditor -> integrator -> output, không tự gọi lại đệ quy.
- Có thể thay bộ chọn bằng eval/ranker đã kiểm chứng sau khi thu thập dữ liệu, song không tự kết luận định tuyến chính xác.

## Runtime ngoại vi có điều kiện

```bash
python skills/hoangphuong-supercomputing-core/scripts/swarm128.py validate --root .
python skills/hoangphuong-supercomputing-core/scripts/swarm128.py catalog --root . --group 12
python skills/hoangphuong-supercomputing-core/scripts/swarm128.py plan --root . --task "Xây dựng ứng dụng quản lý trại 3D có kiểm thử" --max-roles 6
python skills/hoangphuong-supercomputing-core/scripts/swarm128.py benchmark-routing --root . --iterations 300
python -m unittest discover -s skills/hoangphuong-supercomputing-core/scripts -p 'test_*.py' -v
```

**Chỉ khi đã được phép dùng endpoint và có đủ ngân sách, người vận hành có thể chọn thực thi:**

```bash
# AGENT_API_KEY chỉ đặt trong môi trường shell, không ghi vào file plugin hoặc log
python skills/hoangphuong-supercomputing-core/scripts/swarm128.py run --root . \
  --task "Lập kế hoạch kiểm thử ứng dụng" --max-roles 5 --execute \
  --endpoint https://YOUR-MODEL-PROVIDER/v1/chat/completions \
  --model YOUR_APPROVED_MODEL --max-output-tokens 256 --max-calls 5
```

Chương trình gọi vai trò 57 (planner), các vai trò chuyên sâu, vai trò 32 (auditor), sau đó vai trò 64 (integrator) để tích hợp. Cho phép chọn trực tiếp một vai trò bất kỳ 1..128 với `--role-ids 128` (tự thêm các vai trò lõi). Chỉ hỗ trợ API tương thích `chat/completions` trả `choices[0].message.content`; các API khác cần adapter riêng. Số tác tử được sử dụng phụ thuộc ngân sách và giới hạn; không tự động kết nối toàn bộ 128.

## Bảo vệ và nghiệm thu
- Thực thi bên ngoài chỉ sau `--execute`, URL HTTPS, lựa chọn model; API key từ env; không tự gửi dữ liệu nhạy cảm nếu người dùng chưa cho phép.
- Đặt timeout, giới hạn số lần gọi (4–8), giới hạn mỗi lần xuất token, chặn redirect khác host; không có tools/functions được chuyển cho endpoint, không cấp quyền ghi file hoặc chạy shell.
- Khuyến nghị cung cấp benchmark với tập tác vụ độc lập, số agent thực gọi, token/cost do nhà cung cấp báo, tỷ lệ lỗi và toàn bộ trace đã ẩn thông tin nhạy cảm.
- Phân biệt `declared`, `bundled_testable`, `locally_verified`, `external_runtime_connected`. Không nâng trạng thái chỉ vì script tồn tại hoặc bản patch đã phát hành.
- Khi triển khai dịch vụ thật phải có kiểm soát RBAC/secret management/rate limit/tính sẵn sàng ở hạ tầng riêng.
