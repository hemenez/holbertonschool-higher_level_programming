#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for i, x in sorted(my_dict.items()):
        print('{}: {}'.format(i, x))
