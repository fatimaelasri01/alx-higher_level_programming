#!/usr/bin/python3
"""Manages a square's size, position, and printing a square with."""


class Square:
    """Represents a square with attributes for size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with size and position.

        Args:
            size: Length of the side of a square.
            position: Tuple representing the position of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position attribute."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square to stdout using '#' characters."""
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
