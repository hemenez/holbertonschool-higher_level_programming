#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print('Last digit of', '{:d}'.format(number), 'is ', end="")
x = number
if x < 0:
    x = -x
newnum = x % 10
if number < 0:
    newnum = -newnum
if newnum > 5:
    print('{:d}'.format(newnum), '', 'and is greater than 5')
elif newnum == 0:
    print('{:d}'.format(newnum), '', 'and is 0')
else:
    print('{:d}'.format(newnum), '', 'and is less than 6 and not 0')
