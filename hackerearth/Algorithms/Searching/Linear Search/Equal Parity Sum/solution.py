from itertools import accumulate

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    for i in range(1, len(a), 2):
        a[i] *= -1
    sums = list(accumulate(a, initial=0))
    total = sums[-1]
    if total & 1:
        print('NO')
        continue
    total >>= 1
    seen = set()
    for i in sums:
        if i - total in seen:
            print('YES')
            break
        seen.add(i)
    else:
        print('NO')
