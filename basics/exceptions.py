# basics/exceptions.py


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return "Invalid number"


def safe_access(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"


def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
