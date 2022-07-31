def find(a, parents):
    while a != parents[a]:
        parents[a] = parents[parents[a]]
        a = parents[a]
    return a


n = int(input())
xi = []
yi = []
for i in range(n):
    x, y = map(int, input().strip().split())
    xi.append((x, i))
    yi.append((y, i))
xi.sort()
yi.sort()
diffs = []
for i in range(n - 1):
    diffs.append((xi[i + 1][0] - xi[i][0], xi[i][1], xi[i + 1][1]))
    diffs.append((yi[i + 1][0] - yi[i][0], yi[i][1], yi[i + 1][1]))
diffs.sort()
roots = list(range(n))
min_cost = i = 0
while n > 1:
    d, u, v = diffs[i]
    pu = find(u, roots)
    pv = find(v, roots)
    if pu != pv:
        min_cost += d
        roots[pv] = pu
        n -= 1
    i += 1
print(min_cost)
