# ANWS static audit erratum — 2026-11-05

Source: Haaaiawd/ANWS pinned commit 3f3d9116aa3be07fc7f8a5c26d996d60323c0b95. This correction applies to the Batch 13 row 47 audit note.

The Batch 13 delta wording says the legacy .agent directory can be removed when the CLI is run with --yes. Re-reading src/anws/lib/update.js and src/anws/lib/cli.js at the pinned commit shows this clause is inaccurate: --yes sets the force-yes flag, and maybeDeleteLegacyDir returns without deleting in that mode. The recursive .agent deletion follows a separate interactive confirmation path. The --yes flag can still approve overwrites of managed files and other migration actions.

Other static observations remain: writeTargetFiles performs file writes/copies, supporting sync scripts and npm hooks write assets, tests invoke child processes and recursive temporary-directory cleanup, and the Python git_detective.py helpers invoke the local git process without shell mode in the inspected calls. Existing-parent symlink/path-containment behavior remains an unresolved audit question, not a confirmed exploit.

No ANWS runtime or upstream code was installed, imported or executed. The selected Skill remains a prompt-only adaptation. Six image/SVG files were inventoried by metadata but not inspected at byte level; dynamic behavior, binary content, dependency vulnerability status and complete repository security certification remain unverified. The number of repository-wide security audits remains zero.
