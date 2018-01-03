#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    length = 0
    for hi in my_list:
        length = length + 1
    if my_list is None:
        return count
    else:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count = count + 1
            except (ValueError, TypeError):
                pass
        print()
        return count
