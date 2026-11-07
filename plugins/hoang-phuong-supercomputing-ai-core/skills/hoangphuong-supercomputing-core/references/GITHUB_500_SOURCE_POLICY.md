# GitHub 500 — provenance, licenses, safety, and 108-code protection

**As of 2026-11-04:** Discovered 500 unique names from GitHub repository search, not 500 accepted, licensed, safe, or installed projects. 20/25 pilot repos had LICENSE / LICENSE.md file paths read. Copyright entitlement and applicability to code, images, model weights and datasets remain unverified; no external code was executed, copied or deployed.

## Review gates per repo, in order

1. Identity: exact full_name, canonical URL, non-archived check, default branch and pinned commit SHA. Search listing alone is insufficient for installation.
2. Scope: read README, manifest, import scripts, launch hooks, dependencies, data access patterns, and proposed usage; record source provenance.
3. License: read full applicable LICENSE and any per-file/per-directory/model/dataset exceptions. MIT/Apache notices may be required. GPL/AGPL may impose downstream obligations. Modified/custom licenses require manual review; absence of a license means no assumed redistribution permission.
4. Security: inspect prompt injection, egress exfiltration, credentials, install scripts, capabilities, vulnerable dependencies and excessive permissions. Do not execute downloaded code until checked; preferably isolate in a sandbox.
5. Compatibility: decide **reference-only / knowledge-guide / embedded-native-skill / optional runtime / connected tool**. No automatic OAuth token transfer. For tools, only the available host tool with actual authentication provides capability.
6. Rollback: preserve seven original Skills, all 128 agent profiles, sixteen clusters, Academy, and 108 original learning slash codes. Never rename, overwrite or infer an undocumented slash command. New command prefixes must be explicit and non-conflicting.
7. Status: `discovered_not_audited`, `license_metadata_checked`, `security_reviewed`, `packaged`, `verified_in_host`, `external_runtime_opt_in` are distinct. Catalog links are not functional installs.

## Pilot cautions

- Dify: modified Apache terms, must be reviewed against specific use.
- n8n: restrictions and special license terms; not ordinary unrestricted open-source reuse.
- Activepieces: directory-level license differences; inspect individual files.
- Tencent Hunyuan3D: custom model/community license with territorial conditions; do not copy weights or model assets.
- AGPL repos (examples: openpost, learnhouse, electricitymaps): check compliance and service obligations before distribution or hosting.
- Some projects found by repository topic may not be relevant to that category: the categorization is **search origin**, not domain expert verification.

## Operating limits

Skill mode `embedded_skills_only`; no cloned repos, no GitHub `git clone`, Python subprocess from third-party code, VPS, Docker, model API or purchases by default. Tool availability is checked in the host each session.
