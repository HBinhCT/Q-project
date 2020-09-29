#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    # Write your code here
    profit = 0
    predicted = prices.copy()
    while predicted:
        max_idx = predicted.index(max(predicted))
        selected_prices = predicted[:max_idx]
        profit += predicted[max_idx] * len(selected_prices) - sum(selected_prices)
        predicted = predicted[max_idx + 1:]
    return profit


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
