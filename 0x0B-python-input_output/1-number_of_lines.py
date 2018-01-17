#!/usr/bin/python3
def number_of_lines(filename=""):
    """Method returns number of lines of a text file
    """
    with open(filename, encoding="UTF-8") as my_file:
        counter = 0
        while True:
            read_file = my_file.readline()
            if not read_file:
                break
            counter += 1
    return counter
