# V16 activation record — 16.0.6

- Method: **additive active-router Skill + plugin defaultPrompt**, keeping the existing v15 skill and v16 reference intact.
- Plugin ID and internal name unchanged. Seven original Skills, 128 profiles and previous references are retained by the account updater (overlay semantics; `delete_paths` omitted).
- Fixes the mismatched default route (v16 previously only optional), repairs two synchronized manifest versions, and removes the legacy `defaultPrompt: null` incompatibility by replacing it with a valid nonblank prompt.
- Browser @mention and host Skill refresh require post-publish UI confirmation.
- Optional Python prototype still disabled from making external model or network requests by default.
- This is **not** proof of end-to-end production deployment.

Concurrent release 16.0.5 introduced 16 functional clusters; this overlay preserves those files and the manifest discovery keywords.
