#!/bin/python3

import os


# Complete the quickSort function below.
def quickSort(arr):
    left = []
    right = []
    equal = []
    p = arr[0]

    for i in arr:
        if i > p:
            right.append(i)
        elif i < p:
            left.append(i)
        else:
            equal.append(i)

    return left + equal + right


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
