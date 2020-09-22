#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the angryChildren function below.
def angryChildren(k, packets):
    packets.sort()
    total = 0
    difference = 0
    for i in range(k - 1, -1, -1):
        difference += abs(packets[i] * (k - 1 - i) - total)
        total += packets[i]
    res = difference
    for i in range(k, len(packets)):
        total -= packets[i - k]
        difference -= abs(total - packets[i - k] * (k - 1))
        difference += abs(total - packets[i] * (k - 1))
        res = min(res, difference)
        total += packets[i]
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    packets = []

    for _ in range(n):
        packets_item = int(input())
        packets.append(packets_item)

    result = angryChildren(k, packets)

    fptr.write(str(result) + '\n')

    fptr.close()
