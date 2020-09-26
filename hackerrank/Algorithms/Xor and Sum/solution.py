#!/bin/python3

import os
import sys


#
# Complete the xorAndSum function below.
#
def xorAndSum(a, b):
    #
    # Write your code here.
    #
    a, b = int(a, 2), int(b, 2)
    return sum(a ^ (b << i) for i in range(314160)) % 1000000007


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    result = xorAndSum(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()
