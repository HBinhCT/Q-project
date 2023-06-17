from math import ceil, sqrt

n, k = map(int, input().strip().split())
x = list(map(int, input().strip().split()))
y = list(map(int, input().strip().split()))
dist = []
for i in range(n):
    d = sqrt(x[i] * x[i] + y[i] * y[i])
    dist.append(ceil(d))
dist.sort()
print(dist[k - 1])
