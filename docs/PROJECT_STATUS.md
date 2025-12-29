# Project Status (Sprint simulation)

## In progress
- `feature/mission-planning` — owner: Flavio Tauzin — adding grid/line drop patterns and collision-aware waypoint smoothing.
- `feature/telemetry-logging` — owner: Jaehwi Yoo (reviewer: Ching Jui Lin) — capturing GPS, IMU, and drop timestamps for replay.
- `feature/ci-hardening` — owner: Kapriel Talatinian — integrating ruff, mypy, PyTest, and coverage upload to CI.

## Upcoming
- Terrain scoring model refresh using latest crop dataset — owner: Ching Jui Lin.
- Bench seed deployment actuator with adjustable timing — owner: Flavio Tauzin.
- Return-to-launch failsafe simulation in software-in-the-loop — owner: Jaehwi Yoo.

## Recently completed
- Repo scaffolding with README, roadmap, and CI skeleton — owner: Kapriel Talatinian (reviewed by Flavio Tauzin).
- Waypoint + seed drop primitives stubbed in `src/drone/mission.py` — owner: Flavio Tauzin (co-authored by Jaehwi Yoo).
