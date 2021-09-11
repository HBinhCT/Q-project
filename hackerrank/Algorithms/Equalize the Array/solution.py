#!/bin/python3

import os


# Complete the equalizeArray function below.
def equalizeArray(arr):
    from collections import Counter
    return len(arr) - max(Counter(arr).values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
