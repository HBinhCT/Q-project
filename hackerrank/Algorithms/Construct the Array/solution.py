#!/bin/python3

import os


# Complete the countArray function below.
def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    mod = 10 ** 9 + 7
    a = [0] * n
    b = [0] * n
    if x == 1:
        a[0] = 1
        b[0] = 0
    else:
        a[0] = 0
        b[0] = 1
    for i in range(1, n):
        a[i] = b[i - 1]
        b[i] = (a[i - 1] * (k - 1) + b[i - 1] * (k - 2)) % mod
    return a[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
