import sys
import math
import string
# Given a number, find sum of its digits.

digits = 237523

def sumOfDigits(number):
    digitsString = (str(number))
    digitsStringLength = len(str(number))
    numArray = []
    sum = 0

    while(digitsStringLength>0):
        digitsStringLength = digitsStringLength-1
        sum = sum + int(digitsString[digitsStringLength])
    print(sum)

sumOfDigits(digits)