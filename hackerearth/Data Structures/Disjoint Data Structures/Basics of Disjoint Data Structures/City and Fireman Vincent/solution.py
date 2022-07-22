from collections import defaultdict


def find(x, parents):
    while x != parents[x]:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x


def union(x, y, parents, ranks):
    px = find(x, parents)
    py = find(y, parents)
    if px != py:
        if ranks[px] >= ranks[py]:
            parents[py] = px
            ranks[px] += ranks[py]
        else:
            parents[px] = py
            ranks[py] += ranks[px]


n = int(input())
e = list(map(int, input().strip().split()))
k = int(input())
roots = list(range(n))
sizes = [1] * n
for _ in range(k):
    i, j = map(lambda x: int(x) - 1, input().strip().split())
    union(i, j, roots, sizes)
w = 1
ways = defaultdict(list)
for i in range(n):
    p = find(i, roots)
    ways[p].append(e[i])
for i in ways:
    min_way = min(ways[i])
    w *= ways[i].count(min_way)
    w %= 1000000007
print(w)
