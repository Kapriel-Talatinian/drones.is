# CI/CD Plan

- GitHub Actions workflow runs on `dev` and `main` plus all pull requests; contributors may run it from forks via PRs.
- Steps: checkout, set up Python 3.11, install dependencies, run `unittest` suite via `python -m unittest discover`.
- Future tasks: add linting (ruff/flake8), type checks (mypy), coverage upload, and container build for deployment image.
- Coverage is currently unreported (no tests yet); once enabled, branch protection will block merges on failed checks or reduced coverage.
- Proposed matrix: Python `3.10` / `3.11`, Ubuntu and macOS runners; nightly workflow replays telemetry logs to catch regressions in the planner.
