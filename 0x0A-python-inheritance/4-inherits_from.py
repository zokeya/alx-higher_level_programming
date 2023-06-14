#!/usr/bin/python3
"""a funtion to check if object is an instance of inherited class"""


def inherits_from(obj, a_class):
    """is True if the object is an instance of inherited class else False"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
