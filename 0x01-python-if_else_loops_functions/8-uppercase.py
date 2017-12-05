def uppercase(str):
    for i in str:
        if ord(i) < 97 or ord(i) > 122:
            x = ord(i)
        else:
            x = ord(i) - 32
        print(chr(x), end="")
    print('\n', end="")
