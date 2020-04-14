#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    changed = [False] * n
    lives = k
    pa = list(s)
    for i in range(n // 2):
        if pa[i] != pa[n - 1 - i]:
            changed[i] = True
            lives -= 1
            pa[i] = pa[n - 1 - i] = max([pa[i], pa[n - 1 - i]])
        if lives < 0:
            return '-1'
    j = 0
    while lives > 0 and j < n // 2:
        if pa[j] != 9:
            lives += int(changed[j])
            if lives >= 2:
                pa[j] = pa[n - 1 - j] = '9'
                lives -= 2
        j += 1
    if n % 2 == 1 and lives > 0:
        pa[n // 2 + 1] = '9'
    return ''.join(map(str, pa))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
