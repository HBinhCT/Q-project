#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    graph, ans = list(range(g_nodes)), 0
    for node_from, node_to, weight in sorted(zip(g_from, g_to, g_weight), key=lambda x: x[-1]):
        if graph[node_from - 1] != graph[node_to - 1]:
            from_val, to_val = graph[node_from - 1], graph[node_to - 1]
            for i in range(len(graph)):
                if graph[i] == from_val:
                    graph[i] = to_val
            ans += weight
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    fptr.write(str(res) + '\n')

    fptr.close()
