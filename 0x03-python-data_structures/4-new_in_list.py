#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listcopy = my_list.copy()
    if idx < 0:
        return listcopy
    elif idx > len(listcopy) - 1:
        return listcopy
    else:
        listcopy[idx] = element
        return listcopy
