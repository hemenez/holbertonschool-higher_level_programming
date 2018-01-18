#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """Method creates an object from a JSON file
    """
    with open(filename, "r", encoding="utf-8") as my_file:
        obj_file = json.load(my_file)
        return obj_file
