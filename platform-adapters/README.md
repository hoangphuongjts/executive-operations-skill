# Platform adapter pack

This folder provides a minimal adapter pattern for converting the repo into different AI host formats.

## ChatGPT

- Use `SKILL.md` as the main behavior contract.
- Use `plugin.json` as the metadata layer.
- Route requests to the relevant skill under `plugins/`.

## Claude

- Use `CLAUDE.md` as the host instruction file.
- Treat `SKILL.md` as the canonical domain behavior.
- Keep repo docs as reference material.

## Gemini

- Use `GEMINI.md` as the platform wrapper.
- Summarize repo intent before handling tasks.
- Keep outputs bounded and evidence-based.

## Generic agent hosts

- Use `AGENTS.md` and `SKILL.md` together.
- Keep prompts short and operational.
- Attach only relevant repo paths when needed.

## Export pattern

When adapting a repo for a new platform:

1. Copy `SKILL.md` into the host’s skill or instruction directory.
2. Add the platform-specific instruction file.
3. Add a short README or launch note for the host.
4. Validate the repo path mapping and package names.
5. Document any missing runtime or deployment proofs.

This makes the repo portable without turning a source package into a fake deployed system.
