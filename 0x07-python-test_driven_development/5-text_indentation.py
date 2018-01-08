#!/usr/bin/python3
def text_indentation(text):
    """Module will print text following certain conditions
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    if text != "":
        for i in range(len(text)):
            if i == 0:
                print(text[i], end="")
                if text[i] == ':' or text[i] == '?' or text[i] == '.':
                    print('\n')
                    continue
                elif text[i] == ' ':
                    continue
            elif text[i] == ':' or text[i] == '?' or text[i] == '.':
                if i != 0:
                    print(text[i], end="")
                    print('\n')
                continue
            elif (text[i - 1] == ':' or
                  text[i - 1] == '?' or
                  text[i - 1] == '.'):
                if text[i] == ' ':
                    continue
                else:
                    print(text[i], end="")
            elif text[i - 1] == '\n':
                if text[i] == ' ':
                    continue
            elif text[i - 1] == ' ' and text[i] == ' ':
                continue
            else:
                print(text[i], end="")
        if text[i] == '\n':
            print()
    else:
        print()
