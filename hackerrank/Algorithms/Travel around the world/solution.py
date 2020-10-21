#!/bin/python3

import os
import sys


#
# Complete the travelAroundTheWorld function below.
#
def travelAroundTheWorld(a, b, c):
    #
    # Write your code here.
    #
    n = len(a)
    diff = [a[i] - b[i] for i in range(n)]
    count = 0
    for i in range(n, 0, -1):
        diff[i % n] = min(diff[i % n], diff[i % n] + diff[(i + 1) % n])
        count += (diff[i % n] >= 0)
        if a[i % n] - diff[i % n] > c:
            count = 0
            break
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nc = input().split()

    n = int(nc[0])

    c = int(nc[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = travelAroundTheWorld(a, b, c)

    fptr.write(str(result) + '\n')

    fptr.close()
