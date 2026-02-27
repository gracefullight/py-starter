# Python Quality Gate

For every code change in this repository, enforce the following checks before reporting completion.

## Required checks

- Run `uv run poe lint`.
- Run `uv run poe type-check`.

## Failure policy

- Do not claim the task is complete if either command fails.
- Fix issues introduced by the current change first.
- If failures are clearly pre-existing and unrelated, report them explicitly with file paths and errors.

## Repository-specific note

Project tasks are defined in `pyproject.toml`:

- `lint = "ruff check src/ tests/"`
- `type-check = "mypy src/"`
