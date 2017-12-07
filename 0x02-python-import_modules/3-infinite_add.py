#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    index = 0
    total = 0
    for count in sys.argv:
        if index > 0:
            sys.argv[index] = int(sys.argv[index])
            total = sys.argv[index] + total
            index = index + 1
        else:
            index = index + 1
    print('{:d}'.format(total))
