import numpy

n, q = map(int, input().strip().split())
arr = numpy.zeros(n, dtype=int)
for _ in range(q):
    p, l, r, *query = map(int, input().strip().split())
    if p == 1:
        x = query[0]
        arr[l - 1:r] |= x
    elif p == 2:
        x = query[0]
        arr[l - 1:r] &= x
    elif p == 3:
        x = query[0]
        arr[l - 1:r] ^= x
    elif p == 4:
        print(numpy.sum(arr[l - 1:r]))
    elif p == 5:
        print(numpy.bitwise_xor.reduce(arr[l - 1:r]))
