t = int(input())
for _ in range(t):
    n = int(input())
    a = tuple(map(int, input().strip().split()))
    print(min(a[i] + a[i + 1] for i in range(n - 1)))
