#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    left = right = -1
    for i in range(len(w) - 1, 0, -1):
        for j in range(i - 1, left, -1):
            if w[j] < w[i]:
                left, right = j, i
                break
    return 'no answer' if left == -1 else w[:left] + w[right] + ''.join(sorted(w[left:right] + w[right + 1:]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
