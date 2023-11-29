#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_Digit = number % 10
else:
    last_Digit = number % -10

print("Last digit of {:d} is {:d}".format(number, last_Digit), end="")

if last_Digit > 5:
    print(" and is greater than 5")
elif last_Digit < 0:
    print(" and is less than 6 and not 0")
else:
    print(" and is 0")
