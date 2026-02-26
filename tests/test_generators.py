# tests/test_generators.py

from basics.generators import CountDown, number_generator, even_generator


def test_countdown():
    countdown = CountDown(3)
    result = list(countdown)
    assert result == [3, 2, 1]


def test_number_generator():
    result = list(number_generator(5))
    assert result == [0, 1, 2, 3, 4]


def test_even_generator():
    result = list(even_generator(6))
    assert result == [0, 2, 4]