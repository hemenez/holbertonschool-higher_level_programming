#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """Method reads n # of lines of a text file
    """
    with open(filename, encoding="UTF-8") as my_file:
        if nb_lines <= 0:
            print(my_file.read(), end="")
        counter = 0
        while True:
            read_file = my_file.readline()
            if not read_file:
                break
            counter += 1
        if counter <= nb_lines:
            print(my_file.read(), end="")
    with open(filename, encoding="UTF-8") as my_file:
            line_num = 0
            for a_line in my_file:
                if line_num < nb_lines:
                    print(a_line, end="")
                line_num += 1
