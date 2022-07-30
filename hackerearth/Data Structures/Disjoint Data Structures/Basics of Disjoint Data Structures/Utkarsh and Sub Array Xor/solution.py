from sys import stdin


def find(x, parents):
    y = parents.get(x, x)
    while x != y:
        parents[x] = parents.get(y, y)
        x = y
        y = parents.get(x, x)
    return x


mod = 1000000007
n, k = map(int, stdin.readline().strip().split())
roots = {}
ans = pow(2, n, mod)
for _ in range(k):
    u, v = map(int, stdin.readline().strip().split())
    pu = find(u - 1, roots)
    pv = find(v, roots)
    if pu != pv:
        ans *= pow(2, mod - 2, mod)
        ans %= mod
        roots[pv] = pu
    print(ans)
