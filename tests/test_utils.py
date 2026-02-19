# tests/test_utils.py

from basics.math_utils import add, subtract
from basics.string_utils import reverse_string, capitalize_text


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_reverse_string():
    assert reverse_string("hello") == "olleh"


def test_capitalize_text():
    assert capitalize_text("python") == "Python"
