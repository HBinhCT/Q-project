from math import ceil

t = int(input())
for _ in range(t):
    t0, t1, t2, v1, v2, d = map(int, input().strip().split())
    if t0 > t1 and t0 > t2:
        print("-1")
    else:
        if t0 > t2:
            m1 = ceil((d / v1) * 60) + t1
            print(m1)
        elif t0 > t1:
            m2 = ceil((d / v2) * 60) + t2
            print(m2)
        else:
            m1 = ceil((d / v1) * 60) + t1
            m2 = ceil((d / v2) * 60) + t2
            print(min(m1, m2))
