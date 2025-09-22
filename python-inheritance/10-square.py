#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size):
        """Initialize a square with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Return the string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
