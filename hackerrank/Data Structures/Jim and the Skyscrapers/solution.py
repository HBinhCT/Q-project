#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def solve(arr):
    # Write your code here
    from collections import deque

    queue = deque([])
    res = 0
    for i in arr:
        while queue and queue[-1][0] < i:
            _, count = queue.pop()
            res += count * (count - 1)
        if queue and queue[-1][0] == i:
            queue[-1][1] += 1
        else:
            queue.append([i, 1])
    while queue:
        _, count = queue.pop()
        res += count * (count - 1)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
