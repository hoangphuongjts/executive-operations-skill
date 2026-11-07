# Nango gateway — authorization and acceptance policy

**Source of truth:** existing personal plugin `nango-gateway-vn` (do not migrate/delete/overwrite). This overlay provides Core-side routing, not a server or secret.

| Gate | Acceptance | Status at packaging |
| --- | --- | --- |
| Owner/source | Resolve both plugin backend IDs and current versions | PASS |
| Source configuration | Nango Management MCP endpoint and provider auth scheme inspected | PASS (metadata only) |
| Preserve existing modules | Archive is additive; no delete_paths | PASS (overlay review) |
| Adapter presence | New `skills/nango-core-adapter/SKILL.md` validated | PASS |
| ChatGPT host skill load | Readback new release skill | PENDING |
| Nango authenticated tools | Observe live Management MCP read-only call | NOT TESTED; no session tool available |
| Runtime API integration | Provider-specific authorized E2E call | NOT TESTED |

## Operational safeguards
1. Do not request a user to paste API keys in a message or file.
2. Use Nango plugin's configured connection UI to complete authentication. Never copy credentials between plugins.
3. Read-only Nango metadata first. Require explicit confirmation before write, deployments, OAuth scope changes or cost-bearing API calls.
4. Audit logging must avoid tokens, cookies, credentials, PII and proprietary returned payloads.
5. Rollback Core adapter by reverting the Core release through authorized Plugin Creator release workflow; Nango plugin remains untouched.
6. Record actual evidence and report `requires_connection` rather than claim activation.
