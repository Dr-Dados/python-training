#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for i, x in sorted(a_dictionary.items()):
        print("{} : {}".format(i,x))
