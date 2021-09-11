#!/bin/python3

import os


# Complete the findConnectedComponents function below.
def findConnectedComponents(d):
    def count_components(cliques, prev_components, i):
        if i >= len(cliques):
            return len(prev_components)
        c = count_components(cliques, prev_components, i + 1)
        # now add a clique
        new_comp = cliques[i]
        new_components = []
        for comp in prev_components:
            if comp & new_comp != 0:  # check if two components intersect
                new_comp |= comp  # merge them into one
            else:
                new_components.append(comp)
        if new_comp:
            new_components.append(new_comp)
        c += count_components(cliques, new_components, i + 1)
        return c

    singletons = [1 << i for i in range(64)]  # x << y is the same as multiplying x by 2**y
    return count_components(d, singletons, 0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d_count = int(input())

    d = list(map(int, input().rstrip().split()))

    components = findConnectedComponents(d)

    fptr.write(str(components) + '\n')

    fptr.close()
