t = int(input())
for _ in range(t):
    c, n = map(int, input().strip().split())
    z = n * (n + 1) // 2
    if z >= c:
        print(c)
    else:
        c -= z
        print(c % n)
