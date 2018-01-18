#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """Function writes an object to a text file, using JSON
    representation
    """
    with open(filename, "w+", encoding="UTF-8") as my_file:
        my_file.write(json.dumps(my_obj))
