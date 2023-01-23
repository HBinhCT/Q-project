from collections import defaultdict


def find(x, p):
    while x != p[x]:
        p[x] = p[p[x]]
        x = p[x]
    return x


def union(x, y, p, sz, st):
    px = find(x, p)
    py = find(y, p)
    if px != py:
        p[py] = px
        sz[px] += sz[py]
        st[px] += st[py]
        sz[py] = st[py] = 0


t = int(input())
for _ in range(t):
    n, q = map(int, input().strip().split())
    parents = defaultdict(int)
    sizes = defaultdict(int)
    strengths = defaultdict(int)
    for i in range(1, n + 1):
        parents[-i] = parents[i] = -i
        strengths[-i] = i
        sizes[-i] = 1
    for _ in range(q):
        q, *query = map(int, input().strip().split())
        if 1 == q:
            a, b = query
            union(a, b, parents, sizes, strengths)
        elif 2 == q:
            a = query[0]
            pa = find(a, parents)
            print(sizes[pa], strengths[pa])
        elif 3 == q:
            a, b = query
            pa = find(a, parents)
            pb = find(b, parents)
            if pa != pb:
                sizes[pa] -= 1
                strengths[pa] -= a
                pa = parents[a] = a
                sizes[pa] = 1
                strengths[pa] = a
                union(b, a, parents, sizes, strengths)
