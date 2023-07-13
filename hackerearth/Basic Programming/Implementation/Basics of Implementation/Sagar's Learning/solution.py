t = int(input())
for _ in range(t):
    n = int(input())
    x = n // 3
    if x < 1:
        print(-1)
    else:
        print(x, x * 2, x * 3)
