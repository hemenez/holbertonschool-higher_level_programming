#!/usr/bin/python3
import json


def from_json_string(my_str):
    """Method returns an object represented by a JSON string
    """
    return json.loads(my_str)
