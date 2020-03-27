#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gemstones function below.
def gemstones(arr):
    return len(set.intersection(*[set(rock) for rock in arr]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
