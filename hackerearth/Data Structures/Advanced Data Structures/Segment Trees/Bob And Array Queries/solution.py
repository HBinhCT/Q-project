from sys import stdin


def update(arr, idx, val, length):
    while idx <= length:
        arr[idx] += val
        idx += idx & -idx


def find_total(arr, idx):
    total = 0
    while idx:
        total += arr[idx]
        idx -= idx & -idx
    return total


n, q = map(int, stdin.readline().strip().split())
a = [0] * (n + 1)
for _ in range(q):
    p, *query = map(int, stdin.readline().strip().split())
    if p == 1:
        x = query[0]
        update(a, x, 1, n)
    elif p == 2:
        x = query[0]
        if find_total(a, x) - find_total(a, x - 1):
            update(a, x, -1, n)
    elif p == 3:
        x, y = query
        print(find_total(a, y) - find_total(a, x - 1))
