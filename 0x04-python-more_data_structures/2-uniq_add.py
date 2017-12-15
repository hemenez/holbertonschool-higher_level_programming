#!/usr/bin/python3
def uniq_add(my_list=[]):
    final = 0
    my_list = set(my_list)
    for num in sorted(my_list):
        final += num
    return final
