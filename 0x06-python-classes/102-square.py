#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square and comparison methods based on area."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size (int): Length of a side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Getter and setter for the length of a side of this square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the length of a side of this square."""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculates the area of this square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Checks if two squares have equal areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if two squares have different areas."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Checks if this square has a greater area than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if this square has a greater or equal area to the other."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Checks if this square has a smaller area than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if this square has a smaller or equal area to the other."""
        return self.area() <= other.area()
