#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the toys function below.
def toys(w):
    w.sort()
    containers = 1  # since there has to at least one container by default
    a = min(w)
    i = 0
    while w:
        if a <= w[i] <= a + 4:
            w.remove(w[i])
        else:
            containers += 1
            a = min(w)
    return containers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
