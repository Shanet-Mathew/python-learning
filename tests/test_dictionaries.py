from basics.dictionaries import (
    get_value,
    add_key_value,
    remove_key,
    get_keys,
    get_values,
    filter_even_values,
)


def test_get_value():
    assert get_value({"a": 1, "b": 2}, "a") == 1


def test_add_key_value():
    assert add_key_value({"a": 1}, "b", 2) == {"a": 1, "b": 2}


def test_remove_key():
    assert remove_key({"a": 1, "b": 2}, "a") == {"b": 2}


def test_get_keys():
    assert get_keys({"a": 1, "b": 2}) == ["a", "b"]


def test_get_values():
    assert get_values({"a": 1, "b": 2}) == [1, 2]


def test_filter_even_values():
    assert filter_even_values({"a": 1, "b": 2, "c": 4}) == {"b": 2, "c": 4}
