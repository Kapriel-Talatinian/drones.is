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
- **Total commits:** 4 (current local history).
- **Contributors (commit authors to date):** Flavio Tauzin, Ching Jui Lin, Jaehwi Yoo, Kapriel Talatinian (commits authored with edu.ece.fr identities; pairing commits tagged via `Co-authored-by`).
- **Project team:** Flavio Tauzin, Ching Jui Lin, Jaehwi Yoo, Kapriel Talatinian.
- **Significant commits / features implemented:**
  - `96223ed`: Added CI plan, team roster, and edu.ece.fr author guidance (Kapriel Talatinian).
  - `8442238`: Simulated project setup with branching, CI scaffolding, and mission-planning stub (Flavio Tauzin, co-authored by Jaehwi Yoo).
  - `0d9d0cf`: Added initial README scaffold (Ching Jui Lin).

## 2.3 Pull Requests & Code Review
- **Active / planned PRs:**
  - `#1` `feature/mission-planning` → `dev` — reviewer: Jaehwi Yoo — status: planned (adds waypoint generator and drop pattern logic).
  - `#2` `feature/ci-hardening` → `dev` — reviewer: Kapriel Talatinian — status: planned (adds lint/type checks and coverage upload).
  - `#3` `feature/telemetry-logging` → `dev` — reviewer: Ching Jui Lin — status: drafting (adds structured telemetry recorder and replay harness).
  - `#4` `chore/repo-setup` → `main` — reviewer: Flavio Tauzin — status: merged (seeds repo with docs and CI skeletons).
- **Code review approach:**
  - Open a PR from each `feature/*` branch (or contributor fork) into `dev`.
  - Require at least one reviewer approval before merge; CI must pass before merge.
  - Use draft PRs early to surface work-in-progress for feedback.

## 2.4 CI/CD & Testing
- **Testing tools / frameworks used:** Python `unittest` driven by `python -m unittest discover`; PyTest under evaluation in `feature/ci-hardening` for richer fixtures and parametrized cases.
- **Automated builds / deployment pipelines:** GitHub Actions workflow runs on pushes to `dev` and `main` and all PRs, setting up Python 3.11, installing dependencies, and executing the unit test suite. `feature/ci-hardening` appends lint (ruff), type checks (mypy), and coverage upload to the pipeline; nightly workflow will replay logged missions against the planner.
- **Coverage and code quality summary:** Coverage is not yet measured (no tests present). Quality bars: no lint/type errors on PRs once `feature/ci-hardening` merges; coverage gate targeted at ≥70% before promoting to `main`.
