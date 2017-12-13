#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or not idx:
        return my_list
    for i in my_list:
        if i == idx:
            del my_list[i]
        else:
            pass
    return my_list
