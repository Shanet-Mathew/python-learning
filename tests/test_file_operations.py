# tests/test_file_operations.py

from basics.file_operations import write_to_file, read_from_file, append_to_file


def test_write_and_read(tmp_path):
    file = tmp_path / "test.txt"

    write_to_file(file, "Hello")
    content = read_from_file(file)

    assert content == "Hello"


def test_append(tmp_path):
    file = tmp_path / "test.txt"

    write_to_file(file, "Hello")
    append_to_file(file, " World")

    content = read_from_file(file)

    assert content == "Hello World"
