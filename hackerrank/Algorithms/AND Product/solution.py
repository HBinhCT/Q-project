#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the andProduct function below.
def andProduct(a, b):
    return a & ~((1 << math.floor(math.log(a ^ b, 2))) - 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = andProduct(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
