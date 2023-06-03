t = int(input())
for _ in range(t):
    n, q = map(int, input().strip().split())
    s = input().strip()
    p = []
    j = 0
    for i in range(n):
        if s[i] != s[i - 1]:
            j += 1
        p.append(j)
    m = n - 1
    for _ in range(q):
        x, y = sorted(map(int, input().strip().split()))
        x -= 1
        y -= 1
        print(min(p[y] - p[x], p[m] - p[y] + p[x]))
