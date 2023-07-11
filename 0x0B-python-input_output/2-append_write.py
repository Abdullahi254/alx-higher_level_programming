#!/usr/bin/python3
"""
appends string to text file
"""


def append_write(filename="", text=""):
    """appends text to file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
