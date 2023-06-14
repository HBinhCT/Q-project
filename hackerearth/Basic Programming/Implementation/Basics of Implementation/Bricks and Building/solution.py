from collections import Counter
from sys import stdin

n = int(stdin.readline())
heights = [int(stdin.readline()) for _ in range(n)]
counter = Counter(heights)
highest = max(heights)
highest += 1
cache = {}
q = int(stdin.readline())
for _ in range(q):
    k = int(stdin.readline())
    if k in cache:
        print(cache[k])
    else:
        count = 0
        for i in range(k, highest, k):
            if i in counter:
                count += counter[i]
        cache[k] = count
        print(count)
