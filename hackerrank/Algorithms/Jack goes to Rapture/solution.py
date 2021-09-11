#!/bin/python3


#
# Complete the 'getCost' function below.
#
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

def getCost(g_nodes, g_from, g_to, g_weight):
    # Print your answer within the function and return nothing
    parent = [-1] * g_nodes

    def find(n):
        if parent[n] < 0:
            return n
        pt = find(parent[n])
        parent[n] = pt
        return pt

    if find(0) == find(g_nodes - 1):
        print(0)
    else:
        for w, f, t in sorted(zip(g_weight, g_from, g_to)):
            f = find(f - 1)
            t = find(t - 1)
            if f != t:
                if parent[f] == parent[t]:
                    parent[t] -= 1
                if parent[f] > parent[t]:
                    parent[f] = t
                else:
                    parent[t] = f
            if find(0) == find(g_nodes - 1):
                print(w)
                break
        else:
            print('NO PATH EXISTS')


if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    getCost(g_nodes, g_from, g_to, g_weight)
