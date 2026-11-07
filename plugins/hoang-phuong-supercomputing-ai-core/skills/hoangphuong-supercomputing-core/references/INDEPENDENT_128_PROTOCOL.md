# v14.0 — 128 Independent Research-Agent Protocol

## Mục tiêu và định nghĩa kiểm chứng

Mỗi agent ID 001–128 có **hồ sơ nghiên cứu và prompt riêng**, **chuyên ngành**, **nhiệm vụ**, **4 giai đoạn rèn luyện chuyên sâu**, **bài kiểm định chuyên ngành**, **ngữ cảnh và không gian bộ nhớ cách ly**, **lệnh gọi độc lập**. Python runtime dùng được trên máy có Python 3.10+; chỉ kết nối API khi người vận hành bật `--execute`. Có thể gọi nhiều agent qua lệnh team với số lượng và mức song song hạn chế.

**Không đánh đồng** với 128 bộ trọng số LLM được fine-tune, 128 kết nối cloud đang chạy, 128 chuyên gia có bằng tiến sĩ, hay 128 chủ thể AI suy nghĩ độc lập. Cách gọi "nghiên cứu trình độ tiến sĩ" là **mục tiêu chuẩn phương pháp**, phải được kiểm chứng bởi chuyên gia ngành trên bài đánh giá độc lập, không tự chứng nhận.

## Phân bổ lĩnh vực

16 lĩnh vực × 8 agent: phương pháp khoa học; kiến trúc; kỹ thuật phần mềm; kiểm thử; HPC; lượng tử/mật mã; AI/thuật toán; vận hành; UX/sản phẩm; dữ liệu; hệ đa-agent; bảo mật; nội dung/đa phương thức; tài chính; CAD/IoT; đánh giá chất lượng. Mỗi agent giữ nguyên ID và tên v13.2.

## Đào tạo và đánh giá (chưa thực hiện fine-tuning)

1. **Foundation:** Nắm nguồn học thuật có quyền sử dụng, phương pháp nghiên cứu ngành, giới hạn tri thức.
2. **Specialization:** Xây bộ nhiệm vụ cụ thể theo `mission` và điều kiện bác bỏ.
3. **Empirical research:** Có đối chứng, dữ liệu được cấp quyền, tái lập, kiểm tra nguồn và sai số.
4. **Expert panel:** Giám khảo chuyên môn đánh giá trên tập độc lập, sửa sai, tái đánh giá và chỉ khi có chứng cứ mới công bố năng lực.

Mỗi hồ sơ có `evaluation.case_id`, `task`, `expected_evidence`, `rubric` (100 điểm) và **`review_status: not_evaluated`**. Ngưỡng 85 chỉ là mục tiêu đề xuất, không phải điểm đã đạt. Không cung cấp corpus có bản quyền khi chưa xác nhận giấy phép. Dữ liệu đào tạo muốn được sử dụng phải có `agent_id`, `question`, `reference_answer`, `source_license`, `reviewer_id`, `split`; lệnh audit chỉ kiểm tra cấu trúc và rò rỉ trùng câu, không xác thực bản quyền.

## Lệnh chạy cục bộ

Giải nén **toàn bộ plugin** có 7 Skill và manifest, sau đó ở thư mục gốc:

```bash
python skills/hoangphuong-supercomputing-core/scripts/independent_agents.py validate
python skills/hoangphuong-supercomputing-core/scripts/independent_agents.py list --group 4
python skills/hoangphuong-supercomputing-core/scripts/independent_agents.py inspect --id 28
python skills/hoangphuong-supercomputing-core/scripts/independent_agents.py eval-plan --id 28
python skills/hoangphuong-supercomputing-core/scripts/independent_agents.py run --id 28 --task "Đánh giá tính đúng và đưa phản ví dụ"
python skills/hoangphuong-supercomputing-core/scripts/independent_agents.py team --ids 1,28,64 --task "Phân tích phương pháp nghiên cứu"
python -m unittest discover -s skills/hoangphuong-supercomputing-core/scripts -p 'test_*.py' -v
```

Mặc định là **dry-run** và không dùng API, không tốn credits.

## Gọi model thực qua API đã được cho phép

Sử dụng endpoint HTTPS **tương thích Chat Completions**, không được lẫn URL nhà cung cấp khác API chuẩn. Người vận hành tự cấp biến môi trường, không đưa khóa vào log/code hoặc gửi khóa vào ChatGPT. Chỉ bật khi đã phê duyệt dữ liệu và chi phí.

```bash
# Minh họa tên biến môi trường, không chứa API key thật
export AGENT_ALLOWED_HOSTS="api.example-llm.com"
export AGENT_API_KEY="YOUR_SECRET_FROM_VAULT"
python skills/hoangphuong-supercomputing-core/scripts/independent_agents.py run \
  --id 28 --task "Rà soát giả thuyết A theo phép thử B" --execute \
  --endpoint "https://api.example-llm.com/v1/chat/completions" \
  --model "APPROVED_MODEL" --max-output 256 --timeout 30
```

Có thể dùng `team --ids 1,28,64 --parallel 2 --max-calls 3` cùng tham số `--execute` để gọi từng agent được chọn. Dù chia một endpoint mô hình nền, mỗi agent vẫn có system prompt và phiên làm việc riêng. Khuyến cáo không chọn 128 cùng lúc; tối đa 8 agent/lệnh team, 4 luồng, tối đa 8 lần gọi, không cấp tools/function calling. Không tự động đăng bài, mua hàng, giao dịch, ghi tệp nhạy cảm, học từ bí mật, hoặc vượt giới hạn đã cấp.

## Bộ nhớ tách biệt

Lệnh `run --id 28 ... --execute --persist --memory-dir ./secure-memory` mới cho phép ghi lịch sử local tối đa 6 lượt trong tệp `agent-028.json`; mặc định không ghi. Memory có thể chứa dữ liệu nhạy cảm: nên bật mã hóa ổ đĩa, giới hạn quyền OS, xóa thủ công khi không cần. Lệnh team không hỗ trợ ghi nhớ để tránh tranh chấp bộ nhớ và trộn phiên.

## Kiểm soát và tiêu chí đạt thật

- **Đã đóng gói:** cấu hình 128 agent, chương trình huấn luyện mẫu, CLI và unit tests.
- **Đã kiểm thử:** chỉ các test thực sự chạy được ghi bằng log; mock API không xác nhận mô hình thật.
- **Chưa xác nhận:** độ chính xác chuyên môn từng agent; thực thi với API thật; khả năng học sau đào tạo; 128 dịch vụ độc lập; tiêu chuẩn tương đương tiến sĩ.
- **Muốn chuyển cấp:** kết nối runtime đã kiểm soát, cung cấp nguồn hợp pháp, đánh giá bởi chuyên gia có chuyên môn, đo tỷ lệ đúng theo nhóm, kiểm tra bịa nguồn, ứng xử an toàn, khả năng tái lập và tổng chi phí.

**Mô hình phản biện:** Trước khi ra quyết định, chọn 1 specialist + 1 independent reviewer + 1 integrator nếu cần. Tất cả nhận cùng task nhưng lịch sử không được tự động chia sẻ. Không gọi đó là bằng chứng nhiều mô hình thật khác nhau khi dùng một provider/model.
