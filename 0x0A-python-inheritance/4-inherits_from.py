#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Method returs True if object is a subclass of a_class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
