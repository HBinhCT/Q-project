from collections import defaultdict

n = int(input())
a = list(map(int, input().strip().split()))
calc = defaultdict(int)
for i in range(n):
    j = a[i] + (i + 1) * (i + 1)  # A[i] + i^2
    calc[j] += 1
count = 0
for i in range(n):
    j = a[i] - (i + 1) * (i + 1)  # A[j] - j^2
    if j in calc:
        count += calc[j]
print(count)
