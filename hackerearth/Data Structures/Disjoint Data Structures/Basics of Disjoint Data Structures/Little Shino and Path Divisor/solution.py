from collections import defaultdict
from sys import stdin


def create(a, p, r, s, g):
    p[a] = a
    r[a] = 0
    s[a] = 1
    g.add(a)


def find(a, p):
    while a != p[a]:
        p[a] = p[p[a]]
        a = p[a]
    return a


def union(a, b, p, r, s, g):
    pa = find(a, p)
    pb = find(b, p)
    if pa != pb:
        if r[pa] > r[pb]:
            p[pb] = pa
            s[pa] += s[pb]
            g.discard(pb)
        else:
            p[pa] = pb
            if pa == pb:
                r[pb] += 1
            s[pb] += s[pa]
            g.discard(pa)


n, q = map(int, stdin.readline().strip().split())
tree = defaultdict(list)
max_weight = 0
min_weight = 100000
for _ in range(n - 1):
    x, y, w = map(int, stdin.readline().strip().split())
    x -= 1
    y -= 1
    tree[w].append((x, y))
    max_weight = max(max_weight, w)
    min_weight = min(min_weight, w)
parents = list(range(n))
ranks = [0] * n
sizes = [1] * n
uniq_parents = set(parents)
for _ in range(q):
    d = int(stdin.readline())
    if min_weight == max_weight:
        print(0 if max_weight % d else n * (n - 1) // 2)
        continue
    if d > max_weight:
        print(0)
        continue
    if d < min_weight:
        start = (min_weight // d + 1) * d if min_weight % d else min_weight
    else:
        start = d
    roots = set()
    visited = set()
    for w in range(start, max_weight + 1, d):
        if w in tree:
            for x, y in tree[w]:
                if x not in visited:
                    visited.add(x)
                    create(x, parents, ranks, sizes, uniq_parents)
                if y not in visited:
                    visited.add(y)
                    create(y, parents, ranks, sizes, uniq_parents)
                union(x, y, parents, ranks, sizes, uniq_parents)
                roots.add(find(x, parents))
    ans = 0
    for root in roots:
        if root in uniq_parents:
            size = sizes[root]
            ans += size * (size - 1) // 2
    print(ans)
