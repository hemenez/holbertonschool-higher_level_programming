#!/usr/bin/python3
class Rectangle:
    """A class defining a rectangle
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """Method returns area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Method returns rectangle perimeter
        """
        value = 0
        if self.width == 0 or self.height == 0:
            return value
        else:
            value = (self.width * 2) + (self.height * 2)
            return value

    def __str__(self):
        """Method prints rectangle with character '#'
        """
        new_line_counter = 0
        rectangle_string = ""
        if self.width == 0 or self.height == 0:
            return str(rectangle_string)
        for i in range(self.height):
            for j in range(self.width):
                rectangle_string = rectangle_string + '#'
            new_line_counter = new_line_counter + 1
            if new_line_counter < self.height:
                rectangle_string = rectangle_string + '\n'
        return str(rectangle_string)

    def __repr__(self):
        """Method prints object's information
        """
        return 'Rectangle(%s, %s)' %  (self.width, self.height)

    def __del__(self):
        """Method is called when object is deleted
        """
        print('Bye rectangle...')
