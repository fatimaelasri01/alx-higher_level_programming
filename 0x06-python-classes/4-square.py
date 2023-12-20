#!/usr/bin/python3
"""Manages and validates the size attribute of a square."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initializes a square with a given size.

        Args:
            size: Length of the side of a square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the value of the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
