#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the cipher function below.
def cipher(k, s):
    encoded = [int(c) for c in s]
    ln = len(s) - k + 1  # len(s) = n + k -1
    ans = encoded[:ln]
    for i in range(1, ln):
        ans[i] ^= encoded[i - 1]
        if i >= k:
            ans[i] ^= ans[i - k]
    return ''.join(map(str, ans))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = cipher(k, s)

    fptr.write(result + '\n')

    fptr.close()
