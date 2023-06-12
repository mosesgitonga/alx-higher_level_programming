#!/usr/bin/python3
"""Module defining the MyList class"""


class MyList(list):
    """A custom list class that provides additional functionality"""

    def print_sorted(self):
        """Prints the list in sorted (ascending) order"""

        sorted_list = sorted(self)
        print(sorted_list)

    def append(self, item):
        """
        Appends an item to the list.

        Args:
            item: The item to be appended to the list.
        """

        super().append(item)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
