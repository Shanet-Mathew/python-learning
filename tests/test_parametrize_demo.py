import pytest


def add(a, b):
    return a + b


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 200, 300),
    ]
)
def test_add(a, b, expected):
    assert add(a, b) == expected