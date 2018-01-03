#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    if my_list_1 is None or my_list_2 is None:
        return new_list
    else:
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
                new_list.append(result)
            except ZeroDivisionError:
                result = 0
                new_list.append(result)
                print('division by 0')
            except IndexError:
                result = 0
                new_list.append(result)
                print('out of range')
            except (TypeError, ValueError):
                result = 0
                new_list.append(result)
                print('wrong type')
        return new_list
