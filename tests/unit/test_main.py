import pytest

from src.main import (
    hello,
    main,
)

def test_hello():
    expected = "Hello world!"
    actual = hello()
    assert actual == expected

def test_main():
    main()
