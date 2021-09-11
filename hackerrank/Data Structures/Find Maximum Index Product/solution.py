#!/bin/python3

import os


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def solve(arr):
    # Write your code here
    ln = len(arr)
    right = ln - 1
    for i in range(ln - 2, 0, -1):
        if arr[i] <= arr[i - 1] and arr[i] < arr[i + 1]:
            right = i
            break
    left = right - 1
    while left >= 0 and arr[left] <= arr[right]:
        left -= 1
    return (left + 1) * (right + 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
