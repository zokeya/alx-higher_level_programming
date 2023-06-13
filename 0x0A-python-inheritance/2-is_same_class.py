#!/usr/bin/python3
"""a function that implements if is same class"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an 
    instance of the specified class"""
    return (type(obj) == a_class)
