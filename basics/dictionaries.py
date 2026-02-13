def get_value(data, key):
    return data.get(key)


def add_key_value(data, key, value):
    data[key] = value
    return data


def remove_key(data, key):
    if key in data:
        del data[key]
    return data


def get_keys(data):
    return list(data.keys())


def get_values(data):
    return list(data.values())


def filter_even_values(data):
    result = {}
    for key, value in data.items():
        if value % 2 == 0:
            result[key] = value
    return result
