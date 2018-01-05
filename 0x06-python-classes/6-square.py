#!/usr/bin/python3
class Square:
    """A class that defines the size and position of a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves value to compose square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value of square to size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves value of position that square should be printed at"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets value of position that square should be printed at
        to position"""
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """Finds area of square"""
        return self.size ** 2

    def my_print(self):
        """Prints square represented by hashtags for size, and spaces/newline
        for position"""
        if self.size == 0:
            print()
        else:
            if self.position[1] == 0:
                pass
            else:
                print('\n' * self.position[1], end="")
            for i in range(self.size):
                print(' ' * self.position[0], end="")
                for j in range(self.size):
                    print('#', end="")
                print()
