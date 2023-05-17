from math import ceil

s, x, n = map(int, input().strip().split())
ty = sorted(tuple(map(int, input().strip().split())) for _ in range(n))
distance = s
days = i = 0
while distance > 0:
    if i < n:
        if ty[i][0] - 1 == days:
            distance -= ty[i][1]
            days += 1
            i += 1
        else:
            ti = ty[i][0]
            tj = ty[i - 1][0] + 1 if i > 0 else 1
            go = (ti - tj) * x
            if go < distance:
                distance -= go
                days += go // x
            else:
                i = n
    else:
        days += ceil(distance / x)
        distance -= x * ceil(distance / x)
print(days)
