# Integrated Tool Bridge — Supercomputing Core v14.4

## Contract
This is a **single, namespaced facade** that keeps the original plugin's credentials, backend and terms. It routes agent requests to the existing ChatGPT tool layer or original Skill URI when available. It **does not** tunnel arbitrary providers or turn a manifest reference into tool permissions.

### Supported source behaviors
1. Original Skills: discover -> source `skills__read` -> follow specific skill and its authorization -> act with permitted in-chat tools.
2. User-owned plugin Skills: use existing `skills://plugins/<owner>/<slug>`; the original plugin stays installed. For source modifications, update the original separately only when requested.
3. Connected hosted apps: use exact available tools in the current session (e.g., Google_Drive, vidIQ, Higgsfield); read/write permission is checked for every action. No raw OAuth tokens or model API keys pass through Core.
4. Skills with required app/compute: if unavailable, return `requires_connection`; do not claim the local instruction supplies the backend.
5. When names conflict: choose by complete source URI and exact plugin ID; never resolve solely by display name.

### Cross-plugin workflow sample
User asks for a science video channel plan: Core chooses 1–3 internal agent lenses (research, script, audit), reads `content-ai-vietnam/content-strategy` and `channel-growth-agent-vn/channel-growth-agent` skills if currently available, uses `vidIQ` tools only when they are available and consented, verifies public claims, then drafts a combined recommendation. The 3-connector probe in the catalog is **not** a substitute for checking that tool is present when the task runs.

### No silent side effects
Do not auto-publish media, modify repositories, delete files, send mail, train models, start Docker, buy credits, or connect new providers without a user's specific request and host permissions.

### Rollback / future migration
Original plugins remain independent; Core contains no imported proprietary code to unravel. Remove/unlink the Core's catalog file or disable its routing section if it conflicts with source Skills. Keep the original Core's 128 profiles and 7 Skill text untouched. When future local VPS/server capability is explicitly requested, use the existing dormant runtime rather than importing provider binaries into this plugin.
