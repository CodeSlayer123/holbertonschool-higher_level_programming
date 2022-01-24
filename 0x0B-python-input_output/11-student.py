#!/usr/bin/python3
"""class that defines a student by first and last name, age"""


class Student:
    """class that defines a student by first and last name, age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dict = {}
        if type(attrs) is list:
            for i in range(len(attrs)):
                if type(attrs[i]) is not str:
                    return(vars(self))

                if hasattr(self, attrs[i]):
                    new_dict.update({attrs[i]: getattr(self, attrs[i])})
        else:
            return(vars(self))

        return(new_dict)

    def reload_from_json(self, json):
        self.__dict__.update(json)
