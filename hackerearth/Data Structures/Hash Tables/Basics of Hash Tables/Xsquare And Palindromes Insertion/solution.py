from collections import Counter

t = int(input())
for _ in range(t):
    s = input().strip()
    print(max(0, sum(1 for i in Counter(s).values() if i % 2) - 1))
