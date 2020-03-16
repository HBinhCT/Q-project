#!/bin/python3

import math
import os
import random
import re
import sys
import functools
from string import ascii_lowercase, ascii_uppercase


# Complete the caesarCipher function below.
def caesarCipher(s, k):
    return s.translate(get_trans(k % 26))


@functools.lru_cache(maxsize=26)
def get_trans(k):
    return str.maketrans(
        ascii_lowercase + ascii_uppercase,
        ascii_lowercase[k:] + ascii_lowercase[:k] +
        ascii_uppercase[k:] + ascii_uppercase[:k]
    )


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
