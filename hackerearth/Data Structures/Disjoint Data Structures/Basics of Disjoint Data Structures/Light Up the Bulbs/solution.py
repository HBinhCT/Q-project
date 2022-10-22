from math import inf, dist

n = int(input())
bulbs = []
for _ in range(n):
    x, y = map(int, input().strip().split())
    bulbs.append((x, y))
min_length = i = 0
visited = [False] * n
dists = [inf] * n
dists[0] = 0
while i < n:
    length = inf
    k = -1
    for j in range(n):
        if not visited[j] and length > dists[j]:
            length = dists[j]
            k = j
    visited[k] = True
    min_length += length
    i += 1
    for j in range(n):
        length = dist(bulbs[k], bulbs[j])
        length *= length
        if not visited[j] and dists[j] > length:
            dists[j] = length
print(int(min_length))
