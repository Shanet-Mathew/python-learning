from basics.functions import (
    greet,
    add_numbers,
    get_min_max,
    multiply_all,
    user_info,
)


def test_greet_default():
    assert greet("John") == "Hello, John!"


def test_greet_custom_message():
    assert greet("John", "Hi") == "Hi, John!"


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_get_min_max():
    assert get_min_max([1, 5, 3]) == (1, 5)


def test_multiply_all():
    assert multiply_all(2, 3, 4) == 24


def test_user_info():
    assert user_info(name="John", age=25) == {"name": "John", "age": 25}
