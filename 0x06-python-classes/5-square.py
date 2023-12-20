#!/usr/bin/python3
"""Manages square attributes and operations."""


class Square:
    """Represents a square with a size attribute."""

    def __init__(self, size=0):
        """Initializes a square with a given size."""
        self.size = size

    @property
    def size(self):
        """Retrieves the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' characters."""
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            print("#" * self.__size)
