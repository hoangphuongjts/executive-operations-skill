# Giai đoạn kế tiếp: từ MVP tới Agent có LLM thật

## Capability matrix

| Năng lực | MVP này | Hướng kế tiếp |
|---|---|---|
| Inventory | Scan local top-level SKILL.md | Repo graph + plugin registry API |
| Diagnose | Deterministic metadata heuristics | Human-labelled evals + trace quality |
| Research | Explicit public GitHub metadata | Source reviews + licensed references + citations |
| Propose | Known documentation-only patch | AI drafts in sandbox with offline deterministic checks |
| Verify | Hash + unit/integration tests | Independent eval, provenance and model-graded with human review |
| Apply | Explicit local file only | CI-gated plugin release with release ID + approval |
| Rollback | Hash-bound local backup | Plugin release rollback and provider health check |
| Scheduler | Manual invocation | Windows Task Scheduler / trusted service, read-only cycle by default |

## Production gate

1. Thẩm định tất cả đầu vào mô hình như dữ liệu không tin cậy (prompt injection).
2. Khóa quyền đọc, quyền ghi, network egress, budget và max concurrent tasks.
3. Phê duyệt từng hành động nguy hiểm theo ngữ cảnh; chặn escalation qua công cụ khác.
4. Bài thử chuyên môn độc lập, test hồi quy, negative tests, kiểm toán dependency/license.
5. Observability và kill switch ở backend thực, không chỉ trong prompt.
6. Git rollback kèm snapshots, release IDs và chính sách secrets.

## Lộ trình incremental

- v0.2: Optional OpenAlex/Arxiv and GitHub public discovery; cache/provenance, rate limits.
- v0.3: Adapter cho LLM được cấp quyền, tách Planner/Critic/Engineer/Auditor rõ quyền.
- v0.4: CI sandbox và bảng đánh giá golden độc lập; phát hiện regressions.
- v0.5: Plugin connector release staging and explicitly approved promotion.
- v1.0: Scheduler/supervision, telemetry và rollback được kiểm chứng trên môi trường mục tiêu.
