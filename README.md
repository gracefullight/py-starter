# py-starter

This isn't just a collection of files. It's a foundation for **fast, modern, and reliable Python development**. It's designed to let you skip the tedious, error-prone setup and focus directly on building what matters.

I chose `uv` to fundamentally address the complexity of traditional Python environments, where `pip`, `venv`, and `pip-tools` are managed separately. `uv` unifies dependency management and script execution into a single, blazing-fast tool, dramatically boosting developer productivity.

## Core Principles

- **Speed:** Experience a near-instantaneous feedback loop. `uv` and `ruff` make dependency installation, linting, and formatting exceptionally fast.
- **Simplicity:** Eliminate complexity. A single, unified tool (`uv`) manages your entire project's environment and dependencies.
- **Reliability:** Build confidence from the first line of code. `ruff`, `mypy`, and `pytest` are integrated to prevent bugs and ensure stability.
- **Automation:** Let the machine handle the checklist. `pre-commit` hooks automate all quality checks, catching issues before they ever become part of the codebase.

## Getting Started

1. **Install dependencies**
   This command sets up your project's environment with all the necessary libraries and tools.
   ```sh
   uv sync
   ```

2. **Set up pre-commit hooks** (optional but recommended)
   Automate code quality checks before each commit.
   ```sh
   uv run pre-commit install
   ```

3. **Run your project**
   Execute the main application entrypoint to verify your setup is working correctly.
   ```sh
   uv run src/main.py
   # or using the alias
   uv run poe run
   ```

4. **Add or remove packages**
   Seamlessly manage your project's third-party libraries.
   ```sh
   uv add <package>
   uv remove <package>
   ```

## Code Quality Management

- **Lint & Format:** Inconsistent code style and potential errors create friction and lead to bugs. `ruff` solves both problems at once with incredible speed.

  ```sh
  # Check for style issues and potential errors
  uv run ruff check src/ tests/
  # or using alias
  uv run poe lint

  # Automatically format all code
  uv run ruff format src/ tests/
  # or using alias
  uv run poe format
  ```

- **Type Check:** Runtime `TypeError`s are a common source of bugs. `mypy` performs static analysis to catch these errors before you ever run the code, making your application more robust.

  ```sh
  uv run mypy src/
  # or using alias
  uv run poe type-check
  ```

- **Pre-commit Hooks:** Great tools are useless if you forget to run them. `pre-commit` automates your quality checks, running them every time you commit. This fundamentally prevents low-quality code from entering your repository.

  ```sh
  # Run all configured hooks manually across all files
  uv run pre-commit run --all-files
  # or using alias
  uv run poe pre-commit
  ```

- **Run All Checks:** Execute all quality checks at once.

  ```sh
  uv run poe all-checks
  ```

## Testing

- **Run Tests:** Verify that your code behaves exactly as you intend. Tests are the cornerstone of reliable software.

  ```sh
  uv run pytest tests/
  # or using alias
  uv run poe test
  ```

- **Check Test Coverage:** Measure what percentage of your codebase is protected by tests. This metric is crucial for identifying untested areas and increasing confidence in your code's stability.

  ```sh
  uv run pytest tests/ --cov=src
  # or using alias
  uv run poe test-cov
  ```

## Available Scripts

The project includes several convenient aliases using `poethepoet`:

- `uv run poe run` - Run the main application
- `uv run poe test` - Run tests
- `uv run poe test-cov` - Run tests with coverage
- `uv run poe lint` - Check code style and potential errors
- `uv run poe format` - Format code
- `uv run poe type-check` - Run type checking
- `uv run poe pre-commit` - Run all pre-commit hooks
- `uv run poe all-checks` - Run all quality checks (lint, format, type-check, test)

## Requirements

- Python >=3.13
- uv (install via `pip install uv`)

---

Feel free to fork this project and use it as your own template!
