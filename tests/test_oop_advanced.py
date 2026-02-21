# tests/test_oop_advanced.py

import pytest
from basics.oop_advanced import Dog, Cat, Rectangle


def test_polymorphism():
    dog = Dog("Buddy")
    cat = Cat("Kitty")

    assert dog.speak() == "Woof"
    assert cat.speak() == "Meow"


def test_inheritance_name():
    dog = Dog("Buddy")
    assert dog.get_name() == "Buddy"


def test_rectangle_area():
    rect = Rectangle(4, 5)
    assert rect.area() == 20


def test_rectangle_set_width():
    rect = Rectangle(4, 5)
    rect.set_width(10)
    assert rect.area() == 50
