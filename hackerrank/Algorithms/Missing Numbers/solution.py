#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    from collections import Counter
    return sorted((Counter(brr) - Counter(arr)).keys())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
