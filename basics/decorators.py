# basics/decorators.py

import time


def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"Function {func.__name__} executed"
    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return end - start
    return wrapper


def require_positive(func):
    def wrapper(number):
        if number < 0:
            return "Number must be positive"
        return func(number)
    return wrapper


@require_positive
def square(number):
    return number * number