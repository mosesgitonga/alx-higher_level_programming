#!/usr/bin/python3

for i in range(0, 100):
	if i < 10:
		print(f"0{i}", end = ", ")
	else:
		if i == 99:
			print(f"{i}")
		else:
			print(i, end = ", ")
