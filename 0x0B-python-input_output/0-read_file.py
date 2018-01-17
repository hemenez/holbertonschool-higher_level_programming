#!/usr/bin/python3
def read_file(filename=""):
    """Method reads a text file and prints it
    """
    with open(filename, mode="r", encoding="UTF-8") as my_file:
        print(my_file.read(), end="")
