---
name: hoang-phuong-portable-ai-skill
description: "Portable AI skill pack for packaging, validating, and reusing repositories as skills across ChatGPT, Claude, Gemini, and similar AI environments."
version: 1.0.0
author: Hoang Phuong
platforms:
  - ChatGPT
  - Claude
  - Gemini
  - OpenAI-compatible agents
  - Generic agent platforms
use_cases:
  - package a repo as a skill or agent
  - convert a project into an installable prompt pack
  - validate AI skill portability and source provenance
  - route tasks to specialist sub-skills
---

# Hoàng Phương Portable AI Skill

This repository is a portable AI skill pack and migration toolkit, not a standalone server or runtime. It is designed so a repo, plugin, or workflow can be repackaged for use in different AI environments such as ChatGPT, Claude, Gemini, and other agent-style platforms.

## Mission

- Turn repository content into a portable skill package
- Preserve evidence, provenance, and safety limits
- Document install and migration steps clearly
- Provide a single workflow compatible across multiple AI platforms

## Working principles

1. Verify before claiming runtime or deployment.
2. Separate source observations from host execution.
3. Preserve plugin boundaries, OAuth scope limits, and secrets handling.
4. Keep outputs concise, auditable, and suitable for prompts or migration guides.
5. For multi-platform usage, prefer a prompt-first wrapper that each AI host can read as a skill instruction.

## Typical flows

- Repo intake and assessment
- Packaging to skill/plugin format
- Risk and compatibility check
- Migration guidance
- QA validation and rollback notes

## Multi-platform usage

Use this repo as a reference package and then adapt the same logic into platform-specific wrappers:

- ChatGPT / OpenAI plugin: use the `plugin.json` + Skill folders
- Claude: use `CLAUDE.md` instructions and repo-local prompt guidance
- Gemini: use `GEMINI.md` or wrapper prompts derived from this repo
- Generic agents: use `AGENTS.md` and `SKILL.md`

## Output contract

When asked to prepare a repo as a skill, the assistant should provide:

- scope and purpose
- files involved
- safety and dependency constraints
- portability notes for target platform
- installation or import instructions
- validation and rollback plan

## Repo content

This repo already contains:

- `plugins/` for packaged skill/plugin materials
- `packages/` for ZIP export bundles
- `migration/` for manifests and migration steps
- `scripts/` for offline QA and GitHub publishing helpers
- `docs/` for installation and security guidance

This is the right starting point for turning a repo into a cross-platform AI skill package.
