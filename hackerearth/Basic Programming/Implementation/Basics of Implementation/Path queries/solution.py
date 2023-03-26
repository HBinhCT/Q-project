from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n, q = map(int, stdin.readline().strip().split())
    a = [0] + [int(i) & 1 for i in stdin.readline().strip().split()]  # x & 1 is equivalent to x % 2
    for _ in range(n - 1):
        stdin.readline().strip()
    x = sum(a)
    y = n - x
    path = []
    for _ in range(q):
        u, val = map(int, stdin.readline().split())
        val &= 1
        if a[u] and not val:
            x -= 1
            y += 1
            a[u] = val
        elif not a[u] and val:
            x += 1
            y -= 1
            a[u] = val
        path.append(str(x * (x + 1) // 2 + y * (y + 1) // 2))
    print(' '.join(path))
