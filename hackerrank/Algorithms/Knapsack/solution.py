#!/bin/python3

import os


# Complete the unboundedKnapsack function below.
def unboundedKnapsack(k, arr):
    if len(arr) == 0 or k == 0:
        return 0
    if k < min(arr):
        return 0
    for i in arr:
        if k % i == 0:
            return k
    # None of our micro optimizations worked out, time to use dynamic programming
    cache = [0] * (k + 1)
    ans = 0
    for i in range(1, k + 1):
        for j in arr:
            # we have a coin for this value!!
            if i - j == 0 or i - j > 0 and cache[i - j] == 1:
                cache[i] = 1
                ans = i
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for _ in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()
