from collections import deque
from sys import stdin


def find(u, ps):
    while u != ps[u]:
        ps[u] = ps[ps[u]]
        u = ps[u]
    return u


def join(u, v, ps, gs):
    pu = find(u, ps)
    if pu != v:
        ps[pu] = gs[pu] = v


def ranking(u, gs, rs, seen):
    stack = deque([(1, u)])
    while stack:
        check, u = stack.pop()
        if check:
            stack.append((0, u))
            if gs[u] == u:
                rs[u] = 0
                seen[u] = True
            elif not seen[gs[u]]:
                stack.append((1, gs[u]))
        else:
            rs[u] = rs[gs[u]] + 1
            seen[u] = True


n, q = map(int, stdin.readline().strip().split())
m = n * n
grid = []
for i in range(n):
    grid.extend(list(map(int, stdin.readline().strip().split())))
idxes = sorted(range(m), key=lambda x: grid[x])
parents = list(range(m))
groups = list(range(m))
for i in idxes:
    cell = grid[i]
    if groups[i] == i:
        row, col = divmod(i, n)
        if col and grid[i - 1] <= cell:
            join(i - 1, i, parents, groups)
        if col + 1 < n and grid[i + 1] < cell:
            join(i + 1, i, parents, groups)
        if row > 0 and grid[i - n] <= cell:
            join(i - n, i, parents, groups)
        if row + 1 < n and grid[i + n] < cell:
            join(i + n, i, parents, groups)
levels = [0] * m
visited = [0] * m
for i in range(m):
    ranking(i, groups, levels, visited)
mx = 18
dp = [[0] * m for _ in range(mx)]
for i in range(m):
    dp[0][i] = groups[i]
for i in range(mx - 1):
    for j in range(m):
        dp[i + 1][j] = dp[i][dp[i][j]]
for _ in range(q):
    x1, y1, x2, y2 = map(int, stdin.readline().strip().split())
    d1 = x1 * n + y1
    d2 = x2 * n + y2
    if levels[d1] != levels[d2]:
        swap = False
        if levels[d1] < levels[d2]:
            d1, d2 = d2, d1
            swap = True
        i = 0
        while levels[dp[i][d1]] > levels[d2]:
            i += 1
        for j in range(i, -1, -1):
            if levels[dp[j][d1]] >= levels[d2]:
                d1 = dp[j][d1]
        if swap:
            d1, d2 = d2, d1
    if d1 != d2:
        i = 0
        while dp[i][d2] != dp[i][d1]:
            i += 1
        for j in range(i, -1, -1):
            if dp[j][d2] != dp[j][d1]:
                d1 = dp[j][d1]
                d2 = dp[j][d2]
        d1 = dp[0][d1]
        d2 = dp[0][d2]
    print(grid[d1])
