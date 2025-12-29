# Contributing

Thank you for helping build the autonomous seed-planting drone. We simulate a real workflow.

## Branching and forks
- Work from the `dev` branch; create focused `feature/*`, `fix/*`, or `chore/*` branches per task.
- Fork-first is encouraged for external collaborators; team members may push branches to the main repo.
- Keep branch names descriptive: `feature/seed-drop-spacing`, `feature/telemetry-logging`, `chore/ci-hardening`.

## Commits and authorship
- Configure Git with your edu.ece.fr identity, e.g. `git config user.email "name-surname@edu.ece.fr"` and `git config user.name "Full Name"`.
- Add `Co-authored-by:` trailers when pairing so shared effort shows in the log.
- Write concise commit messages with context ("Add seed drop pattern generator", "Wire CI to run unittest").

## Pull requests
- Open PRs from your feature branch into `dev`; assign a reviewer different from the author.
- Include a short summary, testing notes, and screenshots if UI changes occur.
- Allow CI to finish before requesting review; address review comments with follow-up commits.

## Testing and quality
- Run `python -m unittest discover` before pushing. If adding PyTest, include `pytest` in `requirements.txt` and extend the CI workflow.
- Keep changes small and incremental. If a change is risky, add a quick design note in the PR description.

## Issue tracking
- Use GitHub issues to capture bugs and feature requests. Link issues in PR descriptions (`Closes #<id>`).
- Update `GITHUB_REPORT.md` after major milestones so stakeholders can follow along.
