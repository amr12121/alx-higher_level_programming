#!/usr/bin/python
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return 'None'
    else:
        print(my_list[idx])
