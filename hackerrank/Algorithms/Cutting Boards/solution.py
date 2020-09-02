#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the boardCutting function below.
def boardCutting(cost_y, cost_x):
    from heapq import heapify, heappop, heappush
    from itertools import chain, repeat

    segments = [1, 1]
    costs = [
        (x for x in chain(sorted(cost_y, reverse=True), repeat(-1))),
        (x for x in chain(sorted(cost_x, reverse=True), repeat(-1))),
    ]
    heap = []
    heapify(heap)
    heappush(heap, (-next(costs[0]), 0))
    heappush(heap, (-next(costs[1]), 1))
    total_cost = 0
    while True:
        cost, orient = heappop(heap)
        cost = -cost
        if cost == -1:
            break
        total_cost += cost * segments[orient]
        total_cost = int(total_cost % (1e9 + 7))
        segments[1 - orient] += 1
        heappush(heap, (-next(costs[orient]), orient))
    return total_cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        mn = input().split()

        m = int(mn[0])

        n = int(mn[1])

        cost_y = list(map(int, input().rstrip().split()))

        cost_x = list(map(int, input().rstrip().split()))

        result = boardCutting(cost_y, cost_x)

        fptr.write(str(result) + '\n')

    fptr.close()
