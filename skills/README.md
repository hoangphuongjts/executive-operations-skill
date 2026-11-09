# Skill catalog (`skills/`)

This directory gives each of the 16 existing plugin ZIP packages a predictable `skills/<name>/SKILL.md` entry point. The entries are **catalog wrappers**, not extracted replacements for the ZIP packages and not proof that the host can execute a plugin.

## Use

1. Browse `skill-manifest.json` and choose a package by its exact name.
2. Read that skill's `SKILL.md`, the source plugin README, and any linked security/reconnect docs.
3. Inspect the corresponding `plugins/<name>/` source and `packages/<name>__<version>.zip` before importing.
4. Import the original package or adapt its verified prompt content to the selected host's supported format.
5. Test in that host and record the result. Import readiness does not mean installed, authorized, or runtime-tested.

The manifest preserves source package versions and the export matrix's portable-skill counts where available. It also calls out nested skills that are not automatically discovered, host/runtime prerequisites, and blocked site/app candidates. See `MULTI_PLATFORM_GUIDE.md` and `platform-adapters/` for general adaptation notes.
