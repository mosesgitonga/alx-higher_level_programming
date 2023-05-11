#!/usr/bin/python3

if __name__ == "__main__":
	import sys
	arg = len(sys.argv) - 1
	if arg < 1:
		print("{} argument.".format(arg))
	else:
		print("{} arguments:".format(arg))

	for index, arg in enumerate(sys.argv[1:], 1):
		print("{:d}: {}".format(index, arg))
