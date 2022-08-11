from numpy import array, where

n = int(input())
a = array(list(map(int, input().strip().split())))
q = int(input())
for _ in range(q):
    p, *query = map(int, input().strip().split())
    if p == 1:
        l, r, x = query
        a[l - 1:r] += x
    elif p == 2:
        l, r, y = query
        a[l - 1:r] *= y
    else:
        z = query[0]
        try:
            elements = where(a == z)[0]
            print(elements[-1] - elements[0] + 1)
        except:
            print(-1)
