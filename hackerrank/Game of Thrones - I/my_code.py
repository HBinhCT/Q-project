#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gameOfThrones function below.
def gameOfThrones(s):
    from collections import Counter
    s1 = Counter(s)
    num_odd = 0
    for each in s1.values():
        if each % 2 != 0:
            num_odd += 1
            # when num_odd > 1, not palindrome
            if num_odd > 1:
                return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
