#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return(s.title())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input('Write your input here : ')
    result = solve(s)
    fptr.write(result + '\n')

    fptr.close()

