#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print('Last digit of', '{:d}'.format(number), 'is ', end="")
if number > 0:
    newnum = number % 10
elif number < 0:
    newnum = number * -1
    newnum = newnum % 10
    newnum = -newnum
else:
    newnum = number
newnum = int(newnum)
print(newnum, '', end="")
if newnum > 5:
    print('and is greater than 5')
elif newnum == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')
