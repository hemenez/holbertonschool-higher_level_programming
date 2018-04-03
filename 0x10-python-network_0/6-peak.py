#!/usr/bin/python3
def find_peak(list_of_integers):
    """ Fxn finds peak in list of integers """
    if list_of_integers is not None:
#        num = list_of_integers
#        for idx in range(1, len(num)):
#            if num[idx] > num[idx + 1] and num[idx] > num[idx - 1]:
#                return num[idx]
#        else:
        return max(list_of_integers)
