#!/usr/bin/python3
"""a Geometry class that raises an Exception"""


class BaseGeometry:
    """initialize the class"""
    def __init__(self):
        pass

    """public instance method that raises an exception"""
    def area(self):
        raise Exception("area() is not implemented")

    """public instance methot that validates value
    as an integer greater than 0"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
