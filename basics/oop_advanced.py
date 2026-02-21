# basics/oop_advanced.py


class Animal:
    def __init__(self, name):
        self._name = name   # protected attribute (encapsulation)

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

    def get_name(self):
        return self._name


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class Rectangle:
    def __init__(self, width, height):
        self.__width = width      # private attribute
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def set_width(self, width):
        if width > 0:
            self.__width = width
