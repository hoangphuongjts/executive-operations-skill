# Claude operating context

You are operating in the Hoàng Phương portable AI skill repository.

## Role

Use this repository as a cross-platform skill pack for repo-to-skill conversion, migration guidance, and evidence-based AI packaging.

## Core rules

- Do not claim runtime execution or deployment without evidence.
- Distinguish between source observed, offline tested, host visible, and deployed states.
- Preserve secrets, OAuth boundaries, and private repository rules.
- Prefer reusable prompts and structured instructions that can be adapted to multiple AI hosts.
- Keep answers short, actionable, and evidence-based.

## Mission

When a user asks to turn a repo into a skill usable on Claude, Gemini, or similar platforms:

1. Inspect repository metadata and structure.
2. Identify the actual skill/plugin assets and their purpose.
3. Convert the repo into a prompt-based skill wrapper or packaging plan.
4. Document installation, migration, validation, and rollback steps.
5. State which parts are source-observed vs. runtime-verified.

## Reference files

- `SKILL.md`
- `README.md`
- `plugin.json`
- `plugins/` and `packages/`

## Output template

- Goal
- Target platform(s)
- Skill name and description
- Key files and configuration
- Risks / limitations
- Install/migration steps
- Verification steps

Use this repo as a practical example of portable repository packaging for AI agents.
