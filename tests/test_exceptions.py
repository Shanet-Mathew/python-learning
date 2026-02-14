# tests/test_exceptions.py

import pytest
from basics.exceptions import divide, convert_to_int, safe_access, validate_age


def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) == "Cannot divide by zero"


def test_convert_to_int():
    assert convert_to_int("10") == 10
    assert convert_to_int("abc") == "Invalid number"


def test_safe_access():
    assert safe_access([1, 2, 3], 1) == 2
    assert safe_access([1, 2, 3], 5) == "Index out of range"


def test_validate_age():
    assert validate_age(25) == 25

    with pytest.raises(ValueError):
        validate_age(-5)
