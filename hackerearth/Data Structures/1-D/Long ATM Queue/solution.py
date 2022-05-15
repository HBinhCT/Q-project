n = int(input())
h = list(map(int, input().strip().split()))
print(1 + sum(h[i] > h[i + 1] for i in range(n - 1)))
