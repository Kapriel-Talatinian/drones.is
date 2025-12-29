# Project GitHub Report

## 2.1 Repository Overview
- **Repository Name:** `drones.is`
- **URL:** Pending publication to GitHub (add remote URL once repository is pushed).
- **Branching Strategy:**
  - `main` for production-ready releases.
  - `dev` for integration and stabilization ahead of releases.
  - short-lived `feature/*` branches branched from `dev`, merged via pull requests after review.
  - contributors fork the repo when needed and open PRs from forks into `dev`.
- **Current branches created locally:** `main`, `dev`, `feature/mission-planning`, and working branch `work` for this change set.

## 2.2 Commits & Contribution
- **Total commits:** 3 (current local history).
- **Contributors (commit authors to date):** Flavio Tauzin, Ching Jui Lin, Jaehwi Yoo, Kapriel Talatinian (commits authored with edu.ece.fr identities).
- **Project team:** Flavio Tauzin, Ching Jui Lin, Jaehwi Yoo, Kapriel Talatinian.
- **Significant commits / features implemented:**
  - `8442238`: Simulated project setup with branching, CI scaffolding, and mission-planning stub.
  - `0d9d0cf`: Added initial README scaffold.

## 2.3 Pull Requests & Code Review
- **Planned PRs:**
  - `#1` `feature/mission-planning` → `dev` — reviewer: Jaehwi Yoo — status: planned (adds waypoint generator and drop pattern logic).
  - `#2` `feature/ci-hardening` → `dev` — reviewer: Kapriel Talatinian — status: planned (adds lint/type checks and coverage upload).
- **Code review approach:**
  - Open a PR from each `feature/*` branch (or contributor fork) into `dev`.
  - Require at least one reviewer approval before merge; CI must pass before merge.
  - Use draft PRs early to surface work-in-progress for feedback.

## 2.4 CI/CD & Testing
- **Testing tools / frameworks used:** Python `unittest` driven by `python -m unittest discover` (PyTest adoption tracked for richer assertions).
- **Automated builds / deployment pipelines:** GitHub Actions workflow runs on pushes to `dev` and `main` and all PRs, setting up Python 3.11, installing dependencies, and executing the unit test suite. Future workflow `feature/ci-hardening` branch will append lint, mypy, and coverage upload.
- **Coverage and code quality summary:** Coverage is not yet measured (no tests present); upcoming CI expansion will publish coverage artifacts and enforce lint/type-check gates before merge.
