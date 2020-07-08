#!/bin/python3

import math
import os
import random
import re
import sys


def tower_of_hanoi(disks):
    from collections import deque

    def tuplify(x):
        return tuple(map(tuple, x))

    def get_moves(node):
        for i in range(len(node)):
            if node[i]:
                for j in range(len(node)):
                    if not node[j] or node[i][-1] < node[j][-1]:
                        yield i, j

    def move(st, fro, to):
        d = [list(x) for x in st]
        d[to].append(d[fro].pop())
        # WLOG sort 2nd-4th stacks by order of largest disk
        d[1:4] = sorted(d[1:4], key=lambda x: x[-1] if x else 0)
        return tuplify(d)

    towers = [[] for _ in range(4)]  # has 4 rods
    for i in range(len(disks)):
        towers[disks[i] - 1] = [i + 1] + towers[disks[i] - 1]
    visited = set()
    start = (tuplify(towers), 0)
    queue = deque([start])
    visited.add(start)
    while queue:
        state, count = queue.popleft()
        if len(state[0]) == len(disks):
            return count
        else:
            for from_tower, to_tower in get_moves(state):
                new_state = move(state, from_tower, to_tower)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, count + 1))


if __name__ == '__main__':
    N = int(input())

    a = list(map(int, input().rstrip().split()))

    print(tower_of_hanoi(a))
