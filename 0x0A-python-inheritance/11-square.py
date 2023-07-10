#!/usr/bin/python3
# 11-square.py

"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    def area(self):
        """Returns the area of a rectangle."""
        return self.__size ** 2

    def __str__(self):
        """Creates a string object from a given object."""
        return "[Square] {}/{}".format(self.__size, self.__size)