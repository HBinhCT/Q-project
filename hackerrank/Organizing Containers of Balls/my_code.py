#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the organizingContainers function below.
def organizingContainers(container):
    row = sorted([sum(x) for x in container])
    col = sorted([sum(x) for x in zip(*container)])
    return 'Possible' if row == col else 'Impossible'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
