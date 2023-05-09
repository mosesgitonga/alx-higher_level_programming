#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
if (ld > 5):
    if number < 0:
        number = number * -1
	ld = number % 10
	print(f"Last digit of -{number} is -{ld} and is less than 6 and not 0")
    else:
	print(f"Last digit of {number} is {ld} and is greater than 5")
elif (ld == 0):
    print(f"Last digit of {number} is 0 and is 0")
else:
    if number < 0:
        number = number * -1
        ld = number % 10
	print(f"Last digit of -{number} is -{ld} and is less than 6 and not 0")
    else:
	print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
