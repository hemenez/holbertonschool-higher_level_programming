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

    def update(self, *args, **kwargs):
        """Method assigns new argument to each attribute
        """
        if len(args) == 1:
            self.id = args[0]
        if len(args) == 2:
            self.id = args[0]
            self.size = args[1]
        if len(args) == 3:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
        if len(args) == 4:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Method returns dictionary representation of a Square
        """
        sq_dict = {}
        sq_dict['id'] = self.id
        sq_dict['x'] = self.x
        sq_dict['y'] = self.y
        sq_dict['size'] = self.size
        return sq_dict
