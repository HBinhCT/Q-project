#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sherlockAndMinimax function below.
def sherlockAndMinimax(arr, p, q):
    arr.sort()
    if arr[0] > q:
        return p
    elif arr[-1] < p:
        return q
    else:
        ans = -1
        num = -1
        if arr[0] > p and ans < arr[0] - p:
            ans = arr[0] - p
            num = p
        if arr[-1] < q and ans < q - arr[-1]:
            ans = q - arr[-1]
            num = q
        for i in range(len(arr) - 1):
            cur = (arr[i] + arr[i + 1]) // 2
            if p <= cur <= q and cur - arr[i] > ans:
                ans = cur - arr[i]
                num = cur
            elif cur > q and q - arr[i] > ans:
                ans = q - arr[i]
                num = q
            elif cur < p and arr[i + 1] - p > ans:
                ans = arr[i + 1] - p
                num = p
        return num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    pq = input().split()

    p = int(pq[0])

    q = int(pq[1])

    result = sherlockAndMinimax(arr, p, q)

    fptr.write(str(result) + '\n')

    fptr.close()
