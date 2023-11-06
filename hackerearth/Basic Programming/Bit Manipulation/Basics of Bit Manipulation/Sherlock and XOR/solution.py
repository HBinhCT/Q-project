t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    odd = sum(i % 2 for i in a)
    print((n - odd) * odd)
