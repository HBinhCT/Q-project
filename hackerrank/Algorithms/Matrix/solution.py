#!/bin/python3

import os


# Complete the minTime function below.
def minTime(roads, machines):
    from collections import defaultdict

    parent = {}
    dp = defaultdict(int)  # dp[i] denotes whether or not component with root i had already had a machine
    for machine in machines:
        dp[machine] = 1

    def find(node):
        if parent.get(node, node) == node:
            return node
        x = find(parent[node])
        parent[node] = x
        return x

    def union(i, j):
        x, y = find(i), find(j)
        if not dp[x] or not dp[y]:
            if i != x:
                x, y = y, x
            parent[x] = y
            dp[x] |= dp[y]
            dp[y] |= dp[x]
            return True
        return False

    return sum(time for i, j, time in sorted(roads, key=lambda i: -i[-1]) if not union(i, j))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machines = []

    for _ in range(k):
        machines_item = int(input())
        machines.append(machines_item)

    result = minTime(roads, machines)

    fptr.write(str(result) + '\n')

    fptr.close()
