#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right, bisect_left
from collections import defaultdict


def prepare_data(gene_list, health_list):
    genes_dict = defaultdict(lambda: [[], [0]])
    genes_set = set()
    for i, gene in enumerate(gene_list):
        genes_dict[gene][0].append(i)
        for j in range(1, len(gene) + 1):
            genes_set.add(gene[:j])
    for value in genes_dict.values():
        for i, j in enumerate(value[0]):
            value[1].append(value[1][i] + health_list[j])
    return genes_dict, genes_set, max(map(len, gene_list))


def get_health(strand, start, end, max_width, genes_mapping, sub_list):
    total_health = 0
    len_strand = len(strand)
    for i in range(len_strand):
        for j in range(1, min(max_width + 1, len_strand - i + 1)):
            sub = strand[i:i + j]
            if sub not in sub_list:
                break
            if sub not in genes_mapping:
                continue
            ids, health_sub = genes_mapping[sub]
            total_health += health_sub[bisect_right(ids, end)] - health_sub[bisect_left(ids, start)]
    return total_health


if __name__ == '__main__':
    n = int(input())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input())

    genes_map, subs, largest = prepare_data(genes, health)

    healths = []

    for s_itr in range(s):
        firstLastd = input().split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        d = firstLastd[2]

        total = get_health(d, first, last, largest, genes_map, subs)

        healths.append(total)

    print(min(healths), max(healths))
