t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    min_cost = 0
    for i in range(n - 1):
        min_cost += max(a[i], a[i + 1])
    print(min_cost)
