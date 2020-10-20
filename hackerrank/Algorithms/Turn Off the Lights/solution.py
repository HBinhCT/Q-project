#!/bin/python3

import os
import sys


#
# Complete the turnOffTheLights function below.
#
def turnOffTheLights(k, c):
    #
    # Write your code here.
    #
    ans = float('inf')
    n = len(c)
    for i in range(min(n - 1, k) + 1):
        remaining = (n - 1 - k - i) % (2 * k + 1)
        if remaining > k or remaining <= 0:
            current = 0
            for j in range(i, n, 2 * k + 1):
                current += c[j]
            ans = min(ans, current)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = turnOffTheLights(k, c)

    fptr.write(str(result) + '\n')

    fptr.close()
