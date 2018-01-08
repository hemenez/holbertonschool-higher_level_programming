#!/usr/bin/python3
def add_integer(a, b):
    """Module will add two integers"""
    total = 0
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    total = a + b
    return total
