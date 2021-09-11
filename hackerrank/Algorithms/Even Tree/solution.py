#!/bin/python3

import os


# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    weight = {}
    for i in range(t_edges - 1, -1, -1):
        if t_from[i] in weight:
            weight[t_from[i]] += 1
        else:
            weight[t_from[i]] = 1
        if t_to[i] in weight:
            weight[t_to[i]] += weight[t_from[i]]
        else:
            weight[t_to[i]] = weight[t_from[i]]
    return sum(weight[key] % 2 == 0 for key in weight)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
