#!/usr/bin/python3
if __name__ == "__main__":
    def element_at(my_list, idx):
        if idx < 0 or idx > len(my_lis) - 1:
            return 'None'
        else:
            print(my_list[idx])
