#!/usr/bin/python3
from models.base import Base
"""Class Rectangle that inherits from class Base"""


class Rectangle(Base):
    """Class Rectangle that inherits from class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Function 1"""

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
        """Function 2"""

        return(self.__width)

    @width.setter
    def width(self, value):
        """Function 3"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format("width"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = value

    # height

    @property
    def height(self):
        """Function 4"""

        return(self.__height)

    @height.setter
    def height(self, value):
        """Function 5"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format("height"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = value

    # x

    @property
    def x(self):
        """Function 6"""

        return(self.__x)

    @x.setter
    def x(self, value):
        """Function 7"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format("x"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = value

    # y

    @property
    def y(self):
        """Function 8"""

        return(self.__y)

    @y.setter
    def y(self, value):
        """Function 9"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format("y"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = value

    def area(self):
        """Function 10"""

        return(self.__width * self.__height)

    def display(self):
        """Function 11"""

        for i in range(self.__y):
            print()
        for i in range(self.height):
            print(' ' * self.__x + "#" * self.__width)

    def __str__(self):
        """Function 12"""

        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.__x, self.__y,
                       self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Function 13"""

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
        """Function 14"""

        ted = {'id': self.id, 'width': self.width,
               'height': self.height, 'x': self.x, 'y': self.y}
        return(ted)
