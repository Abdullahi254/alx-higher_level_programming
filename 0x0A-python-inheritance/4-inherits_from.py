#!/usr/bin/python3
# 4-inherits_from.py

"""Defines a class and inherited class-checking function."""

def inherits_from(obj, a_class):
    """
    Check if an object is an instance or inherited instance of a class directly or indurectly
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True if the object is an instance of a class that inherited (directly or indirectly)
        from the specified class ; otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
