from basics.loops import (
    sum_of_numbers,
    find_even_numbers,
    countdown,
    multiplication_table,
)


def test_sum_of_numbers():
    assert sum_of_numbers(5) == 15


def test_find_even_numbers():
    assert find_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_countdown():
    assert countdown(3) == [3, 2, 1, 0]


def test_multiplication_table():
    assert multiplication_table(3) == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]