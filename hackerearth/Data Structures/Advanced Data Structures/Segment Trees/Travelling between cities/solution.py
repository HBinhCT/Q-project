from bisect import bisect_left, bisect_right
from collections import defaultdict

t = int(input())
for _ in range(t):
    n, k, q = map(int, input().strip().split())
    locations = list(map(int, input().strip().split()))
    counter = [0] * n
    positions = sorted(enumerate(locations), key=lambda a: a[-1])
    count = 0
    counter[positions[0][0]] = count
    for i in range(1, n):
        if positions[i][1] - positions[i - 1][1] > k:
            count += 1
        counter[positions[i][0]] = count
    groups = defaultdict(list)
    for i in range(n):
        groups[counter[i]].append(i)
    for _ in range(q):
        l, r, x = [int(i) - 1 for i in input().strip().split()]
        start = bisect_left(groups[counter[x]], l)
        end = bisect_right(groups[counter[x]], r)
        print(end - start)
