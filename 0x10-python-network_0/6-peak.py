#!/usr/bin/python3
def find_peak(list_of_integers):
    my_list = list_of_integers
    for idx in range(1, len(my_list)):
        if my_list[idx] > my_list[idx + 1] and my_list[idx] > my_list[idx - 1]:
            return my_list[idx]
