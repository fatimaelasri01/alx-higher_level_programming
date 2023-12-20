#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square with private instance attributes size and position"""

    def __str__(self):
        """Returns a string representation of the square"""
        return self.square_representation()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """constructor.

        Args:
            size: Length of the side of the square
            position: Tuple representing the position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute"""

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square"""
        return self.__size ** 2

    def square_representation(self):
        """Generates a string representation of the square"""
        ret = ""
        if not self.size:
            return "\n"

        for i in range(self.position[1]):
            ret += "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                ret += " "
            for j in range(self.size):
                ret += "#"
            ret += "\n"
        return ret

    def display(self):
        """Prints the square"""
        print(self.square_representation(), end="")
