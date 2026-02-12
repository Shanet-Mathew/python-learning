from basics.lists import (
    get_first_element,
    get_last_element,
    add_item,
    remove_item,
    get_even_numbers,
)


def test_get_first_element():
    assert get_first_element([1, 2, 3]) == 1


def test_get_last_element():
    assert get_last_element([1, 2, 3]) == 3


def test_add_item():
    assert add_item([1, 2], 3) == [1, 2, 3]


def test_remove_item():
    assert remove_item([1, 2, 3], 2) == [1, 3]


def test_get_even_numbers():
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
