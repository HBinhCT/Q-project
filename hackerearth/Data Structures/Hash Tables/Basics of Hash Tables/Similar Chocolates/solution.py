from collections import Counter

n = int(input())
a = list(map(int, input().strip().split()))
m = max(a) + 1
temp = [1] * m
for i in range(2, m):
    for j in range(i, m, i):
        temp[j] += 1
types = (temp[i] for i in a)
total = 0
for i in Counter(types).values():
    total += i * (i - 1) // 2
print(total)
