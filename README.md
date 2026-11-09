## Cross-platform AI skill support

This repo now includes a portable AI skill wrapper intended to work across multiple agent ecosystems, including ChatGPT, Claude, Gemini, and generic agent hosts.

Files added at the repo root:

- `SKILL.md` — canonical cross-platform skill definition
- `CLAUDE.md` — Claude-specific context
- `GEMINI.md` — Gemini-specific context
- `AGENTS.md` — general agent usage guidance

This structure helps turn the repository into a reusable skill pack without relying on one proprietary runtime only.

### How to use it

- Open the repo in an AI host that supports custom instructions or prompt packs.
- Follow `SKILL.md` as the canonical skill definition.
- Use `CLAUDE.md` and `GEMINI.md` when the environment expects platform-specific instruction files.
- For repo-to-skill conversion tasks, treat this as a packaging and migration workflow rather than a fully running service.

### Important limitation

This repository contains source packages, migration manifests, QA helpers, and plugin materials; it is not by itself a deployed application with live cloud APIs. The portability here is primarily about prompt-based skill packaging, migration guidance, and workflow reuse across AI platforms.

