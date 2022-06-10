n = int(input())
a = list(map(int, input().strip().split()))
max_sums = set()
for i in range(n):
    max_sum = float('-inf')
    total = 0
    for j in range(i, n):
        total += a[j]
        max_sum = max(max_sum, total)
        total = max(total, 0)
        if max_sum not in max_sums:
            max_sums.add(max_sum)
print(sum(max_sums))
