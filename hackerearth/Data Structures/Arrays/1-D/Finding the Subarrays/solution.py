from itertools import accumulate

n = int(input())
a = list(map(int, input().strip().split()))
sums = list(accumulate(a, initial=0))
total = sum(a)
subarrays = []
for i in range(n):
    for j in range(i, n):
        ln = j - i + 1
        sum_subarray = sums[j + 1] - sums[i]
        if sum_subarray / ln > (total - sum_subarray) / (n - ln or 1):
            subarrays.append((i + 1, j + 1))
subarrays.sort()
print(len(subarrays))
for l, r in subarrays:
    print(l, r)
