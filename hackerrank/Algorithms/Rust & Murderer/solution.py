#!/bin/python3

import os


#
# Complete the rustMurdered function below.
#
def rustMurderer(n, roads, start):
    #
    # Write your code here.
    #
    from collections import defaultdict

    dists = [1] * n
    lanes = defaultdict(set)
    for u, v in roads:
        lanes[u].add(v)
        lanes[v].add(u)
    not_visited = lanes[start]
    newly_visited = set()
    curr_dist = 2
    while not_visited:
        for i in not_visited:
            diff = not_visited | lanes[i]
            if len(diff) < n:
                dists[i - 1] = curr_dist
                newly_visited.add(i)
        not_visited = not_visited - newly_visited
        newly_visited = set()
        curr_dist += 1
    del dists[start - 1]
    return dists


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        roads = []

        for _ in range(m):
            roads.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = rustMurderer(n, roads, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
