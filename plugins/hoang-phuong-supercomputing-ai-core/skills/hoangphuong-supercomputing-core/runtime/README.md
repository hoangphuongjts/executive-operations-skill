# 128-agent Local Gateway — Supercomputing Core v14.1

This is **source code you can run**, not 128 deployed cloud processes, fine-tuned models, or doctoral qualifications. Uses Python standard library and SQLite. The 128 role profiles are isolated by ID and group; calls to model endpoints are opt-in. No web browsing, shell execution, posting, payment or external tools are exposed to agents.

## Windows / local Python (no Docker required)

From this directory:

```powershell
python platform128.py validate
python platform128.py list
python platform128.py inspect --id 128
python seed_knowledge.py
python platform128.py run --id 1 --task "Nêu giả thuyết kiểm chứng khoa học"
python -m unittest discover -p 'test_*.py' -v
```

For the HTTP server, generate a token and set it in the **current PowerShell session**:

```powershell
$env:AGENT_GATEWAY_TOKEN = python -c "import secrets;print(secrets.token_urlsafe(32))"
python platform128.py serve --host 127.0.0.1 --port 8765
```

Check: `http://127.0.0.1:8765/health`. All other endpoints require `Authorization: Bearer <token>`.

## Docker Compose (if Docker Desktop is installed)

1. Copy `.env.example` to `.env`. Replace the gateway token with a random token (not the placeholder). Keep `AGENT_ALLOW_EXTERNAL=0` initially.
2. Run `docker compose up --build -d` from this directory. The service is bound to **127.0.0.1:8765 only**; it is not published on the Internet.
3. Optionally run `docker compose exec research-agents python seed_knowledge.py` to seed 16 **original, unreviewed** methodology documents.
4. `docker compose logs --tail=50 research-agents` and `docker compose down` as needed. SQLite is stored in a Docker named volume. Configure backup procedures before production.

## Model provider (disabled by default)

Ollama local, after choosing and downloading a model yourself: `AGENT_MODEL_ENDPOINT=http://127.0.0.1:11434/v1/chat/completions` when using native Python. When running in Docker use `http://host.docker.internal:11434/v1/chat/completions` (Ollama must listen on a suitable interface, limit firewall accordingly). Set `AGENT_MODEL_NAME` to the installed model name. Change `AGENT_ALLOW_EXTERNAL=1` only after reviewing which data will be sent. A remote provider **must** use HTTPS and `AGENT_MODEL_API_KEY` as an environment secret. Check terms, model license, token costs, provider data retention. No API key is included.

Calling `python platform128.py run --id 1 --task "..." --execute` makes **one outbound provider request** and may incur a cost. The default command (without `--execute`) is dry-run.

## HTTP API (bearer token required)

- `GET /health` (unauthenticated, minimal status)
- `GET /agents`, `GET /agents/<id>`, `GET /evals/structure`
- `POST /agents/<id>/run` body `{"task":"...","execute":false,"remember":false}`
- `POST /team/run` body `{"ids":[1,2,3],"task":"...","execute":false}` (1–8 agents, sequential calls)
- `POST /knowledge/ingest`: JSON `{group_id,title,body,license,author,approved_by,permission_proof,source_url,reviewed_license}`
- `POST /agents/<id>/memory/delete` body `{"session":"default"}` deletes only that agent/session.

The stored group-id on each agent restricts knowledge retrieval to that one domain. No training data is uploaded or used to update model weights. Memory write is **disabled by default** and limited to an opt-in session when `remember:true`.

## Licensing and provenance

Only manually attested `project_original`, `CC0-1.0`, `CC-BY-4.0`, `MIT` or `permission_granted` may be ingested. External sources require HTTPS, attribution/author, a proof field and explicit `reviewed_license:true`. These are input validation rules, **not an independent legal audit**. Human reviewers must verify license on the actual source; CC BY 4.0 requires appropriate credit and a link to its license, plus notice of changes. Exclude non-commercial/unknown/proprietary sources unless separately licensed. Book/web excerpts must not be ingested without permission. Every document has content SHA-256 and recorded provenance.

## Testing and actual quality

`python platform128.py eval-structure` validates **coverage only**. The 128 evaluation scenarios in `evals_128.jsonl` are unreviewed blueprints, not scored agent capabilities. Expert domain reviews and actual model responses are still required. Test 8 agents at a time, document accuracy, sourced reasoning, edge cases, refusal/robustness, cost/latency and expert signoff. A PhD-style *curriculum* does not confer a PhD or equivalent validated expertise.

## Security and deployment boundary

- Intended for a personal machine or private network. Do **not** expose this demo HTTP service directly to the public Internet. Use an authenticated HTTPS reverse proxy, proper identity/access management and backup/monitoring before remote deployment.
- Provider URLs are configured by the operator, not by user requests. No redirects, credentials in URLs or remote plaintext HTTP.
- No automatic paid API usage. Endpoint calls are gated twice (`AGENT_ALLOW_EXTERNAL=1` and `execute:true`). No built-in browser, code executor, scheduling engine or tool escalation.
- This package is minimal and needs a production security review (rate limiting, multi-user RBAC, TLS, audit logs, secret manager) before public use.


## 16 cụm chuyên môn và tranh biện chéo (v14.1)

- Mỗi **cụm** có 8 agent, tổng 16 cụm/128 agent. Bộ định tuyến theo từ khóa tiếng Việt/Anh chỉ là heuristic chưa được chấm accuracy trên dữ liệu thật.
- Khi nhận một nhiệm vụ, hệ thống đề xuất 2–4 chuyên gia từ những cụm phù hợp, tác tử số **32** kiểm tra phản biện, số **64** tổng hợp; số **57** là vai trò quy hoạch (không phát sinh lượt gọi mô hình trong tuyến này).
- Vòng 1: các chuyên gia trả lời độc lập. Vòng 2: reviewer tìm mâu thuẫn và phản ví dụ. Vòng 3: chuyên gia phản hồi quan điểm chéo. Vòng 4: agent tích hợp đưa kết luận **chưa kiểm chứng độc lập**. Với 3 chuyên gia có tối đa 8 model calls (3 + 1 + 3 + 1); tối đa 4 chuyên gia/10 calls. Đây không phải bằng chứng câu trả lời chính xác nhất.
- Mặc định `dry_run`: chỉ hiển thị nhóm và agent được chọn, **không gọi model**. Muốn có tranh biện AI thực tế phải cấu hình mô hình, bật `AGENT_ALLOW_EXTERNAL=1` và yêu cầu `--execute`; giới hạn số lượt gọi để tránh tốn phí.

```powershell
python cluster_debate.py clusters
python cluster_debate.py plan --task "Thiết kế hệ thống kho tri thức cho 128 agent" --max-specialists 3
python cluster_debate.py debate --task "Thiết kế hệ thống kho tri thức cho 128 agent" # dry-run
# Chỉ sau khi đã cấu hình model, kiểm tra chi phí và cho phép gọi API:
# python cluster_debate.py debate --task "..." --execute
```

Gateway thêm các API có Bearer token:
- `GET /clusters` — 16 nhóm × 8 agent.
- `POST /debate/plan` — `{ "task":"...", "max_specialists":3 }` chọn chuyên gia, không gọi model.
- `POST /debate/run` — `{ "task":"...", "execute":false, "max_specialists":3 }` dry-run; true mới được gọi model khi đã được người vận hành bật.

**Bảo vệ:** không cấp tools cho model; mỗi câu trả lời từ agent khác được xem là dữ liệu không đáng tin cậy, có cắt ngắn; không tự học trọng số, không tự gọi 128 agent, không công bố kết luận đã kiểm định. Tri thức dùng trong mỗi lần gọi chỉ lấy từ cụm của agent đó theo quyền của bộ chỉ mục. Tranh biện nhiều agent có thể đồng thuận sai khi dùng chung cùng một mô hình nền — cần nguồn và chuyên gia xác minh.
