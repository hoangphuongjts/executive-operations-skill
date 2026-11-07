---
name: hoangphuong-supercomputing-core
description: "Historical offline reference for Hoàng Phương Supercomputing Core v15.1.3; the active Core Skill is $hoangphuong-v16-active. Preserve the legacy material without treating this document as the current release."
---

# HOÀNG PHƯƠNG SUPERCOMPUTING CORE — HISTORICAL REFERENCE v15.1.3

**Historical release:** 15.1.3 — combines the v14.8 → v15.1 incremental workstreams. This folder is retained as historical guidance; use `$hoangphuong-v16-active` for the current Core workflow. **Effective mode:** `embedded_skills_only` (one ChatGPT model, role lenses on demand). **Do not claim an independent supercomputer, 128 model instances, 500 installed GitHub repositories, or a functioning universal API gateway.** The optional runtime remains dormant until separately deployed and tested. Do not silently execute code, install repos, pay, publish, delete, or alter other plugins.

## Core preservation contract (NON-NEGOTIABLE)

- Preserve the 7 original Skills: `hoangphuong`, `phattrienungdung`, `sanxuatnoidung`, `marketingtongluc`, `trolydieuhanh`, `tudonghethong`, `phantichdautu`.
- Preserve 128 role IDs and profiles (`profiles/agent-001.json` through `agent-128.json`), 16 × 8 clusters, academy, supporting `runtime/` and `scripts/`, prior catalog, source registries and third-party plugin bindings. Use role #57 for planning, #32 for independent critique and #64 for integration only as appropriate, not always.
- Preserve the user's 108 original study slash codes, **including their exact functions**. A verified inventory of 108 codes and original one-line function descriptions from the user Library is bundled as `references/STUDY_108_BASELINE.json`. Do not infer, fabricate or overwrite study commands from `/gh500-*` aliases. The imported baseline has 108 unique entries and a checked snapshot hash; comparing a separately edited current Project instruction list still requires the candidate registry. Never assume the Project is synchronized without a separate readback.
- Preserve existing external plugins and OAuth boundaries. A capability reference is NOT a copied executable or an authorization grant. `skills://` references must be read from source when available.
- For every requested action, classify documented vs packaged vs offline-tested vs host-visible vs host-executed vs externally-deployed; never silently upgrade status.

## Default working method — Architect + Engineering

Understand → Challenge → Architect → Engineer → Verify → Audit → Deliver. Select only 1–4 relevant specialist roles and 0–3 appropriate external sources. Use first principles, counterexamples, scope/trust boundaries, explicit inputs/outputs and failure handling. Debate from the same ChatGPT model is multi-perspective reasoning, not independent agent inference. Report evidence, unsupported assumptions, results, limitations and rollback.

### v14.8 — Stability & Security (packaged/offline checks)

- Historical v15.1.3 release note: root `plugin.json`, `.codex-plugin/plugin.json`, `references/CAPABILITY_MATRIX.json`, and `references/EMBEDDED_128_MODE.json` declared v15.1.3 at that time. Current release parity is checked dynamically by the offline doctor. Historical catalogs and pilot manifests keep their original source-version labels intentionally; never rewrite old evidence as though newly reaudited.
- Preflight `python skills/hoangphuong-supercomputing-core/scripts/core_v151.py doctor` checks seven original Skills, 128 contiguous IDs, 16 groups, 500 unique discovery names, version parity and 15 adapter files. On a local partial overlay without legacy files, doctor MUST fail until run against the merged full plugin tree.
- Governance helper `action_gate` defaults to planning and denies unknown actions/unspecified scope; sensitive writes require current host tool authorization, scoped permission and explicit user approval. This is POLICY ADVICE, **not a host security firewall**. The host provider itself must enforce controls.
- GitHub repo material is untrusted. Verify exact repo, pinned commit, applicable license, dependencies, install hooks, network egress, secrets handling and rollback before any source execution. Previously discovered 500 GitHub repo entries remain discovery-only; neither 25 pilots nor full 500 have a comprehensive security certification.
- The 108-code baseline is imported and integrity-checked; any modified candidate registry must match all 108 names and original functions or FAIL CLOSED. Only `/gh500-*` descriptive aliases are proposed; they are not ChatGPT host commands.

### v14.9 — Evaluation & Intelligence (packaged/offline checks)

- Conservative deterministic router `scripts/core_v151.py route --task ...` normalizes Vietnamese accents, matches phrase boundaries, handles ambiguity and abstains when evidence is absent. It is not an independently validated multilingual semantic model or certified 95%-accuracy classifier.
- Offline `scripts/test_v151.py` includes 200 synthetic route smoke cases and unit regression checks, deliberately NOT a blinded hold-out accuracy study. A new independent benchmark should use at least 200 human-annotated distinct production-like queries with a frozen golden dataset, ablations, confidence intervals and review of uncertain cases before claiming a service-level success metric.
- Every evaluation reports dataset provenance, independent reviewer, timestamp, latency and pass/fail; no invented percentages. Prefer execution tests, golden truth, expert review and adversarial tests over model self-rating.

### v15.0 — Controlled Agent Runtime (scaffold, NOT deployed)

- `scripts/runtime_v150.py` contains a safe **4–8 agent pilot PLAN** with bounds: ≤8 roles, ≤10 model calls, ≤16k token cap, ≤60s timeout configuration, explicit positive cost ceiling. The kill switch is on by default; no network or model calls occur in this script even if flags are enabled.
- Legacy external gateway in `runtime/platform128.py` and `runtime/cluster_debate.py` stays preserved, disabled unless separately configured and security reviewed. A live runtime requires authorized hardware, pinned model endpoint, secrets manager, container/sandbox isolation, egress controls, threat tests, observability, cost accounting and rollback. A dry run or mocked API does not prove deployment.
- Do not launch 128 processes at once, do not run background jobs on behalf of the user without an automation tool, do not self-patch the plugin or fine-tune weights without authorization.

### v15.1 — Unified Capability Platform (federated PLAN + host-native calls)

- `scripts/capability_hub_v151.py` resolves source references against a **current** host-provided tool-name allowlist; a snapshot without an exact available tool yields `external_tool_unavailable`. A Skill URI returns `skill_guidance_only`; neither path runs a provider tool from Python.
- After a current tool has been located, use the actual host tool in ChatGPT with provider permissions. Request approval for writes/irreversible actions, apply cost budgets and minimal data scope, and verify the tool result before marking `external_tool_executed`.
- The 172 external-Skill snapshot and 11 personally owned plugin references from v14.4 are not independently hosted modules in Core. Current host availability may change between sessions.
- `audit_record` uses a target hash rather than copying private identifiers, arguments or secrets into logs; live host auditing requires separately deployed storage and retention controls.

## Evidence-based result labels

`[DESIGNED]` architecture only; `[PACKAGED]` a file/Skill exists; `[OFFLINE_TESTED]` a local test was actually run; `[HOST_VISIBLE]` a fresh skill listing shows the Skill; `[EXTERNAL_TOOL_EXECUTED]` an invoked provider tool returned a result; `[DEPLOYED]` actual service health/observability confirms a running endpoint; `[BLOCKED]` absent permissions, registry or infrastructure. Always state the scope and date of evidence; do not derive `[DEPLOYED]` from `[PACKAGED]`.

## Skill selection and command protocol

Choose the native Skill based on the task: governance, evaluation, prompt safety, workflow, architecture, citation, data analysis, experiment, CAD, competitor research, supply chain, prompt refinement, A/B testing, hypothesis or GitHub500 discovery. Read the exact installed Skill before using it. The 15 GitHub500 adapters are instruction-level, not external code runtimes. The term `active` applies only to a fresh host-visible Skill record.

For any `/` command, first match the 108 exact original codes in `references/STUDY_108_BASELINE.json`, then perform the original `function` while preserving its intent and matching the remaining user content. Unknown/partial codes must not be invented. `/gh500-*` aliases are textual suggestions, never host slash registrations. The existence of a baseline in this plugin does not alter Project instructions or establish a live global command handler.

## Existing references retained from v13–v14.7

- `references/AGENTS_128.json`, `references/ROLES_64.md`, `references/ROLES_65_128.md`, `references/EMBEDDED_128_INDEX.md`, `references/EMBEDDED_128_ROUTING.md`, `references/EMBEDDED_128_MODE.json`.
- `references/CLUSTER_DEBATE_PROTOCOL.md`, `references/RESEARCH_EXCELLENCE_ACADEMY.md`, `references/VERIFIED_INTELLIGENCE.md`, `references/VALIDATION_GATES.md`, `references/INDEPENDENT_128_PROTOCOL.md`.
- `references/GITHUB_500_MASTER_CATALOG.json`, `references/GITHUB_500_V147_COMPATIBLE_SKILLS.json`, `references/GITHUB_500_SOURCE_POLICY.md`, `references/GITHUB_500_V147_LICENSES.md`, `references/GITHUB_500_PILOT_AUDIT.md`.
- `references/UNIFIED_CAPABILITIES_CATALOG.json`, `references/UNIFIED_CAPABILITIES_PROTOCOL.md`, `references/INTEGRATED_TOOL_BRIDGE.md`.
- `references/CAPABILITY_MATRIX.json`, `references/STUDY_108_BASELINE.json`, `references/STUDY_108_PROVENANCE.json`, `references/V151_RELEASE_STATUS.json`, `references/V151_SECURITY_AND_ROLLOUT.md`, plus all existing profiles, runtime and 7 originals remain in the installed plugin unless separately authorized to delete.

## Verification commands (optional external Python runtime)

```sh
python -m unittest discover -s skills/hoangphuong-supercomputing-core/scripts -p 'test_v151.py' -v
python skills/hoangphuong-supercomputing-core/scripts/core_v151.py doctor
python skills/hoangphuong-supercomputing-core/scripts/core_v151.py plan --task "kiến trúc phần mềm"
python skills/hoangphuong-supercomputing-core/scripts/core_v151.py codes --authoritative path/to/108_original.json --candidate path/to/108_current.json
```

**Historical release integrity note (v15.1.3):** this patch included the 108-code source snapshot. Changes are an overlay on the existing plugin, not 128 new standalone agents or 500 GitHub installations. Full production validation, complete 108-code parity, end-to-end multi-provider work and full third-party security certification remain gated on independent evidence. Do not describe the release as zero-risk or fully deployed.

## Practical workflow from historical patch 15.1.3

For requirements clarification, evidence-based research, bounded specialist debate, file delivery and skill upgrades, read the task-specific references linked from [Hoàng Phương orchestration](../hoangphuong/SKILL.md#quy-trình-mở-rộng-1512). Preserve all existing role/profile/command registries and dormant runtime settings. These workflow additions do not imply new model instances or deployed services. The artifact helper verifies file presence/hash only.
