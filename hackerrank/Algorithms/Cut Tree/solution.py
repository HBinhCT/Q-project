#!/bin/python3

import os


#
# Complete the cuttree function below.
#
def cuttree(n, k, edges):
    #
    # Write your code here.
    #
    from collections import defaultdict

    adj = defaultdict(list)
    dp = [[0] * (k + 1) for _ in range(n)]
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    def compute(x, val, graph, matrix, most):
        matrix[x][0] = 1
        for y in graph[x]:
            if y != val:
                compute(y, x, graph, matrix, most)
                for i in range(most, -1, -1):
                    matrix[x][i] *= matrix[y][0]
                    for j in range(1, i + 1):
                        matrix[x][i] += matrix[x][i - j] * matrix[y][j]
                    if i > 0:
                        matrix[x][i] += matrix[x][i - 1]

    compute(0, 0, adj, dp, k)
    ans = 0
    for u in range(n):
        for v in range(0, k + (u == 0)):
            ans += dp[u][v]
    return ans + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cuttree(n, k, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
