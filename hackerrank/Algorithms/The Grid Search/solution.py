#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gridSearch function below.
def gridSearch(G, P):
    g_rows = len(G)
    g_cols = len(G[0])
    p_rows = len(P)
    p_cols = len(P[0])
    for row in range(g_rows - p_rows + 1):
        for col in range(g_cols - p_cols + 1):
            if G[row][col:col + p_cols] == P[0]:
                for line in range(1, p_rows):
                    if G[row + line][col:col + p_cols] != P[line]:
                        break  # Found a mismatch
                else:
                    return 'YES'  # Found full pattern
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
