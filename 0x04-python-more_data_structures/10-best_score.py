#!/usr/bin/python3
def best_score(my_dict):
    if not my_dict:
        return None
    else:
        for value, key in sorted(my_dict.items()):
            value, key = key, value
            sorted(my_dict.items())
        return key
