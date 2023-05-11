#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg = len(sys.argv) - 1
    if arg == 0:
        print("{:d} argument.".format(arg))
    elif arg == 1:
        print("{:d} argument:".format(arg))
    else:
        print("{:d} arguments:".format(arg))

    for index, arg in enumerate(sys.argv[1:], 1):
        print("{:d}: {:s}".format(index, arg))
