#!/usr/bin/python3
def is_same_class(obj, a_class):
    """Function returns True if object is an instance of specified class,
    otherwise returns False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
