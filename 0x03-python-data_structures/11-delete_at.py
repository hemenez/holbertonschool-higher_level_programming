#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or not idx:
        return my_list
    else:
        for i in my_list:
            if i == idx:
                del my_list[i]
            elif idx < i:
                return my_list
            else:
                pass
    return my_list
