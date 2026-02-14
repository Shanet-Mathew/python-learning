

def square_number(n):
    return n * n


def get_squares(numbers):
    return list(map(lambda x: x * x, numbers))


def get_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


def get_names_uppercase(names):
    return list(map(lambda name: name.upper(), names))
