# CI/CD Plan

- GitHub Actions workflow runs on `dev` and `main` plus all pull requests.
- Steps: checkout, set up Python 3.11, install dependencies, run `unittest` suite.
- Future tasks: add linting (ruff/flake8), type checks (mypy), and container build for deployment image.
- Coverage artifacts will be uploaded once tests exist; failures block merges via branch protection.
