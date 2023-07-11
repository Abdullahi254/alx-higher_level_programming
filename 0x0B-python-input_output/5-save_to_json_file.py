#!/usr/bin/python3
"""
define save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """writes object to a textfile using json format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
