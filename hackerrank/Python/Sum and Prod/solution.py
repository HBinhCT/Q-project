import numpy

n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], dtype=int)
print(numpy.prod(numpy.sum(a, axis=0), axis=0))
