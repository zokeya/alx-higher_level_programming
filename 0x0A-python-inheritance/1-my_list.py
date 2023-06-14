#!/usr/bin/python3
"""Mylist class that inherists from list"""


class MyList(list):
    """define a subclass of the list"""
    def __init__(self):
        """initialize the object"""
        super().__init__()

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
