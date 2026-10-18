# Exercise Graph agent instructions

## Project purpose

Build a corpus of individual physical exercises, their characteristics, variants,
and supporting evidence. The current POC must be useful for finding, inspecting,
and comparing exercises on their own. Circuit/session construction and personalized
programming are later workflows and must not drive the initial corpus requirements.

The exercise corpus, graph claims, and programming recommendations must be grounded
in scientific research on physical training. Scientific grounding is a product
requirement, not a label applied to an exercise list.

## Source of truth

- Requirements: `.docs/requirements/*.md`; these describe intended behaviour.
- Plans: `.docs/plans/*.md`; keep each implementation plan self-contained and current.
- Wiki: `.docs/wiki/*.md`; one topic per file, documenting research, decisions, and
  the latest implemented state. Label proposals separately from implemented features.
- Feature requests: `.docs/requirements/98-feature-requests.md`, when created.
- Initial corpus/graph research: `.docs/wiki/exercise-corpus-and-graph.md`.
- Database decision and local operation: `.docs/wiki/local-database.md`.
- Exercise-science synthesis: `.docs/wiki/exercise-science-review.md`.
- Search, source, and draft claim records: `.docs/research/2026-10-18/*.json`.

Use `.docs/` consistently. The repository has documentation and local database
tooling; the exercise application is not implemented. Use the verified commands
in the database guide and do not invent application build or test commands.

## Persistence decision and local development

- Use PostgreSQL 17 as the POC's single authoritative store for exercises, typed
  relationships, evidence, reviews, and later programme/session records.
- Use `scripts/dev-postgres.sh` for this Debian 13 cloud environment. It installs
  without root and starts a private Unix-socket instance; keep its data outside Git.
- Keep JSON seed/export files reviewable and versioned. Do not introduce a second
  writable database merely for convenience.
- SQLite is an alternative if the product is explicitly reduced to a single-user
  embedded application, not a parallel persistence implementation or substitute
  for PostgreSQL integration tests.
- Defer DuckDB until analytical queries over exports justify it. Treat any such
  analysis as derived from the authoritative store.
- Defer Chroma and embeddings until a measured semantic-retrieval need exists.
  Start with structured queries and PostgreSQL text search; evaluate pgvector if
  vectors become useful. Similarity is not evidence quality or scientific validity.
- Research access was rechecked successfully through Europe PMC, including an
  open-access full-text download. Recheck failed destinations individually rather
  than assuming that all internet access is available or blocked.

## Scientific grounding and provenance

- Separate anatomical/biomechanical descriptions, training-outcome claims,
  programming policies, coach heuristics, and client observations.
- Use anatomy/biomechanics references for descriptive exercise annotations and
  training research for outcome claims. Do not require a programming trial for
  every catalog attribute, or treat a programming review as proof of every muscle
  label. Fill exercise-specific evidence gaps during curation and retain unknowns.
- Attach evidence to the specific claim or rule it supports. A citation on an
  exercise, or a shared muscle tag, does not support every recommendation about it.
- Record source identifiers/URLs, publication year, access date, relevant passage
  or table, population, intervention/comparator, outcome, limitations, reviewer,
  and review status. Record abstract-only access explicitly.
- Assess the body of evidence for the question. Prefer relevant systematic reviews,
  meta-analyses, and current professional guidance, then applicable primary studies.
  Check applicability, risk of bias, conflicting findings, corrections, retractions,
  and newer evidence; publication type alone does not establish certainty.
- Do not generalize population averages into precise individual prescriptions.
  Acute measurements such as EMG do not alone establish long-term hypertrophy,
  strength improvement, injury risk, or universal exercise superiority.
- Treat exercise substitutions, circuit pairings, and progression rules as
  context-dependent. Label coach judgment and untested hypotheses honestly.
- Distinguish unknown, unsupported, contradicted, and inapplicable claims. Keep
  uncertainty visible; do not invent citations, effect sizes, or confidence scores.
- Generated summaries and imported datasets are drafting aids. Require human
  review before their claims or policies become eligible for recommendations.
- Record dataset origin, revision, licence, attribution, and redistribution rights.
  Check media separately from code and descriptive data.
- Record a recommendation's corpus version, rule version, inputs, constraints,
  rationale, and evidence. Permit coach review and override with a recorded reason.
- Keep identifiable client records separate from the shared public corpus. Do not
  commit personal client information or credentials to the repository.

## Workflow phases

- `{req}`: update or expand functional requirements in `.docs/requirements/`.
- `{plan}`: produce a self-contained implementation plan in `.docs/plans/`.
- `{build}`: implement changes guided by a plan or explicit ad-hoc instructions.
- `{ask}`: exploratory questions only; do not change requirements or code.
- `{fix}`: small, focused fixes outside the full requirement/plan/build flow.

For research tasks, save findings and sources in the wiki. Clearly distinguish
sources actually inspected from candidates awaiting verification. Report access
limitations and outstanding research without presenting them as completed review.

## Git rules

- Do not commit directly on `main`.
- Use a new branch for each new plan: `feature/*` for features, `bugfix/*` for fixes.
- Before creating a branch, run `git fetch origin` and `git rebase origin/main`.
  Check the working tree first; preserve existing user changes and stop if rebasing
  would require a destructive action or an unresolved user decision.
- Commit each completed chunk of work to its branch. One plan may have several commits.
- At the end of a build, ask whether to open a PR. Do not merge without authorization.
- PRs should be squash-merged to `main`; warn before merging.

## Collaboration and validation

- Ask clarifying questions before building when ambiguity or missing dependencies
  prevents useful progress. Otherwise state reasonable assumptions and proceed.
- Call out inconsistencies with requirements and gaps in the evidence.
- Update this instruction file when the user provides new instructions.
- For documentation changes, check paths, references, consistency, and the diff.
  For implementation changes, run the relevant existing checks and report their
  actual outcomes. Never describe proposed features or unrun tests as verified.
