#!/bin/python3

import os
import sys


#
# Complete the crabGraphs function below.
#
def crabGraphs(n, t, graph):
    #
    # Write your code here.
    #
    from collections import defaultdict, deque

    def ford_fulkerson(adj, start, to, size):
        parent = [0] * size
        res = 0
        while bfs(adj, parent, start, to, size):
            f = float('inf')
            v = to
            while v != start:
                u = parent[v]
                f = min(f, adj[u][v])
                v = parent[v]
            v = to
            while v != start:
                u = parent[v]
                adj[u][v] -= f
                adj[v][u] += f
                v = parent[v]
            res += f
        return res

    def bfs(adj, parent, start, to, size):
        visits = defaultdict(int)
        queue = deque([start])
        visits[start] += 1
        parent[start] = -1
        while queue:
            u = queue.popleft()
            for v in range(size):
                if visits[v] == 0 and adj[u][v] > 0:
                    queue.append(v)
                    parent[v] = u
                    visits[v] += 1
        return visits[to] == 1

    g = [[0] * (2 * n + 2) for _ in range(2 * n + 2)]
    for a, b in graph:
        g[2 * a][2 * b + 1] = 1
        g[2 * b][2 * a + 1] = 1
    for i in range(1, n + 1):
        g[0][2 * i] = t
        g[2 * i + 1][1] = 1
    return ford_fulkerson(g, 0, 1, 2 * n + 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    c = int(input())

    for c_itr in range(c):
        ntm = input().split()

        n = int(ntm[0])

        t = int(ntm[1])

        m = int(ntm[2])

        graph = []

        for _ in range(m):
            graph.append(list(map(int, input().rstrip().split())))

        result = crabGraphs(n, t, graph)

        fptr.write(str(result) + '\n')

    fptr.close()
