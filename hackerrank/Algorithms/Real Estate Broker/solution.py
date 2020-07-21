#!/bin/python3

import os
import sys


#
# Complete the realEstateBroker function below.
#
def realEstateBroker(clients, houses):
    #
    # Write your code here.
    #
    size_clients = len(clients)
    size_houses = len(houses)
    data = [[] for _ in range(size_clients)]
    for i in range(size_clients):
        a, p = clients[i]
        for x, y in houses:
            data[i].append(int(a < x and p >= y))

    def is_interested_in(u, matched, visited):
        for v in range(size_houses):
            if data[u][v] and not visited[v]:
                visited[v] = True
                if matched[v] == -1 or is_interested_in(matched[v], matched, visited):
                    matched[v] = u
                    return True
        return False

    match = [-1] * size_houses
    res = 0
    for i in range(size_clients):
        seen = [False] * size_houses
        if is_interested_in(i, match, seen):
            res += 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    clients = []

    for _ in range(n):
        clients.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

    houses = []

    for _ in range(m):
        houses.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

    result = realEstateBroker(clients, houses)

    fptr.write(str(result) + '\n')

    fptr.close()
