#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return c_lib * n

    def repair(s, arr, visited):
        visited[s] = True
        cost = 0
        for x in arr[s]:
            if not visited[x]:
                cost += 1
                cost += repair(x, arr, visited)
        return cost

    g = []
    seen = []
    count = 0
    for _ in range(n + 1):
        g.append([0])
        seen.append(False)
    for i in range(1, n + 1):
        g[i][0] = i
    for i, j in cities:
        g[i].append(j)
        g[j].append(i)
    for i in range(1, n + 1):
        if not seen[i]:
            count += repair(i, g, seen)
    return count * c_road + (n - count) * c_lib


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
