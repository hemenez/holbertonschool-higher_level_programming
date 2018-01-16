#!/usr/bin/python3
class MyList(list):
    """Class that inherits from list
    """
    def print_sorted(self):
        """Method prints the list in sorted order
        """
        print(sorted(self))
