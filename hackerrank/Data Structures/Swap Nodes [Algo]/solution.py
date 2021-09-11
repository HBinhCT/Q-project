#!/bin/python3

import os
import sys


#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

def swapNodes(indexes, queries):
    # Write your code here
    sys.setrecursionlimit(2048)
    for k in queries:
        res = []

        def traversal(node, depth):
            if node == -1:
                return
            children = indexes[node - 1]
            if depth % k == 0:
                children[0], children[1] = children[1], children[0]
            traversal(children[0], depth + 1)
            res.append(node)
            traversal(children[1], depth + 1)

        traversal(1, 1)
        yield res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
