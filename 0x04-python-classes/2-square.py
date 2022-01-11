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
        """[returns square area of square size]
        """
        return(self.__size**2)