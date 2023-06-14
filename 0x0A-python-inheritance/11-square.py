#!/usr/bin/python3
"""a Geometry class with subclass Rectangle"""


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


"""a class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """the rectangle representation class"""
    def __init__(self, width, height):
        """initialize the rectangle class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    """public instance method that calculates area of rectangle"""
    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """returns the rectangle description"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """the rectangle representation class"""
    def __init__(self, size):
        """initialize the rectangle class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """returns the rectangle description"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

    """public instance method that calculates area of a Square"""
    def area(self):
        return self.__size ** 2
