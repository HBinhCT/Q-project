#!/bin/python3

import os


# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    sticks.sort()
    i = len(sticks) - 3
    while i >= 0:
        if sticks[i] + sticks[i + 1] > sticks[i + 2]:
            return sticks[i:i + 3]
        i -= 1
    else:
        return [-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
