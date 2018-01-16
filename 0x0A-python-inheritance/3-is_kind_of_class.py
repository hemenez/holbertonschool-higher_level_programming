#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """Method returns True if object is an instance of a class,
    else returns False
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
