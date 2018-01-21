#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method initializes values for rectangle class
        """
        super(Rectangle, self).__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Method calls value of width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method sets value of width attribute
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Method calls value of height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Method sets value of height attribute
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """Method calls value of x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Method sets value of x attribute
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """Method calls value of y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Method sets value of y attribute
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """Method returns area value of a Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """Method prints Rectangle instance with a hashtag character
        """
        for first in range(self.height):
            for second in range(self.width):
                print('#', end="")
            print()
