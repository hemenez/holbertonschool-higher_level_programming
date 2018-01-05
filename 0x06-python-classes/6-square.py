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
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) < 1 or len(value) > 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            if self.position[1] == 0:
                pass
            else:
                print('' * self.position[1])
            for i in range(self.size):
                print(' ' * self.position[0], end="")
                for j in range(self.size):
                    print('#', end="")
                print()
