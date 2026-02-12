def get_first_element(items):
    return items[0]


def get_last_element(items):
    return items[-1]


def add_item(items, item):
    items.append(item)
    return items


def remove_item(items, item):
    if item in items:
        items.remove(item)
    return items


def get_even_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result
