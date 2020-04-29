#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the viralAdvertising function below.
def viralAdvertising(n):
    total = 2
    liked = 2
    for _ in range(1, n):
        liked = liked * 3 // 2
        total += liked
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
