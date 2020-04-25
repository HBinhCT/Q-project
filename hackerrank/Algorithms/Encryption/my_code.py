#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the encryption function below.
def encryption(s):
    return eval("' '.join(map(lambda x: '{0}'[x::{1}], range({1})))".format(s, math.ceil(math.sqrt(len(s)))))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
