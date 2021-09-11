#!/bin/python3

import os


# Complete the steadyGene function below.
def steadyGene(gene):
    from collections import Counter
    ln = len(gene)
    nus = Counter(gene)
    for key, value in nus.items():
        nus[key] -= ln / 4
    left = right = 0
    min_len = ln
    while right < ln:
        if all(map(lambda x: x <= 0, nus.values())):
            min_len = min(min_len, right - left)
            nus[gene[left]] += 1
            left += 1
        else:
            nus[gene[right]] -= 1
            right += 1
    return min_len


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
