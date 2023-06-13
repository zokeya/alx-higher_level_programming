#!/usr/bin/python3
"""Mylist class that inherists from list"""

class Mylist(list):
    """initialize the obj"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
