#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        pass
    else:
        new_string = list(my_string)
        x = new_string.count("C")
        y = new_string.count("c")
        if x != 0:
            xi = new_string.index("C")
            del new_string[xi]
            removedstr = new_string
        if y != 0:
            yi = new_string.index("c")
            del new_string[yi]
            removedstr = new_string
        renovated = ''.join(map(str, removedstr))
        return renovated
