t = int(input())
for _ in range(t):
    n = int(input())
    c = 0
    i = 5
    while n / i >= 1:
        c += n // i
        i *= 5
    print(c)
