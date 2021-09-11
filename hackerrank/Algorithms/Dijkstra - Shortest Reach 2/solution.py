#!/bin/python3

import os
import sys


# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    import heapq
    from collections import defaultdict

    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))
    visited = [False for _ in range(n)]
    distances = [float('inf') for _ in range(n)]
    distances[s - 1] = 0
    heap = [(distances[s - 1], s)]  # Heap is a binary tree so distance is needed to make a comparison
    while heap:
        weight, node = heapq.heappop(heap)
        if not visited[node - 1]:
            visited[node - 1] = True
            for next_weight, next_node in graph[node]:
                if not visited[next_node - 1] and distances[next_node - 1] > next_weight + weight:
                    distances[next_node - 1] = next_weight + weight
                    heapq.heappush(heap, (distances[next_node - 1], next_node))
    del distances[s - 1]
    return [-1 if d == float('inf') else d for d in distances]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = set()

        for _ in range(m):
            edges.add(tuple(map(int, sys.stdin.readline().rstrip().split())))

        s = int(input())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
