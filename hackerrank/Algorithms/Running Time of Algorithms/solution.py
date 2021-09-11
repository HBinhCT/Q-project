#!/bin/python3

import os


# Complete the runningTime function below.
def runningTime(arr):
    total = 0
    for i in range(1, len(arr)):
        j = i
        key = arr[i]
        del arr[i]
        while j and key < arr[j - 1]:
            j -= 1
        arr.insert(j, key)
        total += i - j
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
