mod = 987654319


def find(x, p):
    while True:
        if p[x] < 0:
            return x
        x = p[x]


n, maxw = map(int, input().strip().split())
maxw += 2
tree = []
for _ in range(n - 1):
    v, u, w = map(int, input().strip().split())
    tree.append((w, v, u))
tree.sort()
count = 1
most = -1
parents = [-1] * (n + 1)
for w, v, u in tree:
    most = max(most, w)
    diff = max(1, maxw - w)
    pv = find(v, parents)
    pu = find(u, parents)
    count = count * pow(diff, parents[pv] * parents[pu] - 1, mod) % mod
    parents[pv] += parents[pu]
    parents[pu] = pv
print(0 if maxw < most else count % mod)
