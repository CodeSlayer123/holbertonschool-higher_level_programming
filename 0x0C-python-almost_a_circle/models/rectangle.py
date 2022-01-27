#!/usr/bin/python3
from models.base import Base
"""Class Rectangle that inherits from class Base"""


class Rectangle(Base):
    """Class Rectangle that inherits from class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) != int:
            raise TypeError("{} must be an integer".format("width"))
        if width <= 0:
            raise ValueError("{} must be > 0".format("width"))
        if type(height) != int:
            raise TypeError("{} must be an integer".format("height"))
        if height <= 0:
            raise ValueError("{} must be > 0".format("height"))
        if type(x) != int:
            raise TypeError("{} must be an integer".format("x"))
        if x < 0:
            raise ValueError("{} must be >= 0".format("x"))
        if type(y) != int:
            raise TypeError("{} must be an integer".format("y"))
        if y < 0:
            raise ValueError("{} must be >= 0".format("y"))

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    # width

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("width"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = value

    # height

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("height"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = value

    # x

    @property
    def x(self):
        return(self.__x)

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("x"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = value

    # y

    @property
    def y(self):
        return(self.__y)

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("y"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = value

    def area(self):
        return(self.__width * self.__height)

    def display(self):
        for i in range(self.__y):
            print()
        for i in range(self.height):
            print(' ' * self.__x + "#" * self.__width)

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.__x, self.__y,
                       self.__width, self.__height))

    def update(self, *args, **kwargs):
        flag = 1
        if args is not None:
            flag = 0
        if len(args) > 0 and flag == 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):

        ted = {'id': self.id, 'width': self.width,
               'height': self.height, 'x': self.x, 'y': self.y}
        return(ted)
