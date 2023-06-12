#!/usr/bin/python3
"""class my list"""


class MyList(list):
    """class of mylist"""

    def print_sorted(self):
        """function to print list as sorted"""

        sorted_list = sorted(self)

        print(sorted_list)

    def append(self, item):
        super().append(item)
