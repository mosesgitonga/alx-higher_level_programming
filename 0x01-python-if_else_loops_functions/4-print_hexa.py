#!/usr/bin/python3

for i in range(0, 99):
	if i < 10:
		print("{} = 0x0{:x}".format(i, i))
	elif i >= 10 and i <= 15:
		print("{} = 0x{:x}".format(i, i))
	else:
		print("{} = 0x{:x}".format(i, i))
