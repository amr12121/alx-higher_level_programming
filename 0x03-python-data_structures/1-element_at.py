#!/usr/bin/python3
if __name__ == "__main__":
    def element_at(my_list, idx):
        if idx < 0:
            return 'None'
        elif idx is not in range(my_list):
            return' None'
        else:
            print(my_list[idx])
