#!/usr/bin/python3
"""Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """inherits from Base
    """

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
        print('\n' * self.y, end="")
        for first in range(self.height):
            print(' ' * self.x, end="")
            for second in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        """Method returns string representation of object
        """
        str1 = '[Rectangle] ' + '(' + str(self.id) + ') ' + str(self.x) + '/'
        str2 = str(self.y) + str(' - ')
        str3 = str(self.width) + '/' + str(self.height)
        return str1 + str2 + str3

    def update(self, *args, **kwargs):
        """Method assigns new argument to each attribute
        """
        if len(args) == 1:
            self.id = args[0]
        if len(args) == 2:
            self.id = args[0]
            self.width = args[1]
        if len(args) == 3:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
        if len(args) == 4:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
        if len(args) == 5:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Method returns dictionary representation of a Rectangle
        """
        rect_dict = {}
        rect_dict['id'] = self.id
        rect_dict['x'] = self.x
        rect_dict['y'] = self.y
        rect_dict['width'] = self.width
        rect_dict['height'] = self.height
        return rect_dict
