#!/usr/bin/python3
"""Base Class For Almost A Circle"""


import json
import os


class Base:
    """initializes class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """function 1"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function 2"""

        if list_dictionaries is None:
            return("[]")
        if len(list_dictionaries) == 0:
            return("[]")
        return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """function 3"""

        my_list = []
        if list_objs is not None:
            for i in list_objs:
                my_list.append(i.to_dictionary())

        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """function 4"""

        if json_string is None:
            return([])
        if len(json_string) is 0:
            return([])

        return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """function 5"""
        if cls.__name__ == "Square":
            bob = cls(1)
        elif cls.__name__ == "Rectangle":
            bob = cls(1, 1)

        bob.update(**dictionary)
        return(bob)

    @classmethod
    def load_from_file(cls):
        """function 6"""

        if not os.path.exists(cls.__name__ + ".json"):
            return([])
        with open(cls.__name__ + ".json", "r") as file:
            my_list = cls.from_json_string(file.read())
        for i in range(len(my_list)):
            my_list[i] = cls.create(**my_list[i])
        return(my_list)

    @classmethod
    def clear(cls):
        """function 7"""
        Base.__nb_objects = 0
