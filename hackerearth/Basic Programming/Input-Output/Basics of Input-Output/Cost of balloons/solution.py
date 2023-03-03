t = int(input())
for _ in range(t):
    g, p = map(int, input().strip().split())
    n = int(input())
    x = y = 0
    for _ in range(n):
        i, j = map(int, input().strip().split())
        x += i
        y += j
    if g > p:
        g, p = p, g
    if x < y:
        x, y = y, x
    print(x * g + y * p)
