#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the workbook function below.
def workbook(n, k, arr):
    from itertools import count, zip_longest
    page = count(1)
    # spec = 0
    # for num_probs_chpt in arr:
    #     for probs in zip_longest(*[iter(range(1, num_probs_chpt + 1))] * k):
    #         if next(page) in probs:
    #             spec += 1
    # return spec
    return sum([sum([next(page) in probs for probs in zip_longest(*[iter(range(1, num_probs_chpt + 1))] * k)]) for
                num_probs_chpt in arr])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
