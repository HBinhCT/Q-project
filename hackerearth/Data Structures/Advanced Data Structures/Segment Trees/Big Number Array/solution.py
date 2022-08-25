from collections import defaultdict
from random import randint
from sys import stdin


def flip(arr, length, left, right, val):
    # increase value at 'left' by 'val'
    update(arr, length, left, val)
    # decrease value at 'right + 1' by 'val'
    update(arr, length, right + 1, val)


def update(arr, length, idx, val):
    while idx <= length:
        arr[idx] ^= val
        idx += idx & -idx


def count(arr, idx):
    cnt = 0
    while idx:
        cnt ^= arr[idx]
        idx -= idx & -idx
    return cnt


t = int(stdin.readline())
for _ in range(t):
    n, q = map(int, stdin.readline().strip().split())
    a = [0] * (n + 1)
    values = defaultdict(lambda: randint(1, 2 ** 63))
    for _ in range(q):
        kind, *query = map(int, stdin.readline().strip().split())
        if kind == 1:
            x, y, l, r = query
            flip(a, n, x, y, values[(l, r)])
        elif kind == 2:
            x, y = query
            print('YES' if count(a, x) == count(a, y) else 'NO')
