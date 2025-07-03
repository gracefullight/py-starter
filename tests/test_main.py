import sys
from io import StringIO

import pytest

from src.main import main


def test_main_prints_hello(monkeypatch: pytest.MonkeyPatch) -> None:
    output = StringIO()
    monkeypatch.setattr(sys, "stdout", output)
    main()
    assert "Hello from starter!" in output.getvalue()
