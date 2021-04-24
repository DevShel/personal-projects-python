import sys
import math
import string
# Practice Scenario: Given an array with n distinct elements, convert the given array to a form where all elements are in range from 0 to n-1. The order of elements is same, i.e., 0 is placed in place of smallest element, 1 is placed for second smallest element, … n-1 is placed for largest element

array = [135,1,22,11,4,53]

def sortNumbers(array):
    i = 0
    for i in range(len(array)-1):
        for i in range(len(array)-1):
            if ((array[i])>(array[i+1])):
                temp1 = array[i]
                temp2 = array[i+1]
                array[i] = temp2
                array[i+1] = temp1
            i=i+1
    print(array)
            

sortNumbers(array)
    
