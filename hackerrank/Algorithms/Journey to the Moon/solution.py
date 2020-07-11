#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the journeyToMoon function below.
def journeyToMoon(n, astronaut):
    countries = []
    asts = []
    for i in range(n):
        countries.append({i})
        asts.append(i)  # countries[asts[i]] contains i
    for a, b in astronaut:
        if a not in countries[asts[b]]:
            # union the countries
            union = countries[asts[a]] | countries[asts[b]]
            countries[a] = union  # store the union at countries[a]
            for i in union:  # pointers to a
                if i != a:
                    countries[i] = set()
                asts[i] = a
    total = 0
    non_singles = 0
    for i in range(n):
        size = len(countries[i])
        if size > 1:  # non-single set with length countries[i]
            non_singles += size
            # add pairs with first person in the subset
            total += size * (n - size)
    # singles = n - non_singles
    # add pairs with first person in the set of singles
    total = total + (n - non_singles) * (n - 1)
    # remove double counting
    total = total // 2
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
