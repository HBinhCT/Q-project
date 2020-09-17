#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    i = 2
    while i < n:
        t1, t2 = t2, t1 + t2 * t2
        i += 1
    return t2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
