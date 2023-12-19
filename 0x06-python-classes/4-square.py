#!/usr/bin/python3
"""class square definition"""

class Square:
    def __init__(self, size=0):
        self.__size = 0  # Private instance attribute

        # Check if size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Check if size is less than 0
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute."""
        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # Check if value is less than 0
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Public instance method to calculate the area of the square."""
        return self.__size ** 2
