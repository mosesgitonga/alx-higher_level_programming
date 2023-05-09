#!/usr/bin/python3

for i in range(0, 99):
	if i < 10:
		print(f"{i} = 0x0{i:x}")
	elif i >= 10 and i <= 15:
		print(f"{i} = 0x{i:x}")
	else:
		print(f"{i} = 0x{i:x}")
