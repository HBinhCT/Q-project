#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    n = len(arr)
    values = [0 if i is 0 else i / abs(i) for i in arr]
    for num in map(values.count, [1, -1, 0]):
        print("{:6f}".format(num / n))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
