#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    return sum(abs(s1.count(c) - s2.count(c)) for c in set(s1 + s2))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
