import sys
import math
import string
# Given an array (or string), the task is to reverse the array/string.

string = [1,2,3,4]

def reverseArray(array):
    newArray = []
    i = 0
    length = len(array)
    for i in range(length):
        i = i+1
        newArray.append(array[len(array)-i])  
    print(newArray)

reverseArray(string)