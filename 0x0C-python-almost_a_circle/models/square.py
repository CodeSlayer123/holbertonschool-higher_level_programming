#!/usr/bin/python3
"""Class Square that inherits from class Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Function 1"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Function 2"""

        return("[Square] ({}) {}/{} - {}".
               format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Function 3"""

        return(self.width)

    @size.setter
    def size(self, value):
        """Function 4"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format("width"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Function 5"""

        flag = 1
        if args is not None:
            flag = 0
        if len(args) > 0 and flag == 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """Function 6"""

        fred = {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}

        return(fred)
