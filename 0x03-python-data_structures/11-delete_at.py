#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    elif idx == 0:
        del my_list[0]
    else:
        for i in my_list:
            if i == idx:
                del my_list[i]
            else:
                pass
    return my_list
