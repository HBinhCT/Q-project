#!/bin/python3

import os


#
# Complete the deforestation function below.
#
def deforestation(n, tree):
    #
    # Write your code here.
    #
    from collections import defaultdict

    def calculate(graph, x, parent=0):
        res = 0
        for i in graph[x]:
            if i != parent:
                res ^= calculate(graph, i, x)
        return res + 1

    adj = defaultdict(set)
    for u, v in tree:
        adj[u].add(v)
        adj[v].add(u)
    return 'Alice' if calculate(adj, 1) - 1 else 'Bob'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        tree = []

        for _ in range(n - 1):
            tree.append(list(map(int, input().rstrip().split())))

        result = deforestation(n, tree)

        fptr.write(result + '\n')

    fptr.close()
