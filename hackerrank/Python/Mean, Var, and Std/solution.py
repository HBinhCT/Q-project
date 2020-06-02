import numpy

n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], dtype=int)
numpy.set_printoptions(legacy='1.13')
print(numpy.mean(a, axis=1))
print(numpy.var(a, axis=0))
print(numpy.std(a, axis=None))
