#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Module will print a name following a string"""
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is ', end="")
    for i in range(len(first_name)):
        if first_name[i] == ' ':
            continue
        else:
            print(first_name[i], end="")
    print(' ', end="")
    for j in range(len(last_name)):
        if last_name[j] == ' ':
            continue
        else:
            print(last_name[j], end="")
    print()
#    print('{} {}'.format(first_name, last_name))
