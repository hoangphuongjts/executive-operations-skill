---
name: hoangphuong-core-v160-reference
description: "Hoàng Phương Core v16.0 optional local-only reference prototype. Use for safe architecture, offline test, audit and integration plans; legacy 15.1.3 untouched."
---
# Hoàng Phương Core v16.0 — optional reference implementation

This Skill is an additive v15.2→v16.0 reference overlay for **hoangphuong-supercomputing-core**, not a replacement for the seven original Skills or the 128 defined profiles.

## Status and guardrails
- Version 16.0.0 is **plugin package version** only, NOT a production-deployed AI operating platform.
- Runtime source is available at `reference_runtime/src/hpcore/`; launch only on a separate, authorized Python environment.
- Default `kill_switch=True`; even with explicit local-plan opt-in, code does not invoke LLMs, APIs, install packages, manage OAuth, launch jobs, or make external writes.
- Treat Agent roles as perspective profiles, not running independent agent processes. Existing 500 GitHub entries are discovery-only.
- Legacy seven Skills, 128 profiles/16 groups, 108 study codes and all earlier records are authoritative and remain intact. Do not auto-modify registry or execute slash aliases.
- The existing `hoangphuong-supercomputing-core` skill is the authoritative legacy capability contract. Its historical v15.1.3 heading denotes the base component, not this overlay's production readiness.
- For actions using connected host tools, require tool discovery, current scoped permissions, user approval for external changes, and actual result verification. This prototype's Policy is NOT the host permissions firewall.

## Using the v16 reference
- Start by inspecting `reference_runtime/README.md` and `reference_runtime/docs/ARCHITECTURE.md`.
- Run `PYTHONPATH=src python -m unittest discover -s tests -v` from `reference_runtime` to independently revalidate the 13 synthetic/offline unit tests.
- Run `PYTHONPATH=src python benchmarks/run_benchmark.py benchmark_results.json` to regenerate synthetic benchmark; do not claim real-provider latency.
- Offline task plan: `PYTHONPATH=src python -m hpcore.cli plan --enable-local-plan --task "kiểm thử API"`.
- Read `reference_runtime/docs/SECURITY_AUDIT.md` before proposing production integration.
- For implementation plans, preserve all earlier files and default to non-destructive additive adapters; never represent `OFFLINE_TESTED_LOCAL_PLAN` as provider runtime deployed.

## Roadmap
v15.2 safety/audit prototype; v15.3 bounded role router prototype; v15.4 host tool metadata registry prototype; v15.5 13 unit cases + eight synthetic benchmark cases; v16.0 architecture/documentation scaffold. No production service, independent model runners, Android/iOS app or deployed gateway in this package.
