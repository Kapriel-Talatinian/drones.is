# Project GitHub Report

## 2.1 Repository Overview
- **Repository Name:** `drones.is`
- **URL:** Pending publication to GitHub (add remote URL once repository is pushed).
- **Branching Strategy:**
  - `main` for production-ready releases.
  - `dev` for integration and stabilization ahead of releases.
  - short-lived `feature/*` branches branched from `dev`, merged via pull requests after review.
- **Current branches created locally:** `main`, `dev`, `feature/mission-planning`, and working branch `work` for this change set.

## 2.2 Commits & Contribution
- **Total commits:** 5 (current local history).
- **Contributors (commit authors to date):** Flavio Tauzin, Ching Jui Lin, Jaehwi Yoo, Kapriel Talatinian.
- **Project team:** Flavio Tauzin, Ching Jui Lin, Jaehwi Yoo, Kapriel Talatinian.
- **Significant commits / features implemented:**
  - `e774c58`: Added initial GitHub Actions CI workflow and CI/CD plan.
  - `972d2e1`: Added mission planning package stub with waypoint generation and roadmap.
  - `ef98024`: Expanded README with objectives, branching model, and contributor roster.
  - `0d9d0cf`: Added initial README stub.

## 2.3 Pull Requests & Code Review
- **Open / merged PRs:** None yet (repository not pushed to GitHub).
- **Code review approach:**
  - Open a PR from each `feature/*` branch into `dev`.
  - Require at least one reviewer approval before merge.
  - Use draft PRs early to surface work-in-progress for feedback.

## 2.4 CI/CD & Testing
- **Testing tools / frameworks used:** Python `unittest` (configured in workflow; tests to be added alongside new modules).
- **Automated builds / deployment pipelines:** GitHub Actions workflow runs on pushes to `dev` and `main` and all PRs, installing Python 3.11 and executing the unit test suite.
- **Coverage and code quality summary:** Coverage not yet measured; plan to add coverage upload plus lint/type-check steps (ruff/mypy) in future iterations.
