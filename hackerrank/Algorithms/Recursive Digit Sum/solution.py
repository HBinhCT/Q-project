#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the superDigit function below.
def superDigit(n, k):
    x = int(n) * k % 9
    return x if x else 9


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
