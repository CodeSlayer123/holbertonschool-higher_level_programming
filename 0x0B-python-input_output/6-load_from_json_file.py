#!/usr/bin/python3
"""Task 6 from json file"""

import json


def load_from_json_file(filename):
    """Task 6 from json file"""

    with open(filename, "r") as file:
        return(json.loads(file.read()))
