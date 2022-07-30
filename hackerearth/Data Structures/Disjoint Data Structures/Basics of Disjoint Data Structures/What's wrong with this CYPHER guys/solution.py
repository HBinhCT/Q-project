from sys import stdin


def find(a, parents):
    while a != parents[a]:
        parents[a] = parents[parents[a]]
        a = parents[a]
    return a


def union(a, b, parents, ranks):
    pa = find(a, parents)
    pb = find(b, parents)
    if pa == pb:
        return
    if ranks[pa] < ranks[pb]:
        parents[pa] = parents[pb]
        ranks[pb] += ranks[pa]
    else:
        parents[pb] = parents[pa]
        ranks[pa] += ranks[pb]


t = int(stdin.readline())
for _ in range(t):
    n, q = map(int, stdin.readline().strip().split())
    roots = list(range(n))
    sizes = [1] * n
    res = {
        'yes': 0,
        'no': 0,
    }
    for _ in range(q):
        p, x, y = stdin.readline().strip().split()
        x = int(x) - 1
        y = int(y) - 1
        if p == 'J':
            union(x, y, roots, sizes)
        elif p == '?':
            if find(x, roots) == find(y, roots):
                res['yes'] += 1
            else:
                res['no'] += 1
    print(res['yes'], res['no'])
