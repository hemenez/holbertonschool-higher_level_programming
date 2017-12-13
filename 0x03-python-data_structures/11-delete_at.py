#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list or idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        for i in my_list:
            if i == idx:
                del my_list[i]
            else:
                pass
    return my_list
