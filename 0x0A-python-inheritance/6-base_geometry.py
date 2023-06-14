#!/usr/bin/python3
"""a Geometry class that raises an Exception"""


class BaseGeometry:
    """initialize the class"""
    def __init__(self):
        pass

    """public instance method that raises an exception"""
    def area(self):
        raise Exception("area() is not implemented")
