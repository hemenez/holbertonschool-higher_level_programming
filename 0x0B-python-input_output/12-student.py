#!/usr/bin/python3
class Student():
    """Student class
    """

    def __init__(self, first_name, last_name, age):
        """Instantiation of values
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method returns dictionary description with simple data
        structure (list, dictionary, string, integer and boolean)
        for JSON serialization of an object.
        """
        attr_dict = {}
        if type(attrs) is list and len(attrs) == 0:
            return attr_dict
        if type(attrs) is list:
            for index in attrs:
                if type(index) is not str:
                    return self.__dict__
                for x in self.__dict__:
                    if x == index:
                        attr_dict[index] = self.__dict__[index]
            return attr_dict
        return self.__dict__
