# tests/test_memory_model.py

from basics.memory_model import (
    modify_list,
    reassign_number,
    check_identity,
    shallow_copy_list,
    deep_copy_list,
)


def test_modify_list():
    original = [1, 2, 3]
    modified = modify_list(original)

    assert modified == [1, 2, 3, 100]
    assert original == [1, 2, 3, 100]  # original changed (mutable)


def test_reassign_number():
    num = 5
    result = reassign_number(num)

    assert result == 15
    assert num == 5  # original unchanged (immutable)


def test_identity():
    a = [1, 2]
    b = a
    c = [1, 2]

    assert check_identity(a, b) is True
    assert check_identity(a, c) is False


def test_shallow_copy():
    original = [[1, 2], [3, 4]]
    copied = shallow_copy_list(original)

    copied[0][0] = 99

    # Shallow copy shares inner objects
    assert original[0][0] == 99


def test_deep_copy():
    original = [[1, 2], [3, 4]]
    copied = deep_copy_list(original)

    copied[0][0] = 99

    # Deep copy does NOT share inner objects
    assert original[0][0] == 1