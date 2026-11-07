# Activation notes — v16.0.6

Changes requested: make v16 active as ChatGPT guidance, preserve older profiles/skills and fix metadata inconsistencies.

Changed in release overlay:
- `plugin.json` and `.codex-plugin/plugin.json`: version and interface synchronized, default prompt now points to v16 router.
- `skills/hoangphuong-v16-active/SKILL.md`: added main v16 router.
- Supporting `agents/openai.yaml` and `references/ACTIVATION.md`.

Preserved (omitted in overlay, no delete_paths): 7 original Skills, v15.1.3 baseline, v16 offline reference runtime, 128 profiles, 108-code baseline, GitHub500 catalog, all other adapters and assets.

Not performed: production runtime deployment, Windows local folder modification, third-party setup, model fine-tuning, full legacy/host E2E functional test.

Rebased after concurrent version 16.0.5 (16 clusters) and preserved its keywords and descriptions.
