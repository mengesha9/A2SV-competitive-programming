#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    numSwaps = 0
    # firstElement=0
    # lastElement=0
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1] :
                (a[j],a[j+1]) =(a[j+1] , a[j])
                numSwaps +=1
            firstElement = a[0]
            lastElement= a[len(a)-1]
    print("Array is sorted in " + str(numSwaps)+" swaps.")
    print("First Element: " + str(firstElement))
    print("Last Element: " + str(lastElement))
        
                
                

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
