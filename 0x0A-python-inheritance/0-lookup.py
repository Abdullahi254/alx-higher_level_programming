#!/usr/bin/python3
# 0-lookup.py

"""Defines an object attribute lookup function."""

def lookup(obj):
    """iterates through the attributes and return a list of attributes."""
    return (dir(obj))
