# basics/memory_model.py

import copy


def modify_list(lst):
    """
    Demonstrates mutability.
    Modifies the original list.
    """
    lst.append(100)
    return lst


def reassign_number(x):
    """
    Demonstrates immutability.
    Reassigning does not modify original.
    """
    x = x + 10
    return x


def check_identity(a, b):
    """
    Returns whether two variables point to same object.
    """
    return a is b


def shallow_copy_list(lst):
    """
    Returns a shallow copy of a list.
    """
    return copy.copy(lst)


def deep_copy_list(lst):
    """
    Returns a deep copy of a list.
    """
    return copy.deepcopy(lst)