#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """Method creates an object from a JSON file
    """
    with open(filename, "r", encoding="UTF-8") as my_file:
        obj_file = json.load(my_file)
        return obj_file
#        read_line = my_file.read()
#        file_object = json.dumps(read_line)
#        return file_object
#        read_line = my_file.readline()
#        return json.dumps(read_line)
