#!/bin/python3

import os
import sys


#
# Complete the roadsInHackerland function below.
#
def roadsInHackerland(n, roads):
    #
    # Write your code here.
    #
    def find(x):
        while x != parent[parent[x]]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        p_x = find(x)
        p_y = find(y)
        parent[p_y] = p_x

    def is_connected(x, y):
        p_x = find(x)
        p_y = find(y)
        return p_x == p_y

    # Run DFS to count the number of times an edge is used
    # as weights of all edges is different, hence each weight maps to a particular children
    def dfs(src, res, p=-1):
        total = 1
        for node, weight in tree[src]:
            if node != p:
                children = dfs(node, res, src)
                # children => nodes right to edge, n - children => nodes left to edge
                res[weight] += (n - children) * children
                total += children
        return total

    from collections import defaultdict

    edges = []
    parent = [i for i in range(n)]
    for u, v, w in roads:
        edges.append((u - 1, v - 1, w))
    # build MST
    tree = defaultdict(list)
    edges.sort(key=lambda x: x[2])
    for u, v, w in edges:
        if not is_connected(u, v):
            union(u, v)
            tree[u].append((v, w))
            tree[v].append((u, w))
    ans = [0] * (2 * len(roads))
    dfs(0, ans)
    final = 0
    for i in range(len(ans)):
        final += ans[i] * (1 << i)
    return str(bin(final))[2:]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    result = roadsInHackerland(n, roads)

    fptr.write(result + '\n')

    fptr.close()
