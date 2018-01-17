#!/usr/bin/python3
class BaseGeometry:
    """Class Base Geometry
    """
    def area(self):
        """Method raises exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Method validates value
        """
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError(str(self.name) + " must be an integer")
        if value <= 0:
            raise ValueError(str(self.value) + " must be greater than 0")

class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry parent class
    """
    def __init__(self, width, height):
        """Method handles instantiation
        """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
