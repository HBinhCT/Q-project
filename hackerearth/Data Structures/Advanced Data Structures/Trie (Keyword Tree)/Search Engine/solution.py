from bisect import bisect_left
from functools import lru_cache

n, q = map(int, input().strip().split())
data = []
for _ in range(n):
    s, weight = input().strip().split()
    weight = int(weight)
    data.append((s, weight))
data.sort()


@lru_cache(maxsize=None)
def get_max_weight(txt):
    last_char = txt[-1]
    start = bisect_left(data, (txt, 0))
    end = bisect_left(data, (txt[:-1] + chr(ord(last_char) + 1), 0))
    potential = data[start:end]
    max_weight = -1
    if potential:
        potential.sort(key=lambda x: x[1])
        max_weight = potential[-1][1]
    return max_weight


for _ in range(q):
    t = input().strip()
    print(get_max_weight(t))
