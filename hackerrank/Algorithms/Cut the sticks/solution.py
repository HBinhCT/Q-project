#!/bin/python3

import os


# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    from collections import Counter
    ln = len(arr)
    c = Counter(arr)
    for k in sorted(c):
        yield ln
        ln -= c[k]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
