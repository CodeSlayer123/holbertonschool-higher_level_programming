#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """[initializes square size]

        Args:
            size (int): [size of square]. Defaults to 0.

        Raises:
            TypeError: [size must be an intege]
            ValueError: [size must be >= 0]
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """[returns square area of size of square]
        """
        return(self.__size**2)
    @property
    def size(self):
        """[gets size of square]
        """
        return(self.__size)

    @size.setter
    def size(self, value):
        """[Sets size of square]

        Args:
            value ([int]): [size of square to be set]

        Raises:
            TypeError: [size must be an integer]
            ValueError: [size must be >= 0]
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value