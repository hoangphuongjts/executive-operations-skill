# Multi-platform AI skill guide

This repository can be used as a portable AI skill pack across multiple host types:

- ChatGPT / OpenAI plugin-style skills
- Claude custom instructions / prompt pack
- Gemini instruction-based workflows
- Generic agent frameworks using markdown instructions

## 1) What this repo is

This repo is not a single deployed runtime. It is a multi-part knowledge bundle that includes:

- plugin metadata (`plugin.json`)
- skill folders under `plugins/`
- packaged ZIP exports under `packages/`
- migration manifests and QA scripts under `migration/`
- installation and security docs under `docs/`

That means the portable value is mostly in the package structure, prompts, metadata, and migration guidance — all of which can be adapted to different AI hosts.

## 2) Recommended packaging model

For each platform, use the same core content but with a thin platform wrapper:

- Canonical repo skill: `SKILL.md`
- Claude wrapper: `CLAUDE.md`
- Gemini wrapper: `GEMINI.md`
- Generic agent wrapper: `AGENTS.md`

This lets the same repo present as a skill in different environments without rewriting the core workflow.

## 3) ChatGPT / plugin-style usage

Use the repo’s plugin metadata and skill folders as a prompt pack or plugin bundle.

Typical steps:

1. Open the repo in a plugin-friendly environment.
2. Use `plugin.json` as the plugin registration metadata.
3. Point the host to the relevant skill folder(s) under `plugins/`.
4. Keep the root `SKILL.md` as the canonical behavior description.

## 4) Claude usage

Claude can consume the repository as a custom instruction package or prompt bundle.

Use:

- `CLAUDE.md` for role and operating context
- `SKILL.md` as the canonical skill definition
- repo docs for validation and safety guidance

## 5) Gemini usage

Gemini is best used with a concise instruction layer plus repo summary.

Use:

- `GEMINI.md` for the platform-specific instruction set
- `SKILL.md` for the skill logic and constraints
- `README.md` for repo summary and limit statements

## 6) Generic agents / local tools

If the host supports markdown instruction files or a custom prompt pack, use:

- `AGENTS.md`
- `SKILL.md`
- any relevant skill-specific README in `plugins/*`

## 7) Migration workflow

When converting another repo into a portable AI skill, follow this pattern:

1. Inspect the repo structure and identify the actual functional assets.
2. Classify each item as source, plugin, package, script, docs, or runtime.
3. Define the skill purpose and target platform(s).
4. Write a portable instruction file.
5. Add validation, rollback, and security notes.
6. Keep status labels honest: source observed, offline tested, host visible, deployed.

## 8) Safety and validity

Important limits to keep in mind:

- Not every plugin in this repo is a live deployed service.
- Some package directories are staging or migration artifacts.
- Some parts require OAuth or external host support.
- Do not claim full runtime success without proof.

The correct posture is: portable skill packaging with evidence-based claims, not a blanket claim of live deployment.

## 9) Best-practice summary

For multi-platform AI usage, the strongest approach is:

- keep repo contents as source-of-truth
- expose a compact cross-platform prompt definition
- provide platform-specific wrappers for Claude/Gemini/ChatGPT-style hosts
- state limitations clearly and preserve evidence provenance

This repo is already a good example of that pattern.
