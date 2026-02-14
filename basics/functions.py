def greet(name, message="Hello"):
    return f"{message}, {name}!"


def add_numbers(a, b):
    return a + b


def get_min_max(numbers):
    return min(numbers), max(numbers)


def multiply_all(*args):
    result = 1
    for number in args:
        result *= number
    return result


def user_info(**kwargs):
    return kwargs
