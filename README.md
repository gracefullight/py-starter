## UV

- uv init
- uv add package
- uv remove package
- uv run main.py

## 린트

- uv run ruff check src/      # 코드 린팅 (스타일, 품질, 타입 등 포괄적 검사)
- uv run ruff format src/     # 코드 자동 포맷팅
- uv run ruff check --fix src/ # 자동으로 수정 가능한 문제 해결
- uv run mypy src/           # 타입 검사
- uv run pre-commit run --all-files # pre-commit 훅 검사
