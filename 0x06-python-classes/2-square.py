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
