#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    new_list = set(my_list)
    for el in new_list:
        result += int(el)
    return result
