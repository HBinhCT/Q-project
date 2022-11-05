from bisect import bisect_right
from itertools import accumulate

t = int(input())
for _ in range(t):
    n, q = map(int, input().strip().split())
    a = sorted(map(int, input().strip().split()))
    pre = list(accumulate(a, initial=0))
    for _ in range(q):
        k = int(input()) - 1
        i = bisect_right(pre, k) - 1
        print(max(i, 0))
