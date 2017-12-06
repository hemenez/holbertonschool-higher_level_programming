#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0 and number < 10:
        newnum = number
    elif number > 9:
        newnum = number % 10
    else:
        newnum = number * -1
        newnum = newnum % 10
    newnum = int(newnum)
    print(newnum, end="")
    return newnum
