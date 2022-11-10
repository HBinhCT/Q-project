from bisect import bisect_left, bisect
from collections import defaultdict
from sys import stdin

n, q = map(int, stdin.readline().strip().split())
drinks = list(map(int, stdin.readline().strip().split()))
idxes = defaultdict(list)
quants = set()
for i, v in enumerate(drinks, start=1):
    idxes[v].append(i)
    quants.add(v)
quants = sorted(quants)
first_drink = drinks[0]
mn = min(drinks)
mx = max(drinks)
for _ in range(q):
    l, r, k = map(int, stdin.readline().strip().split())
    x = k // 2
    if x < mn or x > mx:
        print(0)
        continue
    is_all = r - l + 1 == n
    ans = 0
    i = bisect_left(quants, k) - 1
    first = quants[i]
    while first > x:
        second = k - first
        if idxes[second]:
            if is_all:
                first_count = len(idxes[first])
                second_count = len(idxes[second])
            else:
                first_count = bisect(idxes[first], r)
                second_count = bisect(idxes[second], r)
                if 2 == l:
                    first_count -= first == first_drink
                    second_count -= second == first_drink
                elif 2 < l:
                    first_count -= bisect_left(idxes[first], l)
                    second_count -= bisect_left(idxes[second], l)
            ans += first_count * second_count
        i -= 1
        first = quants[i]
    if k - first == first:
        if is_all:
            first_count = len(idxes[first])
        else:
            first_count = bisect(idxes[first], r) - bisect_left(idxes[first], l)
        ans += first_count * (first_count - 1) // 2
    print(ans)
