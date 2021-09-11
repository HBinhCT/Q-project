#!/bin/python3

import os


# Complete the equal function below.
def equal(arr):
    low = min(arr)
    res = float('inf')
    for base in range(0, 3):
        current_sum = 0
        for i in range(len(arr)):
            diff = arr[i] - low + base
            current_sum += diff // 5 + diff % 5 // 2 + diff % 5 % 2  # // 1
        res = min(current_sum, res)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
