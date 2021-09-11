#!/bin/python3

import os


#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#

def componentsInGraph(gb):
    # Write your code here
    from collections import Counter

    def parent(ps, i):
        if ps[i] != i:
            ps[i] = parent(ps, ps[i])
        return ps[i]

    parents = list(range(len(gb) * 2 + 1))
    for a, b in gb:
        p1, p2 = parent(parents, a), parent(parents, b)
        parents[p1] = parents[p2] = parents[a] = parents[b] = min(p1, p2)
    counter = Counter()
    for p in parents:
        counter[parent(parents, p)] += 1
    counts = [c for c in counter.values() if c > 1]
    return min(counts), max(counts)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
