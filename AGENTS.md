# Repository Guidelines

## Project Structure & Module Organization
- `src/`: Application code. Entry point: `src/main.py` exposing `main()`.
- Modules live under `src/<module>/` (e.g., `src/demo/`, `src/week1/`). With `pythonpath = ["src"]`, import modules as `import demo.main`.
- `tests/`: Pytest suite (e.g., `tests/test_main.py`, `tests/test_demo.py`).
- Key config: `pyproject.toml` (poethepoet tasks), `ruff.toml` (lint/format), `mypy.ini` (type checking), `.pre-commit-config.yaml` (hooks), `uv.lock` (deps).

## Build, Test, and Development Commands
- Install deps: `uv sync`.
- Run app: `uv run poe run` (alias for `python src/main.py`).
- Run a module: `uv run python src/demo/main.py`.
- Test: `uv run poe test`; Coverage: `uv run poe test-cov`.
- Lint/Format: `uv run poe lint` / `uv run poe format`.
- Type check: `uv run poe type-check`.
- All checks: `uv run poe all-checks`.
- Pre-commit: `uv run pre-commit install`, then `uv run poe pre-commit`.

## Coding Style & Naming Conventions
- Python 3.12 (>=3.12,<3.13); strict type hints enforced by `mypy`.
- Ruff manages linting and formatting; line length 100, double quotes, spaces for indent.
- Imports sorted by Ruff (isort); first‑party package root is `src`.
- Naming: modules/files `snake_case.py`; functions/variables `snake_case`; classes `PascalCase`.

## Testing Guidelines
- Framework: `pytest`; coverage measured with `--cov=src`.
- Place tests in `tests/` as `test_*.py` with functions `test_*`.
- Run tests via `uv run poe test` or `uv run pytest tests/`.

## Commit & Pull Request Guidelines
- Use Conventional Commits (e.g., `feat:`, `fix:`, `chore:`). Keep subjects <72 chars, imperative mood.
- Before pushing, run `uv run poe all-checks` and ensure tests pass.
- PRs should include purpose, a concise summary of changes, relevant logs/output, and linked issues (e.g., `Closes #123`). Request at least one review.

## Security & Configuration Tips
- Requirements: Python `>=3.12,<3.13` and `uv` (`pip install uv`).
- Don’t commit secrets or large data; follow `.gitignore`.
- Manage deps with `uv add <pkg>` / `uv remove <pkg>`; commit `pyproject.toml` and `uv.lock`.
