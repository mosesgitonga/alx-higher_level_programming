#!/usr/bin/python3

import sys
arg = len(sys.argv) - 1
if arg <= 1:
	print("{} argument:".format(arg))
else:
	print("{} arguments:".format(arg))

for index, arg in enumerate(sys.argv[1:], 1):
	print("{}: {}".format(index, arg))
