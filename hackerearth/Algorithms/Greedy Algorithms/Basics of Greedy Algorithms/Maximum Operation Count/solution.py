n, k = map(int, input().split())
a = sorted(map(int, input().strip().split()))
c = 0
j = m = n // 2
for i in range(m):
    while j < n and a[j] - a[i] < k:
        j += 1
    if j != n:
        c += 1
        j += 1
    else:
        break
print(c)
