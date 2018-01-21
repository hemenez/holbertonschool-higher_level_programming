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

    def __str__(self):
        """Method returns string representation of object
        """
        str1 = '[Square] ' + '(' + str(self.id) + ') ' + str(self.x) + '/'
        str2 = str(self.y) + str(' - ')
        str3 = str(self.width) + '/' + str(self.height)
        return str1 + str2 + str3
