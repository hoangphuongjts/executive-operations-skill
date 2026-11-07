# Master registry merge result — 2026-11-05

## Source and merge guard

- Live stable readback: v16.0.35, release pluginrel_6aec1fb739a881918429c4d4e422bbce.
- Baseline registry SHA-256: 25a6c14882f357c6fd562f93d1233651ca1df361504901f64e65088061074da7 (matched both the mounted v16.0.35 source copy and Plugin Creator readback).
- Merge source: Batch 13 rows 45–48, Batch 14 rows 49–52, and the resolved pending rows 2 and 4.
- All 10 target rows passed identity preconditions for cluster, rank and repository before overlay. Only reviewed fields were updated; 374 non-target rows retained their canonical content and sequence.
- Candidate release version: v16.0.37. The attached v16.0.36 release was inspected as a non-current additive checkpoint; it contains no removed files.

## Result

- Records: 384; clusters: 16 × 24; unique repository names: 382; duplicate slots: 2 (unchanged).
- Repository registry SHA-256 after merge: d7ecdb3584892b66e2ade4e1aaf4ebc2ac31f1b5f5d357eaee8be5e38d2de216.
- SHA-256 of canonical JSON for all untouched rows before and after: 555fac17284fc8e9825e3d114a2b28073f4eb4aef3e26bfb99bea67588a24554 (identical).
- Host-verified / excluded / pending: 16 / 36 / 332; metadata-checked: 52.
- Candidate skills: 16 accepted and packaged; source code from upstream repositories: 0 imported or executed.
- Asset registry: 205 existing items preserved, 3 prompt-only skill records appended; 208 items total, 49 core skills.

## Row decisions

| Rows | Decision |
|---|---|
| 2 | Excluded from current adoption: overlapping science workflows; no distinct eligible C1 Skill selected. |
| 4 | Excluded from current adoption: no selected cost-free standalone prompt Skill; individual data terms remain relevant. |
| 45–48 | 3 excluded; ANWS row 47 retained as a scoped prompt-only adaptation with full repository audit pending. |
| 49–52 | 2 duplicate sources excluded; rows 51–52 packaged and read back in live v16.0.35. |

At the time this merge report was written, production was at v16.0.35 and the candidate had not yet been uploaded.
