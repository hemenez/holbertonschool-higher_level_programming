#!/usr/bin/python3
def append_write(filename="", text=""):
    """Method appends a string to the end of a text file
    """
    with open(filename, "a+", encoding="UTF-8") as my_file:
        my_file.write(text)
        return len(text)
