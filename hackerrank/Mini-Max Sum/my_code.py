#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    a_min = math.inf
    a_max = -math.inf
    a_sum = 0
    for a in arr:
        if a < a_min:
            a_min = a
        if a > a_max:
            a_max = a
        a_sum += a
    print("{} {}".format(a_sum - a_max, a_sum - a_min))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
