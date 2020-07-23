#!/bin/python3

import os
import sys


#
# Complete the beadOrnaments function below.
#
def beadOrnaments(b):
    #
    # Write your code here.
    #
    from functools import reduce
    from operator import mul
    return int((reduce(mul, map(lambda x: x ** (x - 1), b), 1) * (sum(b) ** (len(b) - 2))) % 1000000007)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        b_count = int(input())

        b = list(map(int, input().rstrip().split()))

        result = beadOrnaments(b)

        fptr.write(str(result) + '\n')

    fptr.close()
