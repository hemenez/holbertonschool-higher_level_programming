#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print('{:d} argument'.format(len(sys.argv) - 1), end="")
    count = len(sys.argv) - 1
    if count == 0:
        print('s.')
    elif count == 1:
        print(':')
    else:
        print('s:')
    index = 0
    for count in sys.argv:
        if index > 0:
            print('{:d}: {}'.format(index, sys.argv[index]))
        index = index + 1
