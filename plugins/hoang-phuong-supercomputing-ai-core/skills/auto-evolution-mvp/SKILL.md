---
name: auto-evolution-mvp
description: "Use when the user asks HoangPhuong Core to inventory Skills, diagnose gaps, propose verifiable improvements, create safe local patches, audit versions, or plan controlled Auto-Evolution and rollback."
---

# HoangPhuong Auto-Evolution Engine — MVP 0.2.0

**Scope:** Guidance Skill + embedded **Python reference source**, not a running ChatGPT background Agent. Preserve the currently installed `hoangphuong-v16-active` default, all prior Skills, 128 original profiles and 108 study codes.

## Trigger / routing

When asked to run controlled updates:

1. Read `runtime/README.md` for the offline CLI and limits.
2. Verify the current plugin version, selected paths, installed capabilities and user permissions. Never assume this Skill can access `C:\Users\...` by itself.
3. Use the local Python runtime **only if** the host offers authorized execution/file access. Otherwise present the package and instructions; do not claim to have run it on the user's computer.
4. In the first cycle use `python -m hpcore_evolution --root PATH --reports OTHER_PATH cycle` (read-only for the source). Examine `assessment.json`, trace each finding to a file, distinguish missing section from low model quality.
5. Research GitHub metadata only with user-approved network access `discover ... --allow-network`. Never execute repository material, scripts or dependency installers without verification.
6. For a proposed local documentation repair: run `stage PROPOSAL_ID`, review candidate, run tests; only then, with explicit user authorization, run `apply PROPOSAL_ID --approve PROPOSAL_ID` and verify new hash. Backups and rollback must be available.
7. For plugin-account changes, don't use local file apply as a substitute for an authorized Plugin Creator `update_plugin`. Check current release ID and permissions, preserve plugin name and all old files, upload changes only after approval/review and verify readback.
8. If anything fails or a concurrent release changes, stop and reconcile. Do not skip security/eval gates or self-award permissions.

## Evidence gate (MVP 0.2.0)

- Use `evaluate --baseline BASELINE.json --candidate CANDIDATE.json` to compare the SAME frozen dataset and task IDs. Require fields: `dataset_sha256`, `evaluator`, per-task pass/fail, security blockers, environment and measured-at time. JSON labels are **claims**, not cryptographic certification of reviewers.
- Any newly failing baseline task, security blocker, changed dataset ID/hash or inconsistent task IDs makes the candidate BLOCKED. No measured gains -> `no_verified_gain`.
- Output candidate_review JSON remains `stage=review_only`, `can_deploy=false`. Never grant host authorization based on the report.
- Role map for requested v17 design: Discovery/Weakness Detector/basic Auditor/Controller are offline code; Research is GitHub metadata network-opt-in; Socratic Critic/Architecture Designer are prompt lenses; Code Engineer is restricted document patch, not LLM code generator. 8 independent LLM agents are NOT deployed.

## Actual capabilities

- Source-level skill inventory; deterministic heuristic findings; local staged documentation patch; hash checks; backup and rollback; offline evidence comparison: implemented and offline-tested in the included reference runtime.
- GitHub metadata discovery: implemented opt-in, network not live-tested.
- Automatic LLM design, reasoning improvement, independent agent processes, full repository security certification, ChatGPT plugin update from background task, model training and 24/7 scheduling: **not implemented**.

## Quality / output contract

Return table of `fact`, `source`, `test evidence`, `risk`, `action`, and `state`: `SOURCE_OBSERVED`, `OFFLINE_TESTED`, `HOST_VISIBLE`, `HOST_EXECUTED`, `DEPLOYED`, `BLOCKED`. Do not call metadata heuristics 'IQ score' or deduce 128 active agents from 128 profiles.

## Supporting references

- `runtime/README.md` — Windows PowerShell and CLI.
- `runtime/docs/ARCHITECTURE_AND_NEXT.md` — roadmap and production gates.
- `runtime/docs/V17_IMPLEMENTATION_STATUS.md` — eight-role evidence and gaps.
- `runtime/docs/TEST_REPORT_V020.md` — new regression tests.
- `runtime/docs/TEST_REPORT.md` — offline test results for local reference release.
- `runtime/hpcore_evolution/` — Python source.
- `runtime/tests/` — local offline regression tests.

This Skill complements the existing governance/evaluation/supply-chain Skills and uses the task-appropriate one as needed.
