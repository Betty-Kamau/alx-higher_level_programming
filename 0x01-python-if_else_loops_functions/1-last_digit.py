#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

num2 = number % 1000
num3 = num2 % 100
num4 = (num3 % 10)

if num4 > 5:
    print("Last digit of %d" %number + " is %d " %num4
          +"and is greater than 5")

elif num4 < 6 and num4 > 0:
    print("Last digit of %d" %number + " is %d " %num4
          + "and is less than 6 and not 0")

else:
    print("Last digit of %d" %number + " is %d " %num4 +
          "and is 0")
