#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    newnum = number * -1
    newnum = newnum % 10
    newnum = -newnum
else:
    newnum = number % 10
if newnum > 5:
    print('Last digit of', '{:d}'.format(number), 'is', '{:d}'.format(newnum),
          'and is greater than 5')
elif newnum == 0:
    print('Last digit of', '{:d}'.format(number), 'is', '{:d}'.format(newnum),
          'and is 0')
else:
    print('Last digit of', '{:d}'.format(number), 'is', '{:d}'.format(newnum),
          'and is less than 6 and not 0')
