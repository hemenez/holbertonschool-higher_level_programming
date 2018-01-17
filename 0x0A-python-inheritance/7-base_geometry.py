#!/usr/bin/python3
class BaseGeometry:
    """Class Base Geometry
    """
    def area(self):
        """Method raises exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Method validates value
        """
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError(str(self.name) + " must be an integer")
        if value <= 0:
            raise ValueError(str(self.name) + " must be greater than 0")
