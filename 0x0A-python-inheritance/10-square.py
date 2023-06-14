#!/usr/bin/python3
"""a class Square  that inherits from Rectange (9-rectangle.py)"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """the rectangle representation class"""
    def __init__(self, size):
        """initialize the rectangle class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    """public instance method that calculates area of a Square"""
    def area(self):
        return self.__size * self.__size
