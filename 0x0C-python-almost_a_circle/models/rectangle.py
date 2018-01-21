#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method initializes values for rectangle class
        """
        super(Rectangle, self).__init__(id)

    @property
    def width(self):
        """Method calls value of width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method sets value of width attribute
        """
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
        self.__y = value
