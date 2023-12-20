#!/usr/bin/python3
"""Manages the size attribute and validates its type and value."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initializes a square with a given size.

        Args:
            size: Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = int(size)

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
