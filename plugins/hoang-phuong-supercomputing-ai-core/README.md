## Release v16.0.38 — status-consistency repair

Prepared from deployed v16.0.37 to correct release-status language and preserve the audit trail. This follow-up changes documentation and release metadata only.

- Aligns both manifests and the active router self-check at 16.0.38.
- Reframes the v16.0.37 pre-deployment note as historical and records v16.0.37 as the source observed for this follow-up.
- Preserves the merged 384-row registry, 16 clusters, 128 role profiles, 108 study codes, seven original Skills, and current asset records.
- Adds no runtime, API/MCP capability, dependency, credential or external execution.

## Previous release — v16.0.37

Additive forward repair prepared from deployed v16.0.35 and the retained, non-current v16.0.36 checkpoint. Version 16.0.37 is selected because 16.0.36 already exists as an attached non-current release.

- Aligns both manifests and the active router self-check at 16.0.37.
- Reconciles the original 384-row repository registry using conditional updates to rows 2, 4 and 45–52; all other 374 rows retain their original content and order.
- Confirms 16 host-verified, 36 excluded and 332 pending candidates; the registry still represents 384 repository slots, not 384 approved Skills.
- Adds the three verified prompt-only Skill assets to the additive asset registry; existing asset records remain unchanged.
- Preserves 16 clusters, 128 role profiles, 108 study codes, seven original Skills, 78 packaged SKILL.md files and the unchanged default prompt.
- Adds no upstream runtime, external API/MCP capability, credentials, dependencies or paid jobs; upstream code was not executed.

At the time v16.0.37 was prepared, the live release was v16.0.35 and that candidate had not yet been approved. This is historical preparation context.

## Previous release — v16.0.26

This documentation-only consistency release retains the full v16.0.25 package. It aligns this release heading and the active Core Skill's version check with both manifests. The default prompt and runtime are unchanged.

- Preserves all 70 Skills, 7 original Skills, 128 profiles, 108 study codes, 16 clusters, references, files and plugin bindings.
- Carries forward the scientific-data-analysis-vn guidance Skill and its MIT license notice added in v16.0.24.
- No runtime code, permissions, credentials, external execution or paid jobs are added.

## Previous release — v16.0.25

Added the BATCH_08 repository-audit report and refreshed the Core asset registry, status and candidate index.

## Previous release — v16.0.24

Added the scientific-data-analysis-vn workflow guidance and its upstream MIT license notice; the Skill does not bundle scripts, libraries or a separate runtime.

## Previous release — v16.0.23

This non-destructive overlay preserved the full v16.0.22 package. The Architect + Engineering default prompt was unchanged and remained identical in both manifests.

- Aligns both manifests, `EMBEDDED_128_MODE.json` and `CAPABILITY_MATRIX.json` to the release version.
- Records the exact v16.0.22 source release in `CLUSTER_16_STATUS.json`; the registry retains 384 candidate slots representing 382 unique repositories, with two cross-cluster duplicate records called out.
- Validates all 41 packaged Core Skill mappings and separately counts eight prompt-only candidate adaptations; none represents a downloaded or installed upstream repository.
- Makes offline release diagnostics read matching manifest versions dynamically and labels the v15.1.3 guide historical; `$hoangphuong-v16-active` remains the active entry point.
- Preserves all 7 original Skills, 128 profiles, 108 study codes, 16 clusters, all current Skills, references, files and plugin bindings.
- No upstream repository code, OAuth scopes, secrets, external runtime or paid job is added.

Offline verification was run against the current source snapshot before publication; see the local audit report for counts and skipped historical checks.

## Previous release — v16.0.22

This release added a Vietnamese scientific paper reading adaptation and updated the discovery ledger. Full upstream repository security audits and source-code integration remain pending.

## Historical release note — v15.1

# Historical release note: Hoàng Phương Supercomputing Core v15.1 — guarded overlay

This is a non-destructive update of the EXISTING personal plugin, not a new plugin. Four milestones in a single update: v14.8 stability/security, v14.9 offline evaluation/routing, v15.0 opt-in controlled-runtime pilot planning, v15.1 host-native federated capability planning. **External agent runtime is not deployed.**

- Adds stdlib-only governance, routing, study code parity checker, offline test suite, 4–8 agent pilot planner, conservative capability resolver.
- Repairs release metadata in manifests, Core mode and capability matrix.
- Preserves existing 7 original Skills, 128 profiles, 16 clusters, 500-discovery catalog, 15 GitHub500 adapter Skills, Academy, historical references, runtime source and all other plugins.
- Does not copy or execute 500 third-party repositories, does not grant OAuth permissions, does not claim full audit or success of the optional runtime.

Test: `python -m unittest discover -s skills/hoangphuong-supercomputing-core/scripts -p 'test_v151.py' -v`.
Release gates, risk and rollback: `skills/hoangphuong-supercomputing-core/references/V151_SECURITY_AND_ROLLOUT.md`.
