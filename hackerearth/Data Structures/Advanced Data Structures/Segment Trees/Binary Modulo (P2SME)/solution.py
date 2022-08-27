from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    a = stdin.readline().strip()
    q = int(stdin.readline())
    for _ in range(q):
        kind, *query = stdin.readline().strip().split()
        if kind == '0':
            l, r = map(int, query)
            print(int(a[l: r + 1], 2) % 5)
        elif kind == '1':
            x, v = query
            x = int(x)
            a = a[:x] + v + a[x + 1:]
