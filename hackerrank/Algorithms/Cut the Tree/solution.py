#!/bin/python3

import os


#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#

def cutTheTree(data, edges):
    # Write your code here
    size = len(data)
    nodes = [[] for _ in range(size)]
    for u, v in edges:
        nodes[u - 1].append(v - 1)
        nodes[v - 1].append(u - 1)
    totals = [0] * size
    waiting = {i for i in range(size) if len(nodes[i]) == 1}
    while len(waiting):
        for i in waiting:
            totals[i] += data[i]
            if len(nodes[i]):
                nodes[nodes[i][0]].remove(i)
                totals[nodes[i][0]] += totals[i]
        waiting = {nodes[i][0] for i in waiting if len(nodes[i]) and len(nodes[nodes[i][0]]) == 1}

    total = sum(data)
    min_diff = abs(total - 2 * totals[0])
    for i in range(1, size):
        diff = abs(total - 2 * totals[i])
        if diff < min_diff:
            min_diff = diff
    return min_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
