#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    res = []
    for i in range(p, q + 1):
        s = str(i ** 2)
        d = len(s) // 2
        if int('0' + s[:d]) + int(s[d:]) == i:
            res.append(i)
    if res:
        print(*res)
    else:
        print('INVALID RANGE')


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
