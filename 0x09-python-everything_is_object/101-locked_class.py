#!/usr/bin/python3
"""Locked Class module"""


class LockedClass:
    """class with only one attribute"""

    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        """this is  setatrrirbute"""

        x = "'LockedClass' object has no attribute '{}'".format(name)
        if name != 'first_name':
            raise AttributeError(x)
        super().__setattr__(name, value)
