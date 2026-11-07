# Controlled release v15.1.1 — security and staged deployment

Scope: non-destructive plugin overlay; changes only the Core Skill, manifests, capability metadata, default-mode registry, offline stdlib tools and this documentation. **All 7 legacy Skills, 128 agent profiles, 16 clusters, GitHub source catalogs, previous runtime and other plugins are retained.**

## v14.8 stability/security

- Root and nested manifests, Core Skill and capability matrix released as 15.1.0; historic versioned evidence remains historic.
- Default-deny static action policy; irreversible writes and costs require consent and native host permissions.
- The 108 original study codes and one-line function descriptions were imported from the user Library text source and matched 108 unique code entries. Snapshot hash checked by `core_v151.py study-health`. A modified current Project registry is NOT automatically synced and must pass the independent candidate parity command. The patch does not rename original commands.
- Third-party GitHub repo stays discovery-only until individually licensed, security-reviewed, tested and approved; no auto-install.

## v14.9 evaluation

- Unicode normalization, phrase-aware deterministic routing, abstention for unsupported tasks and ambiguity.
- 200 in-sample synthetic route smoke cases and regression tests are not equivalent to 200 independent cases or a 95% accuracy measurement.
- Independent benchmark acceptance target: >=95% correctly routed on 200+ manually labeled distinct unseen tasks, <=1% unsafe write approvals, no wrong slash-command interception, and reproducible runtime/latency measurements. **These are future gates, not completed results.**

## v15.0 controlled Agent runtime

- 4–8 role pilot planner packaged, kill switch ON by default, no paid-model execution implemented by this new script.
- Stage 1: secure sandbox + credentials + network egress restriction + cost budget + human approval.
- Stage 2: deterministic dry-run; stage 3: provider mock; stage 4: approved limited live canary; stage 5: security review, logs and rollback before expansion.
- Do not deploy the old HTTP gateway externally merely because a script exists. Audit endpoint allowlist, SSRF protection, auth rotation, rate limiting, durable audit storage and data privacy before any network exposure.

## v15.1 federated capability hub

- A catalog record only provides discovery; exact host-visible tools provide possible actions subject to provider authentication.
- No API key transfer, no external plugin code copy, no new OAuth integration. Current session tool availability must be checked again for each request.
- Only a source tool's successful result qualifies as `external_tool_executed`; no Python proxy or arbitrary tool dispatch is included.

## Threat model and controls

| Threat | Control | Residual exposure |
|---|---|---|
| Prompt injection from GitHub/Skill content | Treat as untrusted data; avoid code execution and hidden authorization changes | LLM interpretation may still err; independent adversarial evaluation required |
| Secret exfiltration | Core has no API keys; audit logs hash targets and truncate messages | Provider-specific logs, key managers need independent review |
| Irreversible write | Host provider permission + explicit approval + scope | Not enforced by a Skill text alone |
| Unsafe third-party repo | No remote code execution; per-repo review gate | 500 repository catalog is not vetted |
| Fake 128-agent claims | Evidence-status labels and explicit runtime disabled mode | Existing dormant runtime has not been pentested |
| Slash command collision | Reserved `/` handling and fail-closed 108-code checker | Candidate current Project registry not independently read back |
| Supply-chain provenance | Existing per-skill upstream metadata and LICENSE summaries | Per-file and dependency audit pending |

## Acceptance labels

- `packaged`: plugin update accepted by backend, files present.
- `offline_tested`: named tests run locally and logs exist.
- `host_visible`: fresh host Skill listing after update.
- `live_runtime_verified`: real authorized model and provider calls with logs and metrics. **Never infer from package acceptance.**

## Rollback

Use the preceding plugin release ID retained by Plugin Creator; do not delete prior scripts, profiles or skills. A rollback is a separate authorized release update, not an automatic action. On a failed compatibility check, retain the old active plugin until corrected. The existing release history stays available if supported.
