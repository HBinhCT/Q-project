def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


t = int(input())
for _ in range(t):
    a = int(input())
    while sum_digits(a) % 4:
        a += 1
    print(a)
