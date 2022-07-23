def find(x, parents):
    children = []
    while x != parents[x]:
        children.append(x)
        x = parents[x]
    for y in children:
        parents[y] = x
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


t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    roots = list(range(n))
    sizes = [1] * n
    for _ in range(m):
        l, r = map(lambda x: int(x) - 1, input().strip().split())
        union(l, r, roots, sizes)
    circles = []
    for i in range(n):
        if i == find(i, roots):
            circles.append(i)
    if len(circles) == 1:
        print(0)
    else:
        res = total = 0
        for i in circles:
            res += sizes[i] * (n - sizes[i] - total)
            total += sizes[i]
        print(2 * res)
