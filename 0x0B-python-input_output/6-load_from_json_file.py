#!/usr/bin/python3
"""
define a function that loads json
"""
import json


def def load_from_json_file(filename):
    """loads json from file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
