def find(x, parents):
    while x != parents[x]:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x


def union(x, y, parents):
    px = find(x, parents)
    py = find(y, parents)
    if px != py:
        parents[px] = py


n, q = map(int, input().strip().split())
leaders = list(range(n + 1))
for _ in range(q):
    p, *query = map(int, input().strip().split())
    if p == 1:
        union(query[0], query[1], leaders)
    elif p == 2:
        a = query[0]
        pa = find(a, leaders)
        leaders[pa] = a
        leaders[a] = a
    else:
        print(find(query[0], leaders))
