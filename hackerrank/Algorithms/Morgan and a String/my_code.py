#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the morganAndString function below.
def morganAndString(a, b):
    def morgan(c, d):
        c += 'z'
        d += 'z'
        for _ in range(len(c) + len(d) - 2):
            if c < d:
                yield c[0]
                c = c[1:]
            else:
                yield d[0]
                d = d[1:]

    return ''.join(morgan(a, b))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()
