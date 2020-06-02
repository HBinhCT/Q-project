import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], dtype=int)
b = numpy.array([input().split() for _ in range(n)], dtype=int)
print(numpy.dot(a, b))
