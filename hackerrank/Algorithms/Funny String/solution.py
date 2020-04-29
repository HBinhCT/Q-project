#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the funnyString function below.
def funnyString(s):
    rev = s[::-1]
    for i in range(len(s) - 1):
        if abs(ord(s[i + 1]) - ord(s[i])) != abs(ord(rev[i + 1]) - ord(rev[i])):
            return 'Not Funny'
    return 'Funny'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
