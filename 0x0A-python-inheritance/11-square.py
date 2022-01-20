#!/usr/bin/python3
"""class square that inherits from Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square that inherits from Rectangle class"""

    def __init__(self, size):
        Square.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        return(self.__size ** 2)

    def __str__(self):
        return("[Square] {}/{}".format(self.__size, self.__size))
