#!/usr/bin/python3
"""Defines a rectangle, computes area and perimeter, prints rectangle, repr"""


class Rectangle:
    """Class that defines a rectangle by width and height"""

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return(self.width * self.height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (self.width * 2) + (self.height * 2)
        return(perimeter)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return("")
        return(("#" * self.width + "\n")*(self.height - 1)+("#" * self.width))

    def __repr__(self):

        return("Rectangle({}, {})".format(self.width, self.height))
