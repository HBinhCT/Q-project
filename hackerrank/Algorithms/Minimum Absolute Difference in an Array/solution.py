#!/bin/python3

import os


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    if len(arr) != len(set(arr)):
        return 0
    arr.sort()
    return min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
