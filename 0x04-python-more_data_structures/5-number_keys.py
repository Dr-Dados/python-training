#!/usr/bin/python3

def number_keys(a_dictionary):
    number = 0
    for key,value in a_dictionary.items():
        if key is not None:
            number +=1
    return number
