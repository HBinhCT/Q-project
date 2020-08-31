#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jimOrders function below.
def jimOrders(orders):
    return [i[0] for i in sorted(enumerate(orders, 1), key=lambda x: sum(x[1]))]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
