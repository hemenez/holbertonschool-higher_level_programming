#!/usr/bin/python3


class Base:
    """class Base
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """Method initializes values for class Base
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
