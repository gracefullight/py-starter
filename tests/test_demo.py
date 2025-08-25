from demo.main import say_hello


def test_say_hello_default() -> None:
    assert say_hello() == "Hello, world!"


def test_say_hello_name() -> None:
    assert say_hello("Alice") == "Hello, Alice!"
