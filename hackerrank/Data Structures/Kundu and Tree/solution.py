def find(x, p):
    while p[x] >= 0:
        if p[p[x]] >= 0:
            p[x] = p[p[x]]
        x = p[x]
    return x


n = int(input())
parents = [-1] * n
for i in range(n - 1):
    u, v, color = input().strip().split()
    u = int(u) - 1
    v = int(v) - 1
    if color == 'b':
        pu, pv = find(u, parents), find(v, parents)
        if parents[pu] > parents[pv]:
            pu, pv = pv, pu
        parents[pu] += parents[pv]
        parents[pv] = pu
a, b, c = 0, 0, 0
for i in range(n):
    if parents[i] < 0:
        c -= b * parents[i]
        b -= a * parents[i]
        a -= parents[i]
print(c % 1000000007)
