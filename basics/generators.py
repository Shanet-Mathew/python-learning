# basics/generators.py


class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current


def number_generator(n):
    for i in range(n):
        yield i


def even_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i