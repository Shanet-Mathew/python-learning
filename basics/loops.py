
def sum_of_numbers(n):
    """
    Returns the sum of numbers from 1 to n.
    Example: sum_of_numbers(5) -> 15
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def find_even_numbers(numbers):
    """
    Returns a list of even numbers from the given list.
    Example: [1,2,3,4] -> [2,4]
    """
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


def countdown(start):
    """
    Returns a countdown list from start to 0.
    Example: countdown(3) -> [3,2,1,0]
    """
    result = []
    while start >= 0:
        result.append(start)
        start -= 1
    return result


def multiplication_table(number):
    """
    Returns multiplication table (1–10) of a number.
    Example: multiplication_table(3)
    -> [3,6,9,12,15,18,21,24,27,30]
    """
    table = []
    for i in range(1, 11):
        table.append(number * i)
    return table
