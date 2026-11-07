# GitHub500: Pilot batch of 25 repos — review status, 2026-11-04

**Scope: discovery/partial manual audit, not an independent security certification.** 25 pilot repo identities from the existing catalog, 23 license paths located (including `LICENSE.txt` for SciPy, OpenRemote and OpenRefine). `anthropics/skills` has licensing that varies by individual Skill, and `openlegaldata/awesome-legal-data` lacked a repository-wide license in paths checked — therefore no code is copied from either.

Three MIT-licensed upstream Skill source documents were read via GitHub connector and condensed into separate, **newly written Vietnamese native Skills**:
- Corey's `ab-testing` → `github500-ab-testing`
- K-Dense `experimental-design` → `github500-experimental-design`
- GitHub `agent-supply-chain` → `github500-agent-supply-chain`

For each, provenance under `skills/<skill>/references/PROVENANCE.md` includes source file and blob SHA. **Do not treat the blob SHA as the repository commit identifier.** Full upstream repos, supporting source scripts and dependency trees were not installed, downloaded wholesale or executed.

## Unresolved conditions and risk groups
- **Special/source-available/commercial restrictions**: Dify (modified Apache), Tencent Hunyuan3D (community/geographic restrictions), n8n (Sustainable Use), Activepieces (mixed enterprise), keep catalog/reference only pending full review.
- **Copyleft**: OpenRemote, electricitymaps, getopenpost, learnhouse (AGPL) require separate policy and integration licensing analysis; none is bundled.
- **Permissive but not reviewed fully**: SciPy, OpenRefine, github-mcp-server, MCP python-sdk, FinRL, OHIF, ML-For-Beginners, LangGraph, promptfoo, AgML, RobotecAI, ai-agents-for-beginners. Existing integrations are not changed.
- **Anthropic/skills**: per-skill license required; no root LICENSE discovered in first check; no copy.
- **openlegaldata/awesome-legal-data**: license not found in root; no copy.
- **Dependency security**: 0/25 full dependency/runtime security audits; 3/25 targeted static SKILL.md reviews only. Security risk cannot be ruled out.

## Execution/security boundaries
- No third-party repos cloned or upstream executables run; only GitHub read operations.
- No external model endpoint, VPN, VPS, Docker, OAuth transfer or credential access requested.
- 128 agent profiles and 7 legacy Skill files unchanged. Default embedded_skills_only unchanged.
- Local checksum helper is original stdlib Python code; only use when locally authorized. SHA-256 = file integrity against a trusted baseline, not provenance authentication or signing.
- Number **3 native Skills integrated** refers to native authored guidance, *not* three independent remote agent tools or upstream original executable deployment.
