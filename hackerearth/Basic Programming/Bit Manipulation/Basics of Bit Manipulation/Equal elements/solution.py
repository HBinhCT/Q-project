t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    x = sum(i % 2 for i in a)
    print(min(n - x, x))
