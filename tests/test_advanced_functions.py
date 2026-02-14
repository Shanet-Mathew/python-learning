# tests/test_advanced_functions.py

from basics.advanced_functions import (
    square_number,
    get_squares,
    get_even_numbers,
    get_names_uppercase,
)


def test_square_number():
    assert square_number(4) == 16
    assert square_number(0) == 0


def test_get_squares():
    assert get_squares([1, 2, 3]) == [1, 4, 9]


def test_get_even_numbers():
    assert get_even_numbers([1, 2, 3, 4, 5]) == [2, 4]


def test_get_names_uppercase():
    assert get_names_uppercase(["john", "alice"]) == ["JOHN", "ALICE"]
