n = int(input())
a = list(map(int, input().strip().split()))
print(next(i for i in range(n) if a[i] + i >= n) + 1)
