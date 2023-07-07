t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
    else:
        x = int((-3 + (9 + 8 * n) ** .5) / 2)
        print(2 * (n - x))
