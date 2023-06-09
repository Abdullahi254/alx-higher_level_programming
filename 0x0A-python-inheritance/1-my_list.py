#!/usr/bin/python3
# 1-my_list.py

"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        for i in sorted(self):
            print(i)

