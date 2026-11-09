# Gemini operating context

Use this repository as a portable AI skill package for converting code repositories into reusable agent skills.

## Objectives

- package repo knowledge and prompts for multi-platform agent use
- preserve evidence and provenance while avoiding unsupported claims
- provide a portable structure that works across ChatGPT, Claude, Gemini, and similar environments

## Workflow

1. Read the repository structure and identify actual assets.
2. Determine what is a skill, plugin, script, package, or migration artifact.
3. Build a wrapper that summarizes the repository in a portable prompt format.
4. Create usage instructions for the target AI platform.
5. Highlight security, OAuth, and deployment limits.

## Guardrails

- No assumptions about API keys, OAuth runtime, or production host execution unless clearly documented.
- No overstatement of deployment status.
- Keep the skill format generic enough to be used in different AI environments.

## Recommended output

- skill name
- concise summary
- target platforms
- installation guidance
- validation checklist
- limitations and next steps

This repo is a strong example of a portable skill pack built around a migration-and-packaging workflow.
