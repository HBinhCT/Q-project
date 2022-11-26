from math import gcd, sqrt

m = int(input())
arr = []
for i in range(m):
    arr.append(int(input()))
arr.sort()
subs = []
for i in range(1, m):
    subs.append(arr[i] - arr[i - 1])
x = subs[0]
for i in range(1, m - 1):
    x = gcd(x, subs[i])
res = []
for i in range(2, int(sqrt(x)) + 1):
    if x % i == 0:
        res.append(i)
        res.append(x // i)
res.append(x)
print(*sorted(set(res)))
