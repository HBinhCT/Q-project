#!/bin/python3

import os
import sys


#
# Complete the bendersPlay function below.
#
def bendersPlay(n, paths, queries):
    #
    # Write your code here.
    #
    from collections import defaultdict
    from functools import lru_cache, reduce
    from operator import xor

    def mex(s):
        i = 0
        while i in s:
            i += 1
        return i

    @lru_cache(maxsize=None)
    def calculate(x):
        return mex({calculate(i) for i in graph[x]})

    graph = defaultdict(list)
    for u, v in paths:
        graph[u].append(v)
    res = []
    for query in queries:
        res.append('Bumi' if reduce(xor, [calculate(t) for t in query]) else 'Iroh')
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    paths = []

    for _ in range(m):
        paths.append(list(map(int, input().rstrip().split())))

    q = int(input())

    queries = []

    for q_itr in range(q):
        query_count = int(input())

        queries.append(list(map(int, input().rstrip().split())))

    results = bendersPlay(n, paths, queries)

    fptr.write('\n'.join(results) + '\n')

    fptr.close()
