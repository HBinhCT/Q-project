#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the bfs function below.
def bfs(n, m, edges, s):
    from collections import deque

    # Build graph
    graph = {}
    for num in range(1, n + 1):
        graph[num] = set()
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
    reached = {}
    # Explore graph once
    frontier = deque([(s, 0)])
    seen = {s}
    while frontier:
        curr_node, curr_cost = frontier.popleft()
        for neighbor in graph[curr_node]:
            if neighbor not in seen:
                seen.add(neighbor)
                reached[neighbor] = curr_cost + 6
                frontier.append((neighbor, curr_cost + 6))
    res = []
    for node in range(1, n + 1):
        if s != node:
            res.append(reached.get(node, -1))
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
