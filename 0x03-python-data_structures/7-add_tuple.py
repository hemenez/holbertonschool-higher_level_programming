#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)
    if not tuple_a:
        tuple_a = [0, 0]
    if not tuple_b:
        tuple_b = [0, 0]
    for i in tuple_a:
        if len(tuple_a) < 2:
            tuple_a.append(0)
        elif len(tuple_a) > 2:
            del tuple_a[i]
        else:
            pass
    for j in tuple_b:
        if len(tuple_b) < 2:
            tuple_b.append(0)
        elif len(tuple_b) > 2:
            del tuple_b[j]
        else:
            pass
    newnew = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    final = tuple(newnew)
    return final
