from math import gcd

t = int(input())
for _ in range(t):
    a, b = map(int, input().strip().split())
    c = gcd(a, b)
    print(b // c, a // c)
