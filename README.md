# drones.is

Autonomous AI-driven drone platform for precision seed planting on agricultural plots. The project coordinates flight planning, terrain awareness, and seed deployment to accelerate reforestation and regenerative farming efforts.

## Objectives
- Design a modular flight controller that can fly low and slow over designated plots.
- Use computer vision to detect viable planting zones and avoid obstacles.
- Automate seed pod deployment with configurable spacing and patterns.
- Collect telemetry for post-flight analysis and iterative model tuning.

## Repository Layout
- `src/` — runtime code for mission planning, navigation, and deployment.
- `docs/` — project documentation, plans, and team information.
- `.github/workflows/` — CI workflows for linting and tests.

## Branching Model
- `main` — production-ready snapshots.
- `dev` — integration branch where features converge before release.
- `feature/*` — short-lived branches for focused tasks merged via PRs into `dev`.

## Getting Started
1. Clone the repository and check out `dev` for day-to-day development.
2. Create a `feature/<short-name>` branch off `dev` for each task.
3. Add tests for new modules, run CI locally, and open a PR for review.
4. Use your edu.ece.fr identity (e.g., `name-surname@edu.ece.fr`) when committing to keep authorship consistent.

## Development & Testing
- Fork-first contributions are welcome; open pull requests from your fork or local `feature/*` branch into `dev`.
- CI runs `python -m unittest` today and will add linting, typing (mypy), and coverage upload as the codebase grows.
- Prefer small, reviewable PRs with at least one teammate approval before merging into `dev` and subsequently `main`.

## Contributors
- Flavio Tauzin — mission planning & UX — flavio-tauzin@edu.ece.fr
- Ching Jui Lin — perception & ML pipeline — chingjui-lin@edu.ece.fr
- Jaehwi Yoo — navigation & guidance — jaehwi-yoo@edu.ece.fr
- Kapriel Talatinian — platform integration & tooling — kapriel-talatinian@edu.ece.fr
