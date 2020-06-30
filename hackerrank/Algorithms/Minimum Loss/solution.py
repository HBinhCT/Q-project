#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumLoss function below.
def minimumLoss(price):
    price_list = sorted(enumerate(price), key=lambda x: -x[1])
    return min(price_list[i][1] - price_list[i + 1][1] for i in range(len(price) - 1) if
               price_list[i][0] < price_list[i + 1][0])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
