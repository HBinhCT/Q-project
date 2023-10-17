from collections import Counter

n = int(input())
a = list(map(int, input().strip().split()))
counter = Counter(a)
ans = sorted(k for k, v in counter.items() if v == 1)
print(*ans)
