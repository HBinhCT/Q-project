#!/bin/python3

import os


# Complete the kingdomDivision function below.
def kingdomDivision(n, roads):
    from collections import Counter, defaultdict, deque

    edges = defaultdict(set)  # adjacency list
    degree = Counter()  # node degree
    for u, v in roads:
        edges[u].add(v)
        edges[v].add(u)
        degree[u] += 1
        degree[v] += 1
    # The possible divisions for a sub-tree rooted @ node is count[node][parent]
    # where parent = True if the node shares its parent's color
    count = {i: {True: 1, False: 1} for i in degree}
    # We accumulate counts by iteratively stripping leaves from the tree
    leaves = deque([i for i in degree if degree[i] == 1])
    while True:
        node = leaves.popleft()
        # If parent differs, exclude case where ALL children differ
        count[node][False] = count[node][True] - count[node][False]
        # If no edges left, we have reached root and are done
        if not degree[node]:
            root = node
            break
        else:
            # Otherwise update parent:
            parent = edges[node].pop()
            # update topology
            edges[parent].discard(node)
            degree[parent] -= 1
            if degree[parent] == 1:
                leaves.append(parent)
            # update counts
            count[parent][True] *= count[node][True] + count[node][False]
            count[parent][False] *= count[node][False]
    # Note each division has a corresponding one with colors switched
    total = 2 * count[root][0]
    return total % 1000000007  # 10 ** 9 + 7


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    result = kingdomDivision(n, roads)

    fptr.write(str(result) + '\n')

    fptr.close()
