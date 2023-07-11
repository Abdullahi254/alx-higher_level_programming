#!/usr/bin/python3
# 0-read_file.py

"""Defines read_file()"""

def read_file(filename=""):
    """prints out file content"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
