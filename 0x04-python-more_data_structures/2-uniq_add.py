#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return None
    else:
        final = 0
        my_list = set(my_list)
        for num in sorted(my_list):
            final += num
        return final
