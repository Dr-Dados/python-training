#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for key,el in enumerate(new_list):
        if (el == search):
            new_list[key]=replace
    return new_list
