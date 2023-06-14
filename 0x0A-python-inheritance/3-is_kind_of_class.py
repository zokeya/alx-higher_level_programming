#!/usr/bin/python3
"""a funtion to check if object is an instance of inherited class"""


def is_kind_of_class(obj, a_class):
    """is True if the object is an instance of inherited class else False"""
    return (isinstance(obj, a_class))
