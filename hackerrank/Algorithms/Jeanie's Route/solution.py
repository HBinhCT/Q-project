#!/bin/python3

import os
import sys


#
# Complete the jeanisRoute function below.
#
def jeanisRoute(n, k, roads, cities):
    #
    # Write your code here.
    #
    from collections import defaultdict

    # Adjacency list
    adj = defaultdict(dict)
    for u, v, w in roads:
        adj[u][v] = w
        adj[v][u] = w
    active = [cities[0]]
    total_distance = 0
    longest = 0
    parent = [0] * n
    depth = [-1] * n
    necessity = [False] * n
    for i in cities:
        necessity[i - 1] = 1
    while active:
        node = active[-1]
        if depth[node - 1] < 0:
            depth[node - 1] = 0
            for child in adj[node]:
                if child == parent[node - 1]:
                    continue
                parent[child - 1] = node
                active.append(child)
        else:
            active.pop()
            depth1 = 0  # deepest
            depth2 = 0  # second deepest
            for child in adj[node]:
                if child == parent[node - 1]:
                    continue
                if necessity[child - 1]:
                    necessity[node - 1] = True
                    total_distance += 2 * adj[node][child]
                    d = depth[child - 1] + adj[node][child]
                    if d > depth1:
                        depth2 = depth1
                        depth1 = d
                    elif d > depth2:
                        depth2 = d
            depth[node - 1] = depth1
            if depth1 + depth2 > longest:
                longest = depth1 + depth2
    return total_distance - longest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, k = map(int, sys.stdin.readline().split())

    city = list(map(int, sys.stdin.readline().rstrip().split()))

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, sys.stdin.readline().rstrip().split())))

    result = jeanisRoute(n, k, roads, city)

    fptr.write(str(result) + '\n')

    fptr.close()
