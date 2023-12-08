#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []

    for nbr in my_list:

        if nbr != search:
            new_list.append(nbr)
        else:
            new_list.append(replace)

    return new_list
