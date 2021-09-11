#!/bin/python3

import os


# Complete the prims function below.
def prims(n, edges, start):
    import heapq
    from collections import defaultdict

    graph, heap, ans = defaultdict(list), [], 0
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))
    '''
    defaultdict(<class 'list'>, {1: [(3, 2), (4, 3)], 2: [(3, 1), (6, 4), (2, 5), (5, 3)], 3: [(4, 1), (5, 2), (7, 5)], 
    4: [(6, 2)], 5: [(2, 2), (7, 3)]})
    '''
    visited = [False] * n
    heapq.heappush(heap, (0, start))  # starting from node "start" with weight 0
    heapq.heapify(heap)
    while heap:
        weight, node = heapq.heappop(heap)
        if not visited[node - 1]:  # index starts at 0 instead of 1
            visited[node - 1] = True
            ans += weight
            for neighbor_weight, neighbor_node in graph[node]:
                heapq.heappush(heap, (neighbor_weight, neighbor_node))
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
