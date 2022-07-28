def find(a, parents):
    while parents[a] != -1:
        a = parents[a]
    return a


def union(a, b, parents, sizes, minimums, maximums):
    if sizes[a] < sizes[b]:
        parents[b] = a
        minimums[a] = min(minimums[a], minimums[b])
        maximums[a] = max(maximums[a], maximums[b])
    else:
        parents[a] = b
        minimums[b] = min(minimums[a], minimums[b])
        maximums[b] = max(maximums[a], maximums[b])


n = int(input())
elements = list(map(int, input().strip().split()))
roots = [-1] * n
smalls = elements.copy()
larges = elements.copy()
q = int(input())
for _ in range(q):
    p, *query = map(int, input().strip().split())
    if p == 1:
        x, y = query
        px = find(x - 1, roots)
        py = find(y - 1, roots)
        if px != py:
            union(px, py, roots, elements, smalls, larges)
    elif p == 2:
        try:
            x = query[0]
            p = find(x - 1, roots)
            print(abs(larges[p] - smalls[p]))
        except:
            print(0)
