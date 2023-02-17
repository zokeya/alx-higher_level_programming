#!/usr/bin/paytho3
"""Defines a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Representing a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle
        Args:
            with (int): WIdth of the Rectangle.
            height (int): Height of the Rectangle.
            x (int): X coordinate of the Rectangle.
            y (int): Y coordinate of the Rectangle.
            id (int): Identy of the Rectangle.
        Raises:
            TypeError: If width or height is not an int.
            ValueError: If width or height <= 0.
            TypeError: If x or y is not an int.
            ValueError: If x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set/get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("width must be greater than 0(zero)")
        self.__width = value

    @property
    def height(self):
        """set/get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be greater than 0(zero)")
        self.__height = value

    @property
    def x(self):
        """set/get the x coordinate of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be greater than 0(zero)")
        self.__x = value

    @property
    def y(self):
        """set/get the y coordinate of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be greater than 0(zero)")
        self.__y = value

