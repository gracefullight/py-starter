# Repository Guidelines

## Project Structure & Module Organization
- `src/`: Application code. Entry point: `src/main.py` exposing `main()`.
- `tests/`: Pytest suite (e.g., `tests/test_main.py`).
- Config: `pyproject.toml` (tasks via `poethepoet`), `ruff.toml` (lint/format), `mypy.ini` (type checking), `.pre-commit-config.yaml` (hooks), `uv.lock` (locked deps).

## Build, Test, and Development Commands
Use `uv` for env + execution; tasks are defined in `pyproject.toml`.
- Install deps: `uv sync`
- Run app: `uv run poe run` (alias for `python src/main.py`)
- Test: `uv run poe test`
- Test w/ coverage: `uv run poe test-cov`
- Lint: `uv run poe lint`
- Format: `uv run poe format`
- Type check: `uv run poe type-check`
- All checks: `uv run poe all-checks`
- Pre-commit (manual): `uv run poe pre-commit` | Install hook: `uv run pre-commit install`

## Coding Style & Naming Conventions
- Formatting/Linting: Managed by Ruff; run formatter before committing.
- Line length: 100; quotes: double; indent: spaces (see `ruff.toml`).
- Python: target `py313`; add type hints—`mypy` runs in `strict` mode.
- Imports: isort via Ruff; first‑party is `src`.
- Naming: modules `snake_case.py`; functions/vars `snake_case`; classes `PascalCase`.

## Testing Guidelines
- Framework: `pytest` with optional coverage (`--cov=src`).
- Location/name: place tests under `tests/` as `test_*.py`; functions `test_*`.
- Assertions: allowed in tests (see per-file ignore `S101`).
- Run locally: `uv run poe test` or `uv run pytest tests/`.

## Commit & Pull Request Guidelines
- Commit style: Prefer Conventional Commits (e.g., `feat:`, `fix:`, `chore:`). Use imperative mood, short subject (<72 chars), and a clear body when needed.
- Before pushing: run `uv run poe all-checks` and ensure tests pass.
- PRs: include purpose, summary of changes, any screenshots/logs when relevant, and link related issues (e.g., `Closes #123`). Request at least one review.

## Security & Configuration Tips
- Requirements: Python >= 3.13 and `uv` (`pip install uv`).
- Do not commit secrets or large data; respect `.gitignore`.
- Keep dependencies minimal; use `uv add <pkg>` / `uv remove <pkg>` and commit `pyproject.toml` + `uv.lock`.
