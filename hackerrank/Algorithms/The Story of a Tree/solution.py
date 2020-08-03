#!/bin/python3

import os
import sys


#
# Complete the storyOfATree function below.
#
def storyOfATree(n, edges, k, guesses):
    #
    # Write your code here.
    #
    import fractions

    # Compute neighbors of nodes.
    neighbors = [[] for _ in range(n)]
    for [u, v] in edges:
        neighbors[u - 1].append(v - 1)
        neighbors[v - 1].append(u - 1)
    # Compute parents of nodes, assuming 0 is root.
    parents = [None] * n
    stack = [0]
    while stack:
        node = stack.pop()
        for neighbor in neighbors[node]:
            if neighbor == parents[node]:
                continue
            parents[neighbor] = node
            stack.append(neighbor)
    points = [None] * n
    # Convert guesses into a set.
    guess_set = set((u - 1, v - 1) for u, v in guesses)
    # Compute points[0].
    points[0] = 0
    for u, v in guess_set:
        if parents[v] == u:
            points[0] += 1
    # Compute points[1:].
    stack = list(neighbors[0])
    while stack:
        node = stack.pop()
        parent = parents[node]
        points[node] = points[parent]
        if (parent, node) in guess_set:
            points[node] -= 1
        if (node, parent) in guess_set:
            points[node] += 1
        for neighbor in neighbors[node]:
            if neighbor != parent:
                stack.append(neighbor)
    numerator = sum(p >= k for p in points)
    if not numerator:
        return '0/1'
    elif numerator == n:
        return '1/1'
    else:
        return str(fractions.Fraction(numerator, n))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        gk = input().split()

        g = int(gk[0])

        k = int(gk[1])

        guesses = []

        for _ in range(g):
            guesses.append(list(map(int, input().rstrip().split())))

        result = storyOfATree(n, edges, k, guesses)

        fptr.write(result + '\n')

    fptr.close()
