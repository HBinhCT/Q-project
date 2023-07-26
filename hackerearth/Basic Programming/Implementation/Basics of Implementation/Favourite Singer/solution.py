from collections import Counter

n = int(input())
singers = input().strip().split()
counter = list(Counter(singers).values())
print(counter.count(max(counter)))
