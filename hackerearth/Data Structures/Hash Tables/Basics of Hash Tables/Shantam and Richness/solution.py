from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n, m = map(int, stdin.readline().strip().split())
    l, r, c, p, q, s = map(int, stdin.readline().strip().split())
    donating = [0] * (2 * n)
    for _ in range(m):
        donating[l] += c
        donating[r + 1] -= c
        li = (l * p + r) % n + 1
        ri = (r * q + l) % n + 1
        l = min(ri, li)
        r = max(ri, li)
        c = c * s % 1000000 + 1
    obtain = pos = highest = 0
    for i in range(n):
        obtain += donating[i]
        if obtain > highest:
            highest = obtain
            pos = i
    print(pos, highest)
