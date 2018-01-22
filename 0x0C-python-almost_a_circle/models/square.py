#!/usr/bin/python

from models.base import Base
from models.rectangle import Rectangle

class Square(Rectangle):
    """Class square inherits from Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Method initializes values for Square class
        """
        super(Square, self).__init__(size, size, x, y, id)

    @property
    def size(self):
        """Method calls value of size
        """
        return self.width

    @size.setter
    def size(self, value):
        """Method sets value of size
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """Method returns string representation of object
        """
        str1 = '[Square] ' + '(' + str(self.id) + ') ' + str(self.x) + '/'
        str2 = str(self.y) + str(' - ') + str(self.width)
        return str1 + str2
