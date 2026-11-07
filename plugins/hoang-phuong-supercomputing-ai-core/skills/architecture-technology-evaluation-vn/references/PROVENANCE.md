# Provenance — architecture-technology-evaluation-vn

- Upstream: https://github.com/Haaaiawd/ANWS
- Verified commit: https://github.com/Haaaiawd/ANWS/commit/3f3d9116aa3be07fc7f8a5c26d996d60323c0b95
- Default branch observed: `main`
- License: MIT; Copyright (c) 2026 (as in upstream LICENSE). Full notice in `UPSTREAM_LICENSE_MIT.txt`.
- Sources reviewed as text: root README.md, LICENSE, src/anws/package.json, `templates_en/.agents/skills/tech-evaluator/SKILL.md`, `tech-evaluator/references/ADR_TEMPLATE.md`, selected sibling SKILL.md and JS installer/update code.
- Selected method: 12-dimension weighted matrix + ATAM + requirement/ADR traceability. No source code, CLI, package, scripts or dependencies bundled.
- Modifications: Vietnamese stand-alone prompt workflow; tool-specific `/genesis` targets and mandatory `sequential-thinking` CLI replaced with explicit analytical checklist. The no-early-ADR and evidence requirements are preserved; not compatible with executing ANWS native workflow automatically.
- Original ANWS CLI was not audited repository-wide, downloaded, run, installed or imported. Static review found file writes/copies, optional overwrite and recursive deletion of legacy `.agent/` after confirmation or force flag. The new skill does not invoke any of these operations.
- Related existing skill boundaries: `system-design-planning-vn` = upfront whole-system design; `github500-architecture-blueprint` = existing-code system blueprint; `architecture-documentation-arc42-vn` = architecture documentation; this skill = evidence-based **technology choice**.
