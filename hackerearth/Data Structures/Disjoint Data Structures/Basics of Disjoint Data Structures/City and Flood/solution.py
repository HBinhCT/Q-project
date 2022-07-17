from collections import defaultdict


def find(x, parents):
    while x != parents[x]:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x


def join(x, y, parents, ranks):
    px = find(x, parents)
    py = find(y, parents)
    if ranks[px] < ranks[py]:
        parents[px] = py
        ranks[py] += ranks[px]
    else:
        parents[py] = px
        ranks[px] += ranks[py]


n = int(input())
k = int(input())
roots = [i for i in range(n)]
sizes = defaultdict(int)
for _ in range(k):
    i, j = map(lambda x: int(x) - 1, input().strip().split())
    join(i, j, roots, sizes)
print(len(set(find(i, roots) for i in roots)))
