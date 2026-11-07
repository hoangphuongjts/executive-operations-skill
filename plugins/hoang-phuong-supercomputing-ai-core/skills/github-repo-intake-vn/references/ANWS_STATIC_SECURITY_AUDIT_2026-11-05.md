# ANWS static security audit — snapshot 3f3d9116aa3be07fc7f8a5c26d996d60323c0b95

- Source: https://github.com/Haaaiawd/ANWS, branch `main`, MIT, commit above. No code fetched into execution, imported, installed or run.
- GitHub pinned recursive tree: **203 blob files**, `truncated=false`. **197 textual files** reviewed using read-only connector and static pattern search, including **38 .js/.py code/test files**; six image/SVG assets were inventoried by filename/metadata but their underlying bytes have not been vetted. 34 SKILL.md files (English/Chinese 17 each) present. Keyword scan is an indicator only; it does not prove source safety.
- `src/anws/package.json`: Node >=18, CLI `anws`, no declared npm third-party production dependencies. `prepublishOnly` runs `npm run sync` (asset sync writer), `test` runs Node tests plus template check. **Not executed.** `nexus-*` Python helper requirements include `tree-sitter>=0.22.0`, `tree-sitter-language-pack`; not installed.

## Findings

| Severity | Evidence at pinned snapshot | Static observation | Restriction |
|---|---|---|---|
| HIGH (if CLI enabled) | `src/anws/bin/cli.js` options `--yes`; `src/anws/lib/init.js` `askOverwrite`; `src/anws/lib/copy.js` `writeTargetFiles` | Automatically approving overwrite can replace managed project files. `writeTargetFiles` invokes `fs.copyFile` and `fs.writeFile`. | Never package/execute CLI in Core. Interactive review, backup, confined target, no `--yes` on live user projects. |
| MEDIUM | `src/anws/lib/update.js` lines ~251–272 | Legacy `.agent/` directory may be recursively removed after an interactive confirmation. `--yes` currently bypasses this deletion path but may approve other migration behavior. | Do not run migrations or claim zero risk of deletion. Require explicit separate authorization in any later runtime work. |
| MEDIUM | `src/anws/scripts/strip-alpha-markers.js`; `src/anws/scripts/sync-assets.js`; test files | Supporting scripts write files; tests use child processes, temporary-directory cleanup (`fs.rm(...recursive,force)`) and CLI invocation. | Keep scripts and npm hooks out of prompt-only skill; test scripts are not harmless when run in the wrong directory. |
| MEDIUM | Four `git_detective.py` language/template copies under nexus mapper/query | Python uses `subprocess.run(['git','-C',repo_path,...])` to inspect Git history. No shell injection seen in selected call, but reads repository history and invokes local process. | Do not execute or ship; require sandbox and user authorization if needed later. |
| MEDIUM | `src/anws/templates_en/.agents/skills/system-architect/SKILL.md`, `tech-evaluator/SKILL.md`, and `.agents/workflows/genesis.md` | Many templates presume ANWS `/genesis` sequence, `.anws` state and separate `sequential-thinking`/subagents. These are instructions from upstream, not privileged host instructions. | Do not activate upstream chains verbatim. Only independent text guidance adapted with source and license. |
| UNKNOWN | `assets/*` six images/SVG | Inventory and path metadata verified, content not byte-inspected. Static keyword checks also cannot establish behavior of every branch or license rights of all assets. | Full repository security audit certification **not granted**. |

## Negative observations and limitation

Read-only static pattern review of pinned text showed no clear `curl | sh`, `wget | sh`, direct network transfer from core CLI, or embedded credential dump path. This is **not** a guarantee of no malicious behavior, and no dynamic verification, dependency vulnerability enumeration, binary inspection, or supply-chain signature verification occurred. **Security-audited repository count remains 0** for the 384-source project. Existing prompt-only `architecture-technology-evaluation-vn` stays eligible as a scoped text adaptation, not as proof that ANWS runtime is secure.

## Required completion gates for full audit

Binary asset origin and content verification; comprehensive manual code-flow review for file destination validation, symlink handling, path traversal and update failure/rollback; external dependency provenance and vulnerability review; independent threat-model signoff. Explicitly separate those from actual execution tests (none performed by request).
