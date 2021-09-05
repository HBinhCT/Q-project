#!/bin/python3

import os


#
# Complete the 'balancedForest' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY c
#  2. 2D_INTEGER_ARRAY edges
#

def balancedForest(c, edges):
    # Write your code here
    from collections import Counter, defaultdict

    def tree_sum(u, parent, amounts, adjacency, counts, sums):
        res = 0
        for v in adjacency[u]:
            if v != parent:
                res += tree_sum(v, u, amounts, adjacency, counts, sums)
        res += amounts[u]
        counts[res] += 1
        sums[u] = res
        return res

    def find_min_extra(u, parent, path, total, adjacency, counts, sums):
        s = sums[u]
        path.add(s)
        min_val = min(
            (find_min_extra(
                v,
                u,
                path,
                total,
                adjacency,
                counts,
                sums
            ) for v in adjacency[u] if v != parent),
            default=float('inf'),
        )
        if 3 * s < total:
            if not (total + s) % 2:
                s1 = (total + s) // 2
                if s1 in path:
                    min_val = min(min_val, s1 - 2 * s)
                s2 = (total - s) // 2
                count = counts[s2]
                if count > 0 and (s2 not in path or count > 1):
                    min_val = min(min_val, s2 - s)
        else:
            s1 = 2 * s
            if s1 in path:
                min_val = min(min_val, s + s1 - total)
            s1 = total - s
            if s1 in path:
                min_val = min(min_val, 2 * s - s1)
            if counts[s] > 1:
                min_val = min(min_val, 3 * s - total)
        path.remove(s)
        return min_val

    adj = defaultdict(set)
    for edge in edges:
        x, y = map(lambda i: i - 1, edge)
        adj[x].add(y)
        adj[y].add(x)
    counter = Counter()
    totals = {}
    tot = tree_sum(0, -1, c, adj, counter, totals)
    ans = find_min_extra(0, -1, set(), tot, adj, counter, totals)
    return ans if ans < float('inf') else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()
