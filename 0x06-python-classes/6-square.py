#!/usr/bin/python3
class Square:
    """A class that defines the size of a square with a private attribute
    making sure that size is of an integer value and greater than zero and
    returns the area size of the square. Retrieves value to set size of square.
    Class also has method of printing the square represented by a hashtag. The
    class also has a method of printing spaces given a certain position"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if not isinstance(value, tuple):
                raise TypeError
            if value[0] < 0 or value[1] < 0:
                raise TypeError
            if len(value) > 2:
                raise TypeError
            else:
                self.__position = value
        except TypeError:
            print('position must be a tuple of 2 positive integers')

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            if self.position[1] is not 0:
                print()
            for i in range(self.size):
                print(' ' * self.position[0], end="")
                for j in range(self.size):
                    print('#', end="")
                print()
