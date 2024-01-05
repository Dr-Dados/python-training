#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1
# YOUR CODE HERE
if(number < 0):
    sign = -1
    number = -number
lastDigit = number%10
if (lastDigit < 6 and lastDigit > 0):
    sentence = "is less than 6 and not 0"
elif (lastDigit > 5):
    sentence = "is greater than 5"
elif (lastDigit == 0):
    sentence = "is 0"
print("Last Digit of {} is {} and {}".format(number*sign,lastDigit,sentence))
