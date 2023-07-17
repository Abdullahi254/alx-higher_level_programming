#!/usr/bin/python3
"""
writes string to text file
"""


def write_file(filename="", text=""):
    """writes text to file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
