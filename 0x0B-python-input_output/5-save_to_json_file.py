#!/usr/bin/python3
"""Task 5 to json file"""


import json


def save_to_json_file(my_obj, filename):
    """Task 5 to json file"""

    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
