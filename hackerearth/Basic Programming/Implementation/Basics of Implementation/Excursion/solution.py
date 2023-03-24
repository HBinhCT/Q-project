from math import ceil

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().strip().split())
    cnt = ceil(n / k) + ceil(m / k)
    print(cnt)
