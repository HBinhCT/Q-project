#!/bin/python3

import os


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY tree
#  2. 2D_INTEGER_ARRAY queries
#

def solve(tree, queries):
    # Write your code here
    from bisect import bisect_right

    def find(x, p):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return p[x]

    def union(x, y, w8, p, r, d):
        px = find(x, p)
        py = find(y, p)
        d[w8] += len(r[px]) * len(r[py])
        if px != py:
            if len(r[py]) < len(r[px]):
                p[py] = px
                r[px].update(r[py])
                del r[py]
            else:
                p[px] = py
                r[py].update(r[px])
                del r[px]

    ln = len(tree) + 1
    tree.sort(key=lambda x: x[-1])
    paths = {0: 0}
    weights = [0]
    parents = {i: i for i in range(1, ln + 1)}
    rep = {i: {i} for i in range(1, ln + 1)}
    prev = 0
    for u, v, w in tree:
        if w != prev:
            weights.append(w)
            paths[w] = paths[prev]
        union(u, v, w, parents, rep, paths)
        prev = w
    for left, right in queries:
        wr = weights[bisect_right(weights, right) - 1]
        wl = weights[bisect_right(weights, left - 1) - 1]
        yield paths[wr] - paths[wl]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    tree = []

    for _ in range(n - 1):
        tree.append(list(map(int, input().rstrip().split())))

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(tree, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
