#!/usr/bin/python3
def write_file(filename="", text=""):
    """Method writes a string to a text file and returns
    the number of characters written
    """
    with open(filename, mode="w", encoding="UTF-8") as my_file:
        my_file.write(text)
        return len(text)
