#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    if key not in my_dict:
        pass
    else:
        del my_dict[key]
    return my_dict
