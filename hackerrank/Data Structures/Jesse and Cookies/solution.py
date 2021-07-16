#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    from heapq import heapify, heappop, heappush

    count = 0
    heapify(A)
    while A[0] < k and len(A) > 1:
        heappush(A, heappop(A) + 2 * heappop(A))
        count += 1
    return count if A[0] >= k else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
