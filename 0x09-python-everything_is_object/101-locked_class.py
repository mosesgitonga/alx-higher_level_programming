#!/usr/bin/python3

class LockedClass:
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        x = "'LockedClass' object has no attribute '{}'".format(name)
        if name != 'first_name':
            raise AttributeError(x)
        super().__setattr__(name, value)
