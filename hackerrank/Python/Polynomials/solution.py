import numpy

P, x = numpy.array(input().strip().split(), dtype=float), int(input())
print(numpy.polyval(P, x))
