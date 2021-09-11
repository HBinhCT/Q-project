#!/bin/python3

import os


# Complete the beautifulPath function below.
def beautifulPath(n, edges, A, B):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v, c in edges:
        graph[u].append((v, c))
        graph[v].append((u, c))
    queue = deque()
    distances = [defaultdict(lambda: 0) for _ in range(n)]
    distances[A - 1][0] = 0
    queue.append((A, 0))
    while queue:
        node, cost = queue.popleft()
        for next_node, next_cost in graph[node]:
            penalty = cost | next_cost
            if not distances[next_node - 1][penalty] and penalty <= 1024:
                distances[next_node - 1][penalty] = 1
                queue.append((next_node, penalty))
    return sorted(distances[B - 1])[0] if distances[B - 1] else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    AB = input().split()

    A = int(AB[0])

    B = int(AB[1])

    result = beautifulPath(n, edges, A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
