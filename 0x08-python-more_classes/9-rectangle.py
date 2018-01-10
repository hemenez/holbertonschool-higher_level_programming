#!/usr/bin/python3
class Rectangle:
    """A class defining a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the size of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Method retrieves width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method sets value of width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Method retrieves height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Method sets value of height
        """
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
                rectangle_string = rectangle_string + str(self.print_symbol)
            new_line_counter = new_line_counter + 1
            if new_line_counter < self.height:
                rectangle_string = rectangle_string + '\n'
        return str(rectangle_string)

    def __repr__(self):
        """Method prints object's information
        """
        return 'Rectangle(%s, %s)' % (self.width, self.height)

    def __del__(self):
        """Method is called when object is deleted
        """
        print('Bye rectangle...')
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to return biggest rectangle based on its area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return rect_1
        if Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        if Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Method creates a new Rectangle instance with correct size
        """
        width = size
        height = size
        square = cls(width, height)
        return square
