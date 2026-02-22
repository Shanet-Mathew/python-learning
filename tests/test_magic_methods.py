# tests/test_magic_methods.py

from basics.magic_methods import Book, Vector


def test_str_and_len():
    book = Book("Python", 300)
    assert str(book) == "Python (300 pages)"
    assert len(book) == 300


def test_repr():
    book = Book("Python", 300)
    assert repr(book) == "Book(title='Python', pages=300)"


def test_equality():
    book1 = Book("Python", 300)
    book2 = Book("Python", 300)
    book3 = Book("Java", 200)

    assert book1 == book2
    assert book1 != book3


def test_vector_addition():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    result = v1 + v2

    assert result == Vector(4, 6)
