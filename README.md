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

## Contributors
- Flavio Tauzin — mission planning & UX
- Ching Jui Lin — perception & ML pipeline
- Jaehwi Yoo — navigation & guidance
- Kapriel Talatinian — platform integration & tooling
