#!/usr/bin/python3
class Rectangle:
    """A class defining a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes the size of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Method retrieves width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method sets value of width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Method retrieves height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Method sets value of height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """Method returns area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Method returns rectangle perimeter
        """
        value = 0
        if self.width == 0 or self.height == 0:
            return value
        else:
            value = (self.width * 2) + (self.height * 2)
            return value
