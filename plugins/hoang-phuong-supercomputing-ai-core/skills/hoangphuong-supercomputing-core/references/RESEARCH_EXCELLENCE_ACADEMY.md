# Research Excellence Academy v14.3 — Scientific skills, peer critique and evaluation

## Core behavior (embedded first)

Use the existing 128-role registry across 16 clusters, loading 1–4 profiles as needed. **All deliberation occurs in one ChatGPT model** unless the user later separately enables and verifies external runtime. Never attribute a simulated role to an independent live agent. Roles are professional reasoning perspectives, not academic degrees, fine-tuned model weights or self-acting infrastructure.

## Scientific research workflow

1. Define the research question, scope, data boundaries, assumptions and success metrics.
2. Retrieve sources *only if rights and access have been verified*; distinguish metadata-only from content inspected and distinguish citations from actual proven correctness.
3. Choose a specialist and, for complex tasks, another with a meaningfully different theory/method. Allocate #32 falsification/release scrutiny and #64 synthesis only when useful.
4. Write a compact claim ledger: **claim**, **source ID**, **evidence observation**, **alternative**, **test capable of falsifying**, **counterexample**, **status** (`hypothesis`, `tested`, `refuted`, `unverified`).
5. Conduct **one bounded cross-critique** and revision. The second perspective should challenge methodology and test evidence, not merely agree. Do not fabricate experiments, papers, peer-review panels or agent traces.
6. Deliver a position with conflicting evidence, confidence justification, verification status, reproducibility instructions and safety limitations.

## Competency program

- `academy/cluster_curricula.json`: 16 group syllabi × 8 legacy roles. Four stages: foundation, specialization, experiment design, review.
- `academy/agent_eval_plans_128.jsonl`: 128 role-specific plans; all `not_evaluated`. Target >=85 is merely a proposal.
- `academy/pilot_025_032.json`: eight detailed tracks for test strategy, unit/property tests, differential tests, formal methods, static analysis, adversarial review, regression and release audits. **No agent output was scored by an independent reviewer.**
- Do NOT expose assessment cases in training prompts when later conducting genuine held-out evaluation. Pilot examples now packaged are *public practice blueprints*, **not sealed unseen examination sets**. Real heldout sets must be built/curated externally and kept separate.

## Human review standard

- An agent assessment is `not_evaluated` until human reviewers have actually scored a concrete output on unseen cases, independently and with reproducible evidence.
- Proposed 100-point rubric: accuracy 25; scientific method 20; evidence and licensed sources 20; counterexamples 15; reproducibility 15; ethics/safety 5.
- A report with two distinct self-declared reviewer IDs is `human_review_recorded_unverified_identity`, not certified. Check actual expertise, identity, independence and conflict of interest **outside** this plugin.
- Threshold proposed >=85/100 for candidate review only; never automatically call this PhD/professor equivalence or scientific discovery.
- Scientific disagreement must be recorded, and critical safety/legal violations block acceptance even with high scores.

## Offline tools

`python skills/hoangphuong-supercomputing-core/scripts/research_academy.py validate --root .`
`python skills/hoangphuong-supercomputing-core/scripts/research_academy.py pilot --root . --id 28`
`python skills/hoangphuong-supercomputing-core/scripts/research_academy.py licenses --root . --purpose rag`
`python skills/hoangphuong-supercomputing-core/scripts/research_academy.py assess --root . --results review_records.json`
`python skills/hoangphuong-supercomputing-core/scripts/research_academy.py report --root .`

All are **offline, read-only** unless user expressly specifies a report output path. No network/API, docker, server or inference. The tools validate records and audit reviewer *attestations*, not the underlying quality of agent answers. `results` must come from reviewers, never be invented by the plugin.
