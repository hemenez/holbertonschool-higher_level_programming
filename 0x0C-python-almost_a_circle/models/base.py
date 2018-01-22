#!/usr/bin/python3
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method returns JSON string representation of
        list_dictionaries attribute
        """
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method writes JSON string representation of a list
        of objects to a file
        """
        new_dict = {}
        final_list = []
        final_dict = {}
        if list_objs is None:
            final_list = []
        else:
            for instance in list_objs:
                new_dict = instance.__dict__
                final_dict = {}
                for key in new_dict:
                    if "y" in key:
                        final_dict["y"] = new_dict[key]
                    if "x" in key:
                        final_dict["x"] = new_dict[key]
                    if "id" in key:
                        final_dict["id"] = new_dict[key]
                    if "width" in key:
                        final_dict["width"] = new_dict[key]
                    if "height" in key:
                        final_dict["height"] = new_dict[key]
                final_list.append(final_dict)
        with open(cls.__name__ + ".json", 'w+', encoding="UTF-8") as f:
            f.write(Base.to_json_string(final_list))

    @staticmethod
    def from_json_string(json_string):
        """Method returns the list of a JSON string represtnation of
        the given object, json_string
        """
        my_list = []
        if json_string is None or json_string == "[]":
            return my_list
        my_list = json.loads(json_string)
        return my_list
