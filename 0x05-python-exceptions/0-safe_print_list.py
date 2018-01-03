#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    if my_list is None:
        return count
    else:
        for i in my_list:
            try:
                if i < x + 1:
                    print('{}'.format(i), end="")
                    count = count + 1
            except:
                pass
        print()
        return count
