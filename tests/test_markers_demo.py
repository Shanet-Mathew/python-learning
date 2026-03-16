# tests/test_markers_demo.py

import pytest
from basics.markers_demo import add, multiply, divide


@pytest.mark.smoke
def test_add():
    assert add(2, 3) == 5


@pytest.mark.regression
def test_multiply():
    assert multiply(3, 4) == 12


@pytest.mark.regression
def test_divide():
    assert divide(10, 2) == 5


@pytest.mark.smoke
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)