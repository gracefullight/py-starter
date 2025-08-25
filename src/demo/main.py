from __future__ import annotations


def say_hello(name: str = "world") -> str:
    """Return a friendly greeting.

    Examples
    --------
    >>> say_hello()
    'Hello, world!'
    >>> say_hello("Alice")
    'Hello, Alice!'

    """
    return f"Hello, {name}!"


def main() -> None:
    """Small CLI entry to demonstrate usage."""
    # Ignore T20 rule (print statement prohibition)
    print(say_hello("demo"))  # noqa: T201


if __name__ == "__main__":
    main()
