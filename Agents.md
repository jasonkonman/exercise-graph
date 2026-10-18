## Source of Truth Docs
- Requirements: `./.docs/requirements/*.md`
    - primarily used by me
- Plans: `./.docs/plans/*.md`
    - Plans should be updated to reflect the implementation plan for each slice of work
- Wiki: `./.docs/wiki.`
    - The wiki is the cumulative docs, reflecting latest state, key decisions, for this project.
    - should be organised 1 md file per topic
    - serves as the entry point for any user, agent to understand the project
- Feature requests: `docs/requirements/98-feature-requests.md`

## Workflow Phases
- `{req}`: update or expand functional requirements in `docs/requirements/`.
- `{plan}`: produce a plan in `docs/plans/` that is self-contained and clear for execution.
- `{build}`: implement code changes guided by a plan or ad-hoc instructions.
- `{ask}`: exploratory questions only; do not change requirements or code.
- `{fix}`: small focused fixes outside the full req/plan/build flow.


## Git Rules
- No commits directly on `main`.
- Each new plan is a new branch:
  - Features: `feature/*`
  - Bug fixes: `bugfix/*`
- Before creating a new branch, always `git fetch origin` and `git rebase origin/main`.
- commit to the branch everytime a new chunk / feature has been completed. One plan can have multiple commits
- At the end of a build, prompt whether to open a PR.
- PRs should be squash-merged to `main`.
 - Warn before merging a PR to `main`.

## Collaboration Expectations
- Ask clarifying questions before build if scope is ambiguous or dependencies are missing.
- Call out when something seems wrong or inconsistent with existing requirements.
- Update instruction files when new instructions are provided.