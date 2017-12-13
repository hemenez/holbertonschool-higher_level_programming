#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = (0, 0)
    tuple_a1 = tuple_a + tuple_c
    tuple_b1 = tuple_b + tuple_c
    tuple_a2 = tuple_a1[:2]
    tuple_b2 = tuple_b1[:2]
    total = ((tuple_a2[0] + tuple_b2[0]), (tuple_a2[1] + tuple_b2[1]))
    return total
