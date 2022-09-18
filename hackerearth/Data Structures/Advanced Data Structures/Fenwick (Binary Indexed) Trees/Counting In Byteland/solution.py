import numpy

n, q = map(int, input().strip().split())
byteland = numpy.zeros((n + 1, n + 1, n + 1), dtype=numpy.dtype('int64'))
total = 0
for _ in range(q):
    t, *query = map(int, input().strip().split())
    if t == 1:
        x, y, z, val = query
        byteland[x, y, z] += val
        total += val
    elif t == 2:
        x1, y1, z1, x2, y2, z2 = query
        print(total - numpy.sum(byteland[x1:x2 + 1, y1:y2 + 1, z1:z2 + 1]))
