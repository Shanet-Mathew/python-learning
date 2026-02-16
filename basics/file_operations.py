# basics/file_operations.py


def write_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)


def read_from_file(filename):
    with open(filename, "r") as file:
        return file.read()


def append_to_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)
