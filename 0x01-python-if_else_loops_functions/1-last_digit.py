#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# stupid workaround but its working
sign = 0 if number == 0 else (number / abs(number))
last_digit = abs(number) % 10 * sign
str = f"Last digit of {number:.0f} is {last_digit:.0f} "
if last_digit > 5:
    str += "and is greater than 5"
elif last_digit == 0:
    str += "and is 0"
else:
    str += "and is less than 6 and not 0"
print(str)
