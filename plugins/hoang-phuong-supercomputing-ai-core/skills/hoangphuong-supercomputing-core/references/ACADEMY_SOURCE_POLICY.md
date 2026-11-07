# Research Academy Source Policy — provenance, copyright, and data governance v14.3

**The included registry has ZERO approved third-party documents.** Sources should be imported **only** when review is complete. This plugin contains metadata schema/tools, not copied papers, textbooks, licensed datasets or an internet crawler.

## Required metadata for an approved source

- Stable `source_id`, human-readable `title`, canonical `canonical_url`, `rights_holder`, `license_id` and `license_evidence_url` proving the terms.
- `allowed_uses` are explicit, per-purpose: `quote`, `rag`, `training`, `redistribution`, `commercial`. Permission for one **does not imply** permission for another. Do not assume all CC/OSS terms automatically cover every jurisdiction or model-training use.
- `review_status` must be `human_reviewed`, `reviewer_id` nonempty, `reviewed_at` ISO date, and a documented attribution where required. Technical validation cannot authenticate a person's identity or verify a remote license claim.
- Metadata `pending_review`, `unknown`, missing rights holder/license evidence or suspected third-party restrictions must **fail closed**. No copying full external documents until separately authorized.
- For sources with a custom contract, human legal review is required. This utility only handles a **conservative metadata allowlist** CC0-1.0/CC-BY-4.0/MIT/Apache-2.0; it is not a legal opinion.
- Distinguish **retrieval/quotation**, **embedding in RAG**, **fine-tune/training**, **redistribution** and **commercial deployment**, including attribution/notice and privacy requirements.
- Before public or commercial release, confirm notices, copyright, database rights, personal data consent, and source terms again.

## CLI

`python skills/hoangphuong-supercomputing-core/scripts/research_academy.py licenses --root . --purpose rag`

Empty registry => `approved_sources: 0`, **not** evidence of a populated knowledge base. Passing metadata check means only required *self-declared fields* are present, never that a license is legally verified.
