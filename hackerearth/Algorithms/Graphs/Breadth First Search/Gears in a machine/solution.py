from collections import defaultdict, deque
from operator import xor
from sys import stdin

n, m, q = map(int, stdin.readline().strip().split())
external_gears = [i == '1' for i in stdin.readline().strip().split()]
external_gears.insert(0, False)
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)
n += 1
clockwise_gears = [False] * n
visited = [False] * n
groups = [-1] * n
j = 0
rotations = {}
queue = deque()
for i in range(1, n):
    if visited[i]:
        continue
    clockwise_gears[i] = True
    visited[i] = True
    queue.append(i)
    is_functional = True
    while queue:
        u = queue.popleft()
        groups[u] = j
        du = clockwise_gears[u]
        for v in graph[u]:
            dv = xor(du, external_gears[v] and external_gears[u])
            if visited[v]:
                if dv != clockwise_gears[v]:
                    is_functional = False
                continue
            clockwise_gears[v] = dv
            visited[v] = True
            queue.append(v)
    rotations[j] = is_functional
    j += 1
for _ in range(q):
    gp, gf, dir_p, dir_f = map(int, stdin.readline().strip().split())
    dir_p = dir_p == 1
    dir_f = dir_f == 1
    group_p = groups[gp]
    group_f = groups[gf]
    check = rotations[group_p] and rotations[group_f] and (
            group_p != group_f or (xor(clockwise_gears[gp], dir_p) == xor(clockwise_gears[gf], dir_f)))
    print('YES' if check else 'NO')
