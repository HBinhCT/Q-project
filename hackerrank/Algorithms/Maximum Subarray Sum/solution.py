#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maximumSum function below.
def maximumSum(a, m):
    import bisect
    max_sum, prefix = 0, 0
    calculate_prefix = []
    for i in a:
        prefix = (prefix + i) % m
        max_sum = max(max_sum, prefix)
        cur_prefix = bisect.bisect_left(calculate_prefix, prefix + 1)
        if cur_prefix < len(calculate_prefix):
            max_sum = max(max_sum, prefix - calculate_prefix[cur_prefix] + m)
        calculate_prefix.insert(cur_prefix, prefix)
    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
