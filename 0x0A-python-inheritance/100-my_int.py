#!/usr/bin/python3
"""the class MyInt"""


class MyInt(int):
    """rebel version of an integer"""
    def __new__(cls, *args, **kwargs):
        """instantiate the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """invert != to =="""
        return int(self) != other

    def __ne__(self, other):
        """invert == to !="""
        return int(self) == other
