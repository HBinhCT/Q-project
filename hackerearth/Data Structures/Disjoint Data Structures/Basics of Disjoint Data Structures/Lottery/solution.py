def find(a, parents):
    children = []
    while a != parents[a]:
        children.append(a)
        a = parents[a]
    for b in children:
        parents[b] = a
    return a


def union(a, b, parents, flags):
    pa = find(a, parents)
    pb = find(b, parents)
    if flags[pa] and flags[pb]:
        return False
    if pa == pb:
        flags[pa] = True
        return True
    flags[pa] |= flags[pb]
    parents[pb] = pa
    return True


t = int(input())
for _ in range(t):
    n, r, c = map(int, input().strip().split())
    rooms = []
    for _ in range(n):
        x, y, z = map(int, input().strip().split())
        rooms.append((z, x - 1, y + r - 1))
    rooms.sort(reverse=True)
    roots = list(range(r + c))
    checks = [False] * (r + c)
    ans = 0
    for z, x, y in rooms:
        if union(x, y, roots, checks):
            ans += z
    print(ans)
