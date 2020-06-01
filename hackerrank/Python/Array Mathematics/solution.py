import numpy

n, m = list(map(int, input().split()))
a = numpy.array([input().split() for _ in range(n)], dtype=int)
b = numpy.array([input().split() for _ in range(n)], dtype=int)
print(a + b, a - b, a * b, a // b, a % b, a ** b, sep='\n')
