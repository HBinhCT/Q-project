from bisect import insort_left, bisect_left

n, k = map(int, input().strip().split())
a = list(map(int, input().split()))
medians = [0]
for i in range(k - 1):
    insort_left(medians, a[i])
res = 0
for i in range(k - 1, n):
    insort_left(medians, a[i])
    median = medians[(k + 1) // 2]
    res = max(res, median)
    j = bisect_left(medians, a[i - k + 1])
    del medians[j]
print(pow(n, res, 1000000007))
