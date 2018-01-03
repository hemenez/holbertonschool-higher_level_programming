#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        quotient = a / b
        return quotient
    except ZeroDivisionError:
        quotient = None
        return None
    finally:
        print("Inside result: {}".format(quotient))
