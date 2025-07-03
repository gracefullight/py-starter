# py-starter

A modern Python starter project using [uv](https://github.com/astral-sh/uv) for dependency management, with best practices for linting, formatting, type checking, and pre-commit hooks.

## Quick Start

1. **Install dependencies**

   ```sh
   uv pip install
   ```

2. **Add or remove packages**

   ```sh
   uv add <package>
   uv remove <package>
   ```

3. **Run your project**

   ```sh
   uv run src/main.py
   ```

## Code Quality & Automation

- **Lint code** (style, quality, type checks)

  ```sh
  uv run ruff check src/
  ```

- **Auto-format code**

  ```sh
  uv run ruff format src/
  ```

- **Auto-fix lint issues**

  ```sh
  uv run ruff check --fix src/
  ```

- **Type check**

  ```sh
  uv run mypy src/
  ```

- **Run all pre-commit hooks**

  ```sh
  uv run pre-commit run --all-files
  ```

## Testing

- **Run tests**

  ```sh
  uv run pytest
  ```

- **Run tests with coverage**

  ```sh
  uv run pytest --cov=src
  ```

## Requirements

- Python >=3.13
- [uv](https://github.com/astral-sh/uv) (install via `pip install uv`)

---

Feel free to fork and use as your own Python project template!
