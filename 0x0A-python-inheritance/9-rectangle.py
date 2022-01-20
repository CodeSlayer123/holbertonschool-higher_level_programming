#!/usr/bin/python3
"""Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        Rectangle.integer_validator(self, "width", width)
        Rectangle.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return(self.__width * self.__height)

    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__width, self.__height))