from functools import lru_cache


@lru_cache(None)
def choose(mask, size, lim, arr, total=0, prev_group=-1):
    if total > lim:
        return 0
    if total == lim:
        return 1
    res = 0
    for i in range(size):
        days, group = arr[i]
        if mask >> i & 1 and group != prev_group:
            res += choose(1 << i ^ mask, size, lim, arr, total + days, group)
    return res % 1000000007


t = int(input())
for _ in range(t):
    n, d = map(int, input().strip().split())
    projects = []
    for _ in range(n):
        projects.append(tuple(map(int, input().strip().split())))
    print(choose((1 << n) - 1, n, d, tuple(projects)))
