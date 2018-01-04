#!/usr/bin/python3
class Square:
    """A class that defines the size of a square with a private attribute
    making sure that size is of an integer value and greater than zero and
    returns the area size of the square"""
    def __init__(self, __size=0):
        self.__size = __size
        try:
            if type(__size) is not int:
                raise TypeError
            if __size < 0:
                raise ValueError
        except TypeError:
            print('size must be an integer', end="")
            raise
        except ValueError:
            print('size must be >= 0', end="")
            raise

    def area(self):
        return int(self.__size) ** 2
