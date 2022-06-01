n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
total = sum(a[i] for i in range(k))
max_sum = total
for i in range(k - 1):
    total += a[n - 1 - i] - a[k - 1 - i]
    max_sum = max(max_sum, total)
print(max_sum)
