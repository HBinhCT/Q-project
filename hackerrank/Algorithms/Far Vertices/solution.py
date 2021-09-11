#!/bin/python3

import os


#
# Complete the farVertices function below.
#
def farVertices(n, k, edges):
    #
    # Write your code here.
    #
    from collections import Counter

    tree = {}
    for edge in edges:
        tree[edge[0], edge[1]] = tree[edge[1], edge[0]] = 1
    tree_paths = len(tree)
    while True:
        for edge in edges:
            matches = {x: y for x, y in tree.items() if edge[1] == x[0]}
            for match in matches.keys():
                if (edge[0], match[1]) not in tree.keys() and edge[0] != match[1]:
                    tree[edge[0], match[1]] = tree[match[1], edge[0]] = matches[match] + 1
            matches = {x: y for x, y in tree.items() if edge[0] == x[1]}
            for match in matches.keys():
                if (edge[1], match[0]) not in tree.keys() and edge[1] != match[0]:
                    tree[edge[1], match[0]] = tree[match[0], edge[1]] = matches[match] + 1
        if len(tree) == tree_paths:
            break
        tree_paths = len(tree)
    removed = 0
    while True:
        matches = [x[0] for x, y in tree.items() if y > k]
        if len(matches) == 0:
            break
        else:
            removed += 1
            match_count = Counter(matches)
            max_count = max(y for x, y in match_count.items())
            match_max = [x for x, y in match_count.items() if y == max_count]
            remove_node = match_max[0]
            nodes_to_remove = [x for x in tree.keys() if x[0] == remove_node or x[1] == remove_node]
            for node in nodes_to_remove:
                del tree[node]
    return removed


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = farVertices(n, k, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
